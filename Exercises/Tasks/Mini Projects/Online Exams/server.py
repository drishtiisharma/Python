from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import os


from routes.pages import (
    login_page,
    student_page,
    admin_page,
    admin_students_page,
    admin_add_student_page
)

from routes.login import (
    login_api,
    logout_api
)

from routes.student.api import (
    student_details_api
)

from routes.admin.api import (
    get_students_api,
    add_student_api,
    update_student_api,
    delete_student_api
)

from utils.files import serve_static


# -------------------------------------------------
# Server configuration
# -------------------------------------------------

HOST = "localhost"
PORT = 8000

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# -------------------------------------------------
# Static files
# -------------------------------------------------

STATIC_FILES = {

    "/static/css/style.css":
        ("static/css/style.css", "text/css"),

    "/static/js/login.js":
        ("static/js/login.js", "application/javascript"),

    "/static/js/student/student.js":
        ("static/js/student/student.js", "application/javascript"),

    "/static/js/admin/dashboard.js":
        ("static/js/admin/dashboard.js", "application/javascript"),

    "/static/js/admin/see_all_students.js":
        ("static/js/admin/see_all_students.js", "application/javascript"),

    "/static/js/admin/add_student.js":
        ("static/js/admin/add_student.js", "application/javascript")
}


# -------------------------------------------------
# HTTP Handler
# -------------------------------------------------

class MyHandler(BaseHTTPRequestHandler):


    # -------------------------------------------------
    # GET
    # -------------------------------------------------

    def do_GET(self):

        parsed_url = urlparse(self.path)
        path = parsed_url.path


        # -----------------------------
        # HTML pages
        # -----------------------------

        if path == "/":

            login_page(
                self,
                BASE_DIR
            )

            return


        if path == "/student":

            student_page(
                self,
                BASE_DIR
            )

            return


        if path == "/admin":

            admin_page(
                self,
                BASE_DIR
            )

            return


        if path == "/admin/students":

            admin_students_page(
                self,
                BASE_DIR
            )

            return


        if path == "/admin/students/add":

            admin_add_student_page(
                self,
                BASE_DIR
            )

            return


        # -----------------------------
        # Student API
        # -----------------------------

        if path == "/api/student/me":

            student_details_api(self)

            return


        # -----------------------------
        # Admin API
        # -----------------------------

        if path == "/api/admin/students":

            get_students_api(self)

            return


        # -----------------------------
        # Static files
        # -----------------------------

        if path in STATIC_FILES:

            file_path, content_type = STATIC_FILES[path]

            serve_static(
                self,
                BASE_DIR,
                file_path,
                content_type
            )

            return


        # -----------------------------
        # Not found
        # -----------------------------

        self.send_error(
            404,
            "Page not found"
        )


    # -------------------------------------------------
    # POST
    # -------------------------------------------------

    def do_POST(self):

        parsed_url = urlparse(self.path)
        path = parsed_url.path


        if path == "/api/login":

            login_api(self)

            return


        if path == "/api/logout":

            logout_api(self)

            return


        if path == "/api/admin/students":

            add_student_api(self)

            return


        self.send_error(
            404,
            "API endpoint not found"
        )


    # -------------------------------------------------
    # PUT
    # -------------------------------------------------

    def do_PUT(self):

        parsed_url = urlparse(self.path)
        path = parsed_url.path


        if path.startswith(
            "/api/admin/students/"
        ):

            update_student_api(
                self,
                path
            )

            return


        self.send_error(
            404,
            "API endpoint not found"
        )


    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def do_DELETE(self):

        parsed_url = urlparse(self.path)
        path = parsed_url.path


        if path.startswith(
            "/api/admin/students/"
        ):

            delete_student_api(
                self,
                path
            )

            return


        self.send_error(
            404,
            "API endpoint not found"
        )


# -------------------------------------------------
# Start server
# -------------------------------------------------

if __name__ == "__main__":

    server = HTTPServer(
        (HOST, PORT),
        MyHandler
    )

    print(
        f"Server running at http://{HOST}:{PORT}"
    )

    try:

        server.serve_forever()

    except KeyboardInterrupt:

        print("\nServer stopped.")

    finally:

        server.server_close()
