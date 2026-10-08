sessions = {}


def get_session_id(handler):

    cookie_header = handler.headers.get("Cookie")

    if not cookie_header:
        return None

    from http.cookies import SimpleCookie

    cookie = SimpleCookie()

    cookie.load(cookie_header)

    if "session_id" not in cookie:
        return None

    return cookie["session_id"].value


def get_session(handler):

    session_id = get_session_id(handler)

    if not session_id:
        return None

    return sessions.get(session_id)