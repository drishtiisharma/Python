from utils.sessions import get_session
from utils.files import serve_html


def login_page(handler, base_dir):

    serve_html(
        handler,
        base_dir,
        "login.html"
    )


def student_page(handler, base_dir):

    session = get_session(handler)

    if not session:

        handler.send_response(302)
        handler.send_header("Location", "/")
        handler.end_headers()

        return

    if session["role"] != "student":

        handler.send_response(302)
        handler.send_header("Location", "/admin")
        handler.end_headers()

        return

    serve_html(
        handler,
        base_dir,
        "student.html"
    )


def admin_page(handler, base_dir):

    session = get_session(handler)

    if not session:

        handler.send_response(302)
        handler.send_header("Location", "/")
        handler.end_headers()

        return

    if session["role"] != "admin":

        handler.send_response(302)
        handler.send_header("Location", "/student")
        handler.end_headers()

        return

    serve_html(
        handler,
        base_dir,
        "admin/dashboard.html"
    )


def admin_students_page(handler, base_dir):

    session = get_session(handler)

    if not session:

        handler.send_response(302)
        handler.send_header("Location", "/")
        handler.end_headers()

        return

    if session["role"] != "admin":

        handler.send_response(302)
        handler.send_header("Location", "/student")
        handler.end_headers()

        return

    serve_html(
        handler,
        base_dir,
        "admin/see_all_students.html"
    )


def admin_add_student_page(handler, base_dir):

    session = get_session(handler)

    if not session:

        handler.send_response(302)
        handler.send_header("Location", "/")
        handler.end_headers()

        return

    if session["role"] != "admin":

        handler.send_response(302)
        handler.send_header("Location", "/student")
        handler.end_headers()

        return

    serve_html(
        handler,
        base_dir,
        "admin/add_student.html"
    )
