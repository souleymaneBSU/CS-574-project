from __future__ import annotations

import functools
import io
import ipaddress
import logging
import mimetypes
import os
import os.path
import pathlib
import posixpath
import re
import socket
import socketserver
import string
import sys
import threading
import time
import traceback
import urllib.parse
import webbrowser
import wsgiref.simple_server
import wsgiref.util
from typing import Any, BinaryIO, Callable, Iterable

import watchdog.events
import watchdog.observers.polling

_SCRIPT_TEMPLATE_STR = """
var livereload = function(epoch, requestId) {
    var req, timeout;

    var poll = function() {
        req = new XMLHttpRequest();
        req.onloadend = function() {
            if (parseFloat(this.responseText) > epoch) {
                location.reload();
            } else {
                timeout = setTimeout(poll, this.status === 200 ? 0 : 3000);
            }
        };
        req.open("GET", "/livereload/" + epoch + "/" + requestId);
        req.send();
    }

    var stop = function() {
        if (req) {
            req.abort();
        }
        if (timeout) {
            clearTimeout(timeout);
        }
        req = timeout = undefined;
    };

    window.addEventListener("load", function() {
        if (document.visibilityState === "visible") {
            poll();
        }
    });
    window.addEventListener("visibilitychange", function() {
        if (document.visibilityState === "visible") {
            poll();
        } else {
            stop();
        }
    });
    window.addEventListener("beforeunload", stop);

    console.log('Enabled live reload');
}
livereload(${epoch}, ${request_id});
"""
_SCRIPT_TEMPLATE = string.Template(_SCRIPT_TEMPLATE_STR)


class _LoggerAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict) -> tuple[str, dict]:  # type: ignore[override]
        return time.strftime("[%H:%M:%S] ") + msg, kwargs


log = _LoggerAdapter(logging.getLogger(__name__), {})


def _normalize_mount_path(mount_path: str) -> str:
    """Ensure the mount path starts and ends with a slash."""
    return ("/" + mount_path.lstrip("/")).rstrip("/") + "/"


def _serve_url(host: str, port: int, path: str) -> str:
    return f"http://{host}:{port}{_normalize_mount_path(path)}"


