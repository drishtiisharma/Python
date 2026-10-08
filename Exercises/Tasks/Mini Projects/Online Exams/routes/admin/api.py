from utils.responses import send_json, get_json_body
from utils.sessions import get_session

from routes.admin.students import (
    get_all_students,
    add_student,
    update_student,
    delete_student
)


def get_students_api(handler):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {
                "success": False,
                "message": "Not logged in"
            },
            401
        )

        return

    if session["role"] != "admin":

        send_json(
            handler,
            {
                "success": False,
                "message": "Access denied"
            },
            403
        )

        return

    try:

        students = get_all_students()

        for student in students:

            if student["created_at"]:

                student["created_at"] = (
                    student["created_at"].isoformat()
                )

        send_json(
            handler,
            {
                "success": True,
                "students": students
            }
        )

    except Exception as e:

        print("Error loading students:", e)

        send_json(
            handler,
            {
                "success": False,
                "message": "Unable to load students"
            },
            500
        )


def add_student_api(handler):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {
                "success": False,
                "message": "Not logged in"
            },
            401
        )

        return

    if session["role"] != "admin":

        send_json(
            handler,
            {
                "success": False,
                "message": "Access denied"
            },
            403
        )

        return

    data = get_json_body(handler)

    if not data:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid request body"
            },
            400
        )

        return

    fname = data.get("fname")
    lname = data.get("lname")
    email = data.get("email")
    role = data.get("role")

    if not fname or not lname or not email or not role:

        send_json(
            handler,
            {
                "success": False,
                "message": "All fields are required"
            },
            400
        )

        return

    if role not in ["student", "admin"]:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid role"
            },
            400
        )

        return

    result = add_student(
        fname,
        lname,
        email,
        role
    )

    if not result["success"]:

        send_json(
            handler,
            result,
            400
        )

        return

    send_json(
        handler,
        result,
        201
    )


def update_student_api(handler, path):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {
                "success": False,
                "message": "Not logged in"
            },
            401
        )

        return

    if session["role"] != "admin":

        send_json(
            handler,
            {
                "success": False,
                "message": "Access denied"
            },
            403
        )

        return

    try:

        user_id = int(
            path.split("/")[-1]
        )

    except ValueError:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid student ID"
            },
            400
        )

        return

    data = get_json_body(handler)

    if not data:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid request body"
            },
            400
        )

        return

    fname = data.get("fname")
    lname = data.get("lname")
    role = data.get("role")

    if not fname or not lname or not role:

        send_json(
            handler,
            {
                "success": False,
                "message": "All fields are required"
            },
            400
        )

        return

    if role not in ["student", "admin"]:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid role"
            },
            400
        )

        return

    result = update_student(
        user_id,
        fname,
        lname,
        role
    )

    if not result["success"]:

        send_json(
            handler,
            result,
            400
        )

        return

    send_json(
        handler,
        result
    )


def delete_student_api(handler, path):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {
                "success": False,
                "message": "Not logged in"
            },
            401
        )

        return

    if session["role"] != "admin":

        send_json(
            handler,
            {
                "success": False,
                "message": "Access denied"
            },
            403
        )

        return

    try:

        user_id = int(
            path.split("/")[-1]
        )

    except ValueError:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid student ID"
            },
            400
        )

        return

    result = delete_student(user_id)

    if not result["success"]:

        send_json(
            handler,
            result,
            400
        )

        return

    send_json(
        handler,
        result
    )
