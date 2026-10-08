from routes.student.dashboard import get_student_details

from utils.responses import send_json
from utils.sessions import get_session


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