class LiveReloadServer(socketserver.ThreadingMixIn, wsgiref.simple_server.WSGIServer):
    daemon_threads = True
    poll_response_timeout = 60

    def __init__(
        self,
        builder: Callable[[], None],
        host: str,
        port: int,
        root: str,
        mount_path: str = "/",
        polling_interval: float = 0.5,
        shutdown_delay: float = 0.25,
    ) -> None:
        self.builder = builder
        try:
            if isinstance(ipaddress.ip_address(host), ipaddress.IPv6Address):
                self.address_family = socket.AF_INET6
        except Exception:
            pass
        self.root = os.path.abspath(root)
        self.mount_path = _normalize_mount_path(mount_path)
        self.url = _serve_url(host, port, mount_path)
        self.build_delay = 0.1
        self.shutdown_delay = shutdown_delay
        # To allow custom error pages.
        self.error_handler: Callable[[int], bytes | None] = lambda code: None

        super().__init__((host, port), _Handler, bind_and_activate=False)
        self.set_app(self.serve_request)

        self._wanted_epoch = _timestamp()  # The version of the site that started building.
        self._visible_epoch = self._wanted_epoch  # Latest fully built version of the site.
        self._epoch_cond = threading.Condition()  # Must be held when accessing _visible_epoch.

        self._rebuilds_from_watch: int = 0
        self._want_rebuild: bool = False
        self._rebuilds: int = 0
        self._rebuild_cond = threading.Condition()  # Must be held when accessing _want_rebuild.

        self._shutdown = False
        self.serve_thread = threading.Thread(target=lambda: self.serve_forever(shutdown_delay))
        self.observer = watchdog.observers.polling.PollingObserver(timeout=polling_interval)

        self._watched_paths: dict[str, int] = {}
        self._watch_refs: dict[str, Any] = {}

    def watch(self, path: str, func: None = None, *, recursive: bool = True) -> None:
        """Add the 'path' to watched paths, call the function and reload when any file changes under it."""
        path = os.path.abspath(path)
        if not (func is None or func is self.builder):  # type: ignore[unreachable]
            raise TypeError("Plugins can no longer pass a 'func' parameter to watch().")

        if path in self._watched_paths:
            self._watched_paths[path] += 1
            return
        self._watched_paths[path] = 1

        def callback(event):
            if event.is_directory:
                return
            log.debug(str(event))
            with self._rebuild_cond:
                self._want_rebuild = True
                self._rebuilds_from_watch = self._rebuilds_from_watch + 1
                self._rebuild_cond.notify_all()

        handler = watchdog.events.FileSystemEventHandler()
        handler.on_any_event = callback  # type: ignore[method-assign]
        log.debug(f"Watching '{path}'")
        self._watch_refs[path] = self.observer.schedule(handler, path, recursive=recursive)

    def unwatch(self, path: str) -> None:
        """Stop watching file changes for path. Raises if there was no corresponding `watch` call."""
        path = os.path.abspath(path)

        self._watched_paths[path] -= 1
        if self._watched_paths[path] <= 0:
            self._watched_paths.pop(path)
            self.observer.unschedule(self._watch_refs.pop(path))

    def serve(self, *, open_in_browser=False):
        self.server_bind()
        self.server_activate()

        if self._watched_paths:
            self.observer.start()

            paths_str = ", ".join(f"'{_try_relativize_path(path)}'" for path in self._watched_paths)
            log.info(f"Watching paths for changes: {paths_str}")

        if open_in_browser:
            log.info(f"Serving on {self.url} and opening it in a browser")
        else:
            log.info(f"Serving on {self.url}")
        self.serve_thread.start()
        if open_in_browser:
            webbrowser.open(self.url)

        self._build_loop()

    def _build_loop(self):
        while True:
            with self._rebuild_cond:
                assert not self._watched_paths or self._rebuilds_from_watch, 'Build loop running without any watched files'
                while not self._rebuild_cond.wait_for(
                    lambda: self._want_rebuild or self._shutdown, timeout=self.shutdown_delay
                ):
                    # We could have used just one wait instead of a loop + timeout, but we need
                    # occasional breaks, otherwise on Windows we can't receive KeyboardInterrupt.
                    pass
                if self._shutdown:
                    break
                log.info("Detected file changes")
                while self._rebuild_cond.wait(timeout=self.build_delay):
                    log.debug("Waiting for file changes to stop happening")

                self._wanted_epoch = _timestamp()
                self._want_rebuild = False
                self._rebuilds = self._rebuilds + 1

            try:
                self.builder()
            except Exception as e:
                if isinstance(e, SystemExit):
                    print(e, file=sys.stderr)  # noqa: T201
                else:
                    traceback.print_exc()
                log.error(
                    "An error happened during the rebuild. The server will appear stuck until build errors are resolved."
                )
                continue

            with self._epoch_cond:
                log.info("Reloading browsers")
                self._visible_epoch = self._wanted_epoch
                self._epoch_cond.notify_all()

            assert self._want_rebuild == False, 'Want rebuild is still true after completing the build'
            assert self._rebuilds <= self._rebuilds_from_watch, 'More rebuilds than file changes'

    def shutdown(self, wait=False) -> None:
        self.observer.stop()
        with self._rebuild_cond:
            self._shutdown = True
            self._rebuild_cond.notify_all()

        if self.serve_thread.is_alive():
            super().shutdown()
        self.server_close()
        if wait:
            self.serve_thread.join()
            self.observer.join()

    def serve_request(self, environ, start_response) -> Iterable[bytes]:
        try:
            result = self._serve_request(environ, start_response)
        except Exception:
            code = 500
            msg = "500 Internal Server Error"
            log.exception(msg)
        else:
            if result is not None:
                return result
            code = 404
            msg = "404 Not Found"

        error_content = None
        try:
            error_content = self.error_handler(code)
        except Exception:
            log.exception("Failed to render an error message!")
        if error_content is None:
            error_content = msg.encode()

        start_response(msg, [("Content-Type", "text/html")])
        return [error_content]

    def _serve_request(self, environ, start_response) -> Iterable[bytes] | None:
        # https://bugs.python.org/issue16679
        # https://github.com/bottlepy/bottle/blob/f9b1849db4/bottle.py#L984
        path = environ["PATH_INFO"].encode("latin-1").decode("utf-8", "ignore")

        if path.startswith("/livereload/"):
            if m := re.fullmatch(r"/livereload/([0-9]+)/[0-9]+", path):
                epoch = int(m[1])
                start_response("200 OK", [("Content-Type", "text/plain")])

                def condition():
                    return self._visible_epoch > epoch

                with self._epoch_cond:
                    if not condition():
                        # Stall the browser, respond as soon as there's something new.
                        # If there's not, respond anyway after a minute.
                        self._log_poll_request(environ.get("HTTP_REFERER"), request_id=path)
                        self._epoch_cond.wait_for(condition, timeout=self.poll_response_timeout)
                    return [b"%d" % self._visible_epoch]

        if (path + "/").startswith(self.mount_path):
            rel_file_path = path[len(self.mount_path) :]

            if path.endswith("/"):
                rel_file_path += "index.html"
            # Prevent directory traversal - normalize the path.
            rel_file_path = posixpath.normpath("/" + rel_file_path).lstrip("/")
            file_path = os.path.join(self.root, rel_file_path)
        elif path == "/":
            start_response("302 Found", [("Location", urllib.parse.quote(self.mount_path))])
            return []
        else:
            return None  # Not found

        # Wait until the ongoing rebuild (if any) finishes, so we're not serving a half-built site.
        with self._epoch_cond:
            self._epoch_cond.wait_for(lambda: self._visible_epoch == self._wanted_epoch)
            epoch = self._visible_epoch

        try:
            file: BinaryIO = open(file_path, "rb")
        except OSError:
            if not path.endswith("/") and os.path.isfile(os.path.join(file_path, "index.html")):
                start_response("302 Found", [("Location", urllib.parse.quote(path) + "/")])
                return []
            return None  # Not found

        if self._watched_paths and file_path.endswith(".html"):
            with file:
                content = file.read()
            content = self._inject_js_into_html(content, epoch)
            file = io.BytesIO(content)
            content_length = len(content)
        else:
            content_length = os.path.getsize(file_path)

        content_type = self._guess_type(file_path)
        start_response(
            "200 OK", [("Content-Type", content_type), ("Content-Length", str(content_length))]
        )
        return wsgiref.util.FileWrapper(file)

    def _inject_js_into_html(self, content, epoch):
        try:
            body_end = content.rindex(b"</body>")
        except ValueError:
            body_end = len(content)
        # The page will reload if the livereload poller returns a newer epoch than what it knows.
        # The other timestamp becomes just a unique identifier for the initiating page.
        script = _SCRIPT_TEMPLATE.substitute(epoch=epoch, request_id=_timestamp())
        return b"%b<script>%b</script>%b" % (
            content[:body_end],
            script.encode(),
            content[body_end:],
        )

    @classmethod
    @functools.lru_cache  # "Cache" to not repeat the same message for the same browser tab.
    def _log_poll_request(cls, url, request_id):
        log.info(f"Browser connected: {url}")

    @classmethod
    def _guess_type(cls, path):
        # MkDocs only ensures a few common types (as seen in livereload_tests.py::test_mime_types).
        # Other uncommon types will not be accepted.
        if path.endswith((".js", ".JS", ".mjs")):
            return "application/javascript"
        if path.endswith(".gz"):
            return "application/gzip"

        guess, _ = mimetypes.guess_type(path)
        if guess:
            return guess
        return "application/octet-stream"


class _Handler(wsgiref.simple_server.WSGIRequestHandler):
    def log_request(self, code="-", size="-"):
        level = logging.DEBUG if str(code) == "200" else logging.WARNING
        log.log(level, f'"{self.requestline}" code {code}')

    def log_message(self, format, *args):
        log.debug(format, *args)


def _timestamp() -> int:
    return round(time.monotonic() * 1000)


def _try_relativize_path(path: str) -> str:
    """Make the path relative to current directory if it's under that directory."""
    p = pathlib.Path(path)
    try:
        p = p.relative_to(os.getcwd())
    except ValueError:
        pass
    return str(p)
