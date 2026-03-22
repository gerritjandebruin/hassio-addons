"""WSGI wrapper for Fava with Home Assistant ingress support.

Home Assistant's ingress proxy strips the /api/hassio_ingress/<token> prefix
before forwarding requests to the add-on. Fava's --prefix flag uses
DispatcherMiddleware which expects the prefix in the request path, causing
a mismatch (white screen).

This wrapper sets SCRIPT_NAME so Flask generates correct URLs with the
ingress prefix, while keeping routing at / where the requests actually arrive.
"""
import os
import signal
import sys

from cheroot.wsgi import Server
from fava.application import create_app


class IngressMiddleware:
    """Set SCRIPT_NAME for correct URL generation without affecting routing."""

    def __init__(self, wsgi_app, prefix):
        self.wsgi_app = wsgi_app
        self.prefix = prefix.rstrip("/")

    def __call__(self, environ, start_response):
        environ["SCRIPT_NAME"] = self.prefix
        return self.wsgi_app(environ, start_response)


def main():
    beancount_file = os.path.abspath(sys.argv[1])
    port = int(sys.argv[2])
    prefix = sys.argv[3] if len(sys.argv) > 3 else ""

    # Add beancount file directory to sys.path so plugins can be found
    beancount_dir = os.path.dirname(beancount_file)
    if beancount_dir not in sys.path:
        sys.path.insert(0, beancount_dir)

    app = create_app([beancount_file])

    if prefix:
        app.wsgi_app = IngressMiddleware(app.wsgi_app, prefix)

    server = Server(("127.0.0.1", port), app)
    signal.signal(signal.SIGTERM, lambda *_: server.stop())
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


if __name__ == "__main__":
    main()
