from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from http.cookies import SimpleCookie

import json
import os

from routes.login import login, logout
from routes.student.dashboard import get_student_details
from routes.admin.students import get_all_students

# -------------------------------------------------
# Server configuration
# -------------------------------------------------

HOST = "localhost"
PORT = 8000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------------------------
# Session storage
# -------------------------------------------------

sessions = {}


# -------------------------------------------------
# Request Handler
# -------------------------------------------------

class MyHandler(BaseHTTPRequestHandler):

    # =================================================
    # Helper: Send JSON response
    # =================================================

    def send_json(self, data, status=200, headers=None):

        response = json.dumps(data).encode("utf-8")

        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        if headers:

            for key, value in headers.items():

                self.send_header(
                    key,
                    value
                )

        self.end_headers()

        self.wfile.write(response)


    # =================================================
    # Helper: Read JSON body
    # =================================================

    def get_json_body(self):

        content_length = int(
            self.headers.get(
                "Content-Length",
                0
            )
        )

        body = self.rfile.read(content_length)

        return json.loads(
            body.decode("utf-8")
        )


    # =================================================
    # Helper: Get session ID from cookie
    # =================================================

    def get_session_id(self):

        cookie_header = self.headers.get("Cookie")

        if not cookie_header:

            return None

        cookie = SimpleCookie()

        cookie.load(cookie_header)

        if "session_id" not in cookie:

            return None

        return cookie["session_id"].value


    # =================================================
    # Helper: Get current session
    # =================================================

    def get_session(self):

        session_id = self.get_session_id()

        if not session_id:

            return None

        return sessions.get(session_id)


    # =================================================
    # Helper: Serve HTML
    # =================================================

    def serve_html(self, filename):

        filepath = os.path.join(
            BASE_DIR,
            "templates",
            filename
        )

        if not os.path.exists(filepath):

            self.send_error(
                404,
                "HTML file not found"
            )

            return

        with open(filepath, "rb") as file:

            content = file.read()

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html"
        )

        self.send_header(
            "Content-Length",
            str(len(content))
        )

        self.end_headers()

        self.wfile.write(content)


    # =================================================
    # Helper: Serve static files
    # =================================================

    def serve_static(self, filepath, content_type):

        full_path = os.path.join(
            BASE_DIR,
            filepath
        )

        if not os.path.exists(full_path):

            self.send_error(
                404,
                "File not found"
            )

            return

        with open(full_path, "rb") as file:

            content = file.read()

        self.send_response(200)

        self.send_header(
            "Content-Type",
            content_type
        )

        self.send_header(
            "Content-Length",
            str(len(content))
        )

        self.end_headers()

        self.wfile.write(content)


    # =================================================
    # GET requests
    # =================================================

    def do_GET(self):

        parsed_url = urlparse(self.path)

        path = parsed_url.path


        # -------------------------------------------------
        # Login page
        # -------------------------------------------------

        if path == "/":

            self.serve_html("login.html")

            return


        # -------------------------------------------------
        # Student dashboard
        # -------------------------------------------------

        if path == "/student":

            session = self.get_session()

            if not session:

                self.send_response(302)

                self.send_header(
                    "Location",
                    "/"
                )

                self.end_headers()

                return


            # Make sure only students access this page

            if session["role"] != "student":

                self.send_response(302)

                self.send_header(
                    "Location",
                    "/admin"
                )

                self.end_headers()

                return


            self.serve_html("student.html")

            return


        # -------------------------------------------------
        # Admin dashboard
        # -------------------------------------------------

        if path == "/admin":

            session = self.get_session()

            if not session:

                self.send_response(302)

                self.send_header(
                    "Location",
                    "/"
                )

                self.end_headers()

                return


            # Only admins can access admin dashboard

            if session["role"] != "admin":

                self.send_response(302)

                self.send_header(
                    "Location",
                    "/student"
                )

                self.end_headers()

                return


            self.serve_html("admin.html")

            return


        # -------------------------------------------------
        # Student information API
        # -------------------------------------------------

        if path == "/api/student/me":

            session = self.get_session()

            if not session:

                self.send_json(
                    {
                        "success": False,
                        "message": "Not logged in"
                    },
                    401
                )

                return


            if session["role"] != "student":

                self.send_json(
                    {
                        "success": False,
                        "message": "Access denied"
                    },
                    403
                )

                return


            student = get_student_details(
                session["user_id"]
            )


            if not student:

                self.send_json(
                    {
                        "success": False,
                        "message": "Student not found"
                    },
                    404
                )

                return


            # datetime cannot directly be converted to JSON

            if student["created_at"]:

                student["created_at"] = (
                    student["created_at"].isoformat()
                )


            self.send_json(
                {
                    "success": True,
                    "student": student
                }
            )

            return


        # -------------------------------------------------
        # Admin: Get all students
        # -------------------------------------------------

        if path == "/api/admin/students":

            session = self.get_session()

            if not session:

                self.send_json(
                    {
                        "success": False,
                        "message": "Not logged in"
                    },
                    401
                )

                return


            # Only admin can access this API

            if session["role"] != "admin":

                self.send_json(
                    {
                        "success": False,
                        "message": "Access denied"
                    },
                    403
                )

                return


            try:

                students = get_all_students()


                # Convert datetime to string

                for student in students:

                    if student["created_at"]:

                        student["created_at"] = (
                            student["created_at"].isoformat()
                        )


                self.send_json(
                    {
                        "success": True,
                        "students": students
                    }
                )

            except Exception as e:

                print(
                    "Error loading students:",
                    e
                )

                self.send_json(
                    {
                        "success": False,
                        "message": "Unable to load students"
                    },
                    500
                )

            return

        # -------------------------------------------------
        # CSS
        # -------------------------------------------------

        if path == "/static/css/style.css":

            self.serve_static(
                "static/css/style.css",
                "text/css"
            )

            return


        # -------------------------------------------------
        # Login JavaScript
        # -------------------------------------------------

        if path == "/static/js/login.js":

            self.serve_static(
                "static/js/login.js",
                "application/javascript"
            )

            return


        # -------------------------------------------------
        # Student JavaScript
        # -------------------------------------------------

        if path == "/static/js/student/student.js":

            self.serve_static(
                "static/js/student/student.js",
                "application/javascript"
            )

            return


        # -------------------------------------------------
        # Admin JavaScript
        # -------------------------------------------------

        if path == "/static/js/admin/admin.js":

            self.serve_static(
                "static/js/admin/admin.js",
                "application/javascript"
            )

            return


        # -------------------------------------------------
        # Unknown GET request
        # -------------------------------------------------

        self.send_error(
            404,
            "Page not found"
        )


    # =================================================
    # POST requests
    # =================================================

    def do_POST(self):

        parsed_url = urlparse(self.path)

        path = parsed_url.path


        # -------------------------------------------------
        # Login
        # -------------------------------------------------

        if path == "/api/login":

            try:

                data = self.get_json_body()

                email = data.get("email")

                password = data.get("password")


                if not email or not password:

                    self.send_json(
                        {
                            "success": False,
                            "message":
                                "Email and password are required"
                        },
                        400
                    )

                    return


                result = login(
                    email,
                    password,
                    sessions
                )


                if not result["success"]:

                    self.send_json(
                        result,
                        401
                    )

                    return


                session_id = result["session_id"]


                self.send_json(

                    {
                        "success": True,
                        "message": "Login successful",
                        "role": result["role"]
                    },

                    200,

                    {
                        "Set-Cookie":
                            f"session_id={session_id}; "
                            "HttpOnly; "
                            "Path=/; "
                            "SameSite=Lax"
                    }

                )

            except Exception as e:

                print(
                    "Login error:",
                    e
                )

                self.send_json(

                    {
                        "success": False,
                        "message": "Server error"
                    },

                    500

                )

            return


        # -------------------------------------------------
        # Logout
        # -------------------------------------------------

        if path == "/api/logout":

            session_id = self.get_session_id()


            if session_id:

                logout(
                    session_id,
                    sessions
                )


            self.send_json(

                {
                    "success": True
                },

                200,

                {
                    "Set-Cookie":
                        "session_id=; "
                        "HttpOnly; "
                        "Path=/; "
                        "Max-Age=0"
                }

            )

            return


        # -------------------------------------------------
        # Unknown POST request
        # -------------------------------------------------

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