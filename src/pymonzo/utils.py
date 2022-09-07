"""
pymonzo utils.
"""
from datetime import datetime, timedelta
from typing import Any, Callable, List, Tuple
from wsgiref.simple_server import make_server
from wsgiref.util import request_uri


def n_days_ago(n: int) -> datetime:
    """
    Return datetime that was n days ago.
    """
    today = datetime.now()
    delta = timedelta(days=n)
    return today - delta


def empty_str_to_none(value: Any) -> Any:
    """
    Return passed string, unless it's empty, in which case return 'None'.
    """
    if value == "":
        return None
    return value


class WSGIApp:
    """
    Bare-bones WSGI app made for retrieving the OAuth callback.
    """

    last_request_uri = ""

    def __call__(
        self,
        environ: dict,
        start_response: Callable[[str, List[Tuple[str, str]]], None],
    ) -> List[bytes]:
        """
        Implement WSGI interface and save the URL of the callback.
        """
        start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
        self.last_request_uri = request_uri(environ)
        msg = "Monzo OAuth authorization complete."
        return [msg.encode("utf-8")]


def get_authorization_response(host: str, port: int) -> str:
    """
    Get OAuth authorization response.

    It's done by creating a bare-bones HTTP server and retrieving the OAuth callback.
    """
    wsgi_app = WSGIApp()
    with make_server(host, port, wsgi_app) as server:  # type: ignore
        server.handle_request()

    return wsgi_app.last_request_uri
