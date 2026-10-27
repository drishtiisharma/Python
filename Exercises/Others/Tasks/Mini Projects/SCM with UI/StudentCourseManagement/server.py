from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from routes.login import login_user

from routes.admin.students import (
    get_all_students,
    register_student,
    update_student,
    remove_student
)

from routes.admin.courses import (
    get_all_courses,
    add_course,
    enroll_student,
    remove_student_from_course
)

from routes.admin.enrollments import (
    get_all_enrollments
)

from routes.admin.dashboard import get_dashboard_data

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.send_file(
                "templates/login.html",
                "text/html"
            )

        elif self.path == "/static/css/style.css":
            self.send_file(
                "static/css/style.css",
                "text/css"
            )

        elif self.path == "/static/js/login.js":
            self.send_file(
                "static/js/login.js",
                "application/javascript"
            )
            
        elif self.path == "/admin.html":
            self.send_file(
                "templates/admin.html",
                "text/html"
            )

        elif self.path == "/static/js/admin/admin.js":
            self.send_file(
                "static/js/admin/admin.js",
                "application/javascript"
            )

        elif self.path == "/api/students":

            students = get_all_students()
            self.send_json(students)

        elif self.path == "/api/courses":

            courses = get_all_courses()

            self.send_json(courses)

        elif self.path == "/api/enrollments":

            enrollments = get_all_enrollments()

            self.send_json(enrollments)

        elif self.path == "/api/dashboard":

            data = get_dashboard_data()

            self.send_json(data)
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

    def do_POST(self):

        if self.path == "/api/login":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            email = data["email"]
            password = data["password"]

            result = login_user(email, password)

            self.send_json(result)

        elif self.path == "/api/students/register":
        
                    content_length = int(
                        self.headers["Content-Length"]
                    )
        
                    body = self.rfile.read(content_length)
        
                    data = json.loads(body)
        
                    result = register_student(
                        data["fname"],
                        data["lname"],
                        data["age"],
                        data["gender"],
                        data["email"],
                        data["password"]
                    )
        
                    self.send_json(result)

        elif self.path == "/api/students/update":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            result = update_student(
                data["student_id"],
                data["fname"],
                data["lname"],
                data["age"],
                data["gender"],
                data["email"]
            )

            self.send_json(result)

        elif self.path == "/api/students/remove":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            result = remove_student(
                data["student_id"]
            )

            self.send_json(result)



        elif self.path == "/api/courses/add":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            result = add_course(
                data["course_name"],
                data["credits"]
            )

            self.send_json(result)


        elif self.path == "/api/enrollments/add":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            result = enroll_student(
                data["student_id"],
                data["course_id"]
            )

            self.send_json(result)

        elif self.path == "/api/enrollments/remove":

            content_length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(content_length)

            data = json.loads(body)

            result = remove_student_from_course(
                data["student_id"],
                data["course_id"]
            )

            self.send_json(result)
        

        else:

            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

    def send_file(self, filename, content_type):

        with open(filename, "rb") as file:
            content = file.read()

        self.send_response(200)

        self.send_header(
            "Content-Type",
            content_type
        )

        self.end_headers()

        self.wfile.write(content)

    def send_json(self, data):

        response = json.dumps(data).encode()

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(response)


server = HTTPServer(
    ("localhost", 8000),
    MyHandler
)

print("Server running at http://localhost:8000")

server.serve_forever()