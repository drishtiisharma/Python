
from utils.sessions import get_session

from utils.responses import (
    send_json,
    get_json_body
)

from routes.student.dashboard import (
    get_student_details,
    update_student_profile,
    change_student_password
)

def student_details_api(handler):

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

    if session["role"] != "student":

        send_json(
            handler,
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

        send_json(
            handler,
            {
                "success": False,
                "message": "Student not found"
            },
            404
        )

        return

    if student["created_at"]:

        student["created_at"] = student["created_at"].isoformat()

    send_json(
        handler,
        {
            "success": True,
            "student": student
        }
    )


def update_student_profile_api(handler):

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


    if session["role"] != "student":

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


    if not fname or not lname:

        send_json(
            handler,
            {
                "success": False,
                "message": "All fields are required"
            },
            400
        )

        return


    result = update_student_profile(
        session["user_id"],
        fname,
        lname
    )


    if not result["success"]:

        send_json(
            handler,
            result,
            400
        )

        return


    session["fname"] = fname
    session["lname"] = lname

    send_json(
        handler,
        result
    )


def change_student_password_api(handler):

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


    if session["role"] != "student":

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


    old_password = data.get("old_password")

    new_password = data.get("new_password")


    if not old_password or not new_password:

        send_json(
            handler,
            {
                "success": False,
                "message": "All fields are required"
            },
            400
        )

        return


    result = change_student_password(
        session["user_id"],
        old_password,
        new_password
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