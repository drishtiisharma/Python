from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

import os

from routes.signup.api import signup_api

from routes.pages import (
    login_page,
    signup_page,
    student_page,
    admin_page,
    admin_students_page,
    admin_add_student_page,
    admin_admins_page,
    admin_exams_page,
    student_exams_page,
    student_quiz_page,
    student_results_page
)

from routes.login import (
    login_api,
    logout_api
)

from routes.student.api import (
    student_details_api,
    update_student_profile_api,
    change_student_password_api,
    get_available_exams_api,
    start_exam_attempt_api,
    get_attempt_quiz_data_api,
    save_student_answer_api,
    submit_exam_attempt_api,
    get_attempt_result_api,
    get_student_results_api,
    get_detailed_result_api
)

from routes.admin.api import (
    get_students_api,
    add_student_api,
    update_student_api,
    delete_student_api
)

from routes.admin.api import (
    get_admins_api,
    update_admin_api,
    delete_admin_api
)

from routes.admin.api import (
    get_subjects_api,
    add_subject_api,
    get_exams_api,
    get_exam_by_id_api,
    add_exam_api,
    update_exam_api,
    delete_exam_api,
    toggle_exam_status_api
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

    "/static/js/signup.js":
        ("static/js/signup.js", "application/javascript"),

    "/static/js/student/student.js":
        ("static/js/student/student.js", "application/javascript"),

    "/static/js/admin/dashboard.js":
        ("static/js/admin/dashboard.js", "application/javascript"),

    "/static/js/admin/see_all_students.js":
        ("static/js/admin/see_all_students.js", "application/javascript"),

    "/static/js/admin/add_student.js":
        ("static/js/admin/add_student.js", "application/javascript"),

    
    "/static/js/admin/see_all_admins.js":
        ("static/js/admin/see_all_admins.js", "application/javascript"),

    "/static/js/admin/exams.js":
        ("static/js/admin/exams.js", "application/javascript"),

    "/static/js/student/exams.js":
        ("static/js/student/exams.js", "application/javascript"),

    "/static/js/student/quiz.js":
        ("static/js/student/quiz.js", "application/javascript"),

    "/static/js/student/results.js":
        ("static/js/student/results.js", "application/javascript"),
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


        if path == "/signup":

            signup_page(
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


        if path == "/student/exams":

            student_exams_page(
                self,
                BASE_DIR
            )

            return


        if path == "/student/quiz":

            student_quiz_page(
                self,
                BASE_DIR
            )

            return


        if path == "/student/results":

            student_results_page(
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

        
        if path == "/admin/admins":

            admin_admins_page(
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


        if path == "/admin/exams":

            admin_exams_page(
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


        if path == "/api/student/exams":

            get_available_exams_api(self)

            return


        if path.startswith("/api/student/attempts/") and path.endswith("/result"):

            get_attempt_result_api(
                self,
                path
            )

            return


        if path.startswith("/api/student/attempts/"):

            get_attempt_quiz_data_api(
                self,
                path
            )

            return


        if path == "/api/student/results":

            get_student_results_api(self)

            return


        if path.startswith("/api/student/results/"):

            get_detailed_result_api(
                self,
                path
            )

            return



        # -----------------------------
        # Admin API
        # -----------------------------

        if path == "/api/admin/students":

            get_students_api(self)

            return

        
        if path == "/api/admin/admins":

            get_admins_api(self)

            return


        if path == "/api/admin/subjects":

            get_subjects_api(self)

            return


        if path == "/api/admin/exams":

            get_exams_api(self)

            return


        if path.startswith("/api/admin/exams/"):

            get_exam_by_id_api(self, path)

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


        # -----------------------------
        # Login
        # -----------------------------

        if path == "/api/login":

            login_api(self)

            return


        # -----------------------------
        # Signup
        # -----------------------------

        if path == "/api/signup":

            signup_api(self)

            return


        # -----------------------------
        # Logout
        # -----------------------------

        if path == "/api/logout":

            logout_api(self)

            return


        # -----------------------------
        # Add student
        # -----------------------------

        if path == "/api/admin/students":

            add_student_api(self)

            return


        if path == "/api/admin/subjects":

            add_subject_api(self)

            return


        if path == "/api/admin/exams":

            add_exam_api(self)

            return


        # -----------------------------
        # Student Quiz Attempts
        # -----------------------------

        if path.startswith("/api/student/exams/") and path.endswith("/start"):

            start_exam_attempt_api(
                self,
                path
            )

            return


        if path.startswith("/api/student/attempts/") and path.endswith("/answer"):

            save_student_answer_api(
                self,
                path
            )

            return


        if path.startswith("/api/student/attempts/") and path.endswith("/submit"):

            submit_exam_attempt_api(
                self,
                path
            )

            return


        # -----------------------------
        # Not found
        # -----------------------------

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


        # -----------------------------
        # Student profile
        # -----------------------------

        if path == "/api/student/profile":

            update_student_profile_api(self)

            return


        # -----------------------------
        # Student password
        # -----------------------------

        if path == "/api/student/password":

            change_student_password_api(self)

            return


        # -----------------------------
        # Admin update student
        # -----------------------------

        if path.startswith(
            "/api/admin/students/"
        ):

            update_student_api(
                self,
                path
            )

            return


        
        if path.startswith("/api/admin/admins/"):

            update_admin_api(
                self,
                path
            )

            return


        if path.startswith("/api/admin/exams/") and path.endswith("/status"):

            toggle_exam_status_api(
                self,
                path
            )

            return


        if path.startswith("/api/admin/exams/"):

            update_exam_api(
                self,
                path
            )

            return


        # -----------------------------
        # Not found
        # -----------------------------

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


        # -----------------------------
        # Admin delete student
        # -----------------------------

        if path.startswith(
            "/api/admin/students/"
        ):

            delete_student_api(
                self,
                path
            )

            return

        
        if path.startswith("/api/admin/admins/"):

            delete_admin_api(
                self,
                path
            )

            return


        if path.startswith("/api/admin/exams/"):

            delete_exam_api(
                self,
                path
            )

            return



        # -----------------------------
        # Not found
        # -----------------------------

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