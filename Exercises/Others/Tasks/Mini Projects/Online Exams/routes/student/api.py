
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

from routes.student.exams import (
    get_available_exams,
    start_exam_attempt,
    get_attempt_quiz_data,
    save_student_answer,
    submit_exam_attempt,
    get_attempt_result,
    get_student_all_results,
    get_detailed_attempt_result
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


# -------------------------------------------------
# Quiz Attempt & Submission APIs
# -------------------------------------------------

def start_exam_attempt_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected: /api/student/exams/<exam_id>/start
        parts = [p for p in path.split("/") if p]
        exam_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
        return

    try:
        result = start_exam_attempt(session["user_id"], exam_id)
        status_code = 200 if result["success"] else result.get("status_code", 400)
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error starting exam attempt:", e)
        send_json(handler, {"success": False, "message": "Unable to start exam attempt"}, 500)


def get_attempt_quiz_data_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected: /api/student/attempts/<attempt_id>
        parts = [p for p in path.split("/") if p]
        attempt_id = int(parts[-1])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    try:
        result = get_attempt_quiz_data(attempt_id, session["user_id"])
        status_code = 200 if result["success"] else result.get("status_code", 400)
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error getting quiz questions:", e)
        send_json(handler, {"success": False, "message": "Unable to load quiz"}, 500)


def save_student_answer_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected: /api/student/attempts/<attempt_id>/answer
        parts = [p for p in path.split("/") if p]
        attempt_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    data = get_json_body(handler)
    if not data or "question_id" not in data:
        send_json(handler, {"success": False, "message": "question_id is required"}, 400)
        return

    try:
        question_id = int(data["question_id"])
        selected_option_id = int(data["selected_option_id"]) if data.get("selected_option_id") is not None else None
    except (ValueError, TypeError):
        send_json(handler, {"success": False, "message": "Invalid question or option ID"}, 400)
        return

    try:
        result = save_student_answer(attempt_id, session["user_id"], question_id, selected_option_id)
        status_code = 200 if result["success"] else result.get("status_code", 400)
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error saving answer:", e)
        send_json(handler, {"success": False, "message": "Unable to save answer"}, 500)


def submit_exam_attempt_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected: /api/student/attempts/<attempt_id>/submit
        parts = [p for p in path.split("/") if p]
        attempt_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    data = get_json_body(handler) if handler.headers.get("Content-Length") else {}
    answers = data.get("answers") if isinstance(data, dict) else None

    try:
        result = submit_exam_attempt(attempt_id, session["user_id"], answers)
        status_code = 200 if result["success"] else result.get("status_code", 400)
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error submitting exam:", e)
        send_json(handler, {"success": False, "message": "Unable to submit exam"}, 500)


def get_attempt_result_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected: /api/student/attempts/<attempt_id>/result
        parts = [p for p in path.split("/") if p]
        attempt_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    try:
        result = get_attempt_result(attempt_id, session["user_id"])
        status_code = 200 if result["success"] else result.get("status_code", 400)
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error getting result:", e)
        send_json(handler, {"success": False, "message": "Unable to load result"}, 500)


def get_student_results_api(handler):
    """
    Returns all submitted exam results for the authenticated student.
    Guarantees students only receive their own results.
    """
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        results = get_student_all_results(session["user_id"])
        send_json(handler, {"success": True, "results": results})
    except Exception as e:
        print("Error fetching student results:", e)
        send_json(handler, {"success": False, "message": "Unable to load results"}, 500)


def get_detailed_result_api(handler, path):
    """
    Returns full scorecard and question-by-question review for an attempt.
    Guarantees students only receive their own attempt review.
    Path format: /api/student/results/<attempt_id>
    """
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "student":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        parts = [p for p in path.split("/") if p]
        attempt_id = int(parts[-1])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    try:
        result_data = get_detailed_attempt_result(attempt_id, session["user_id"])
        status_code = 200 if result_data["success"] else result_data.get("status_code", 400)
        send_json(handler, result_data, status_code)
    except Exception as e:
        print("Error fetching detailed result:", e)
        send_json(handler, {"success": False, "message": "Unable to load result details"}, 500)



# -------------------------------------------------
# Student Available Exams API
# -------------------------------------------------

def get_available_exams_api(handler):

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

    try:

        exams = get_available_exams(session["user_id"])

        send_json(
            handler,
            {
                "success": True,
                "exams": exams
            }
        )

    except Exception as e:

        print("Error fetching available exams:", e)

        send_json(
            handler,
            {
                "success": False,
                "message": "Unable to load available exams"
            },
            500
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