from utils.responses import send_json, get_json_body
from utils.sessions import get_session

from routes.admin.students import (
    get_all_students,
    add_student,
    update_student,
    delete_student
)


from routes.admin.admins import (
    get_all_admins,
    update_admin,
    delete_admin
)

from routes.admin.exams import (
    get_all_subjects,
    add_subject,
    get_all_exams,
    get_exam_by_id,
    create_exam,
    update_exam,
    delete_exam,
    toggle_exam_status
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


# -------------------------------------------------
# Get all other admins
# -------------------------------------------------

def get_admins_api(handler):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {"success": False, "message": "Not logged in"},
            401
        )
        return

    if session["role"] != "admin":

        send_json(
            handler,
            {"success": False, "message": "Access denied"},
            403
        )
        return

    try:

        current_user_id = session["user_id"]

        admins = get_all_admins(current_user_id)

        for admin in admins:

            if admin["created_at"]:
                admin["created_at"] = (
                    admin["created_at"].isoformat()
                )

        send_json(
            handler,
            {
                "success": True,
                "admins": admins
            }
        )

    except Exception as e:

        print("Error loading admins:", e)

        send_json(
            handler,
            {
                "success": False,
                "message": "Unable to load admins"
            },
            500
        )


# -------------------------------------------------
# Update Admin
# -------------------------------------------------

def update_admin_api(handler, path):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {"success": False, "message": "Not logged in"},
            401
        )
        return

    if session["role"] != "admin":

        send_json(
            handler,
            {"success": False, "message": "Access denied"},
            403
        )
        return

    try:

        user_id = int(path.split("/")[-1])

    except ValueError:

        send_json(
            handler,
            {"success": False, "message": "Invalid admin ID"},
            400
        )
        return

    data = get_json_body(handler)

    if not data:

        send_json(
            handler,
            {"success": False, "message": "Invalid request body"},
            400
        )
        return

    fname = data.get("fname")
    lname = data.get("lname")

    if (
        not isinstance(fname, str)
        or not isinstance(lname, str)
        or not fname.strip()
        or not lname.strip()
    ):

        send_json(
            handler,
            {"success": False, "message": "First and last names are required"},
            400
        )
        return

    try:

        result = update_admin(
            user_id,
            fname.strip(),
            lname.strip(),
            session["user_id"]
        )

        if not result["success"]:

            send_json(handler, result, 400)
            return

        send_json(handler, result)

    except Exception as e:

        print("Error updating admin:", e)

        send_json(
            handler,
            {"success": False, "message": "Unable to update admin"},
            500
        )


# -------------------------------------------------
# Delete Admin
# -------------------------------------------------

def delete_admin_api(handler, path):

    session = get_session(handler)

    if not session:

        send_json(
            handler,
            {"success": False, "message": "Not logged in"},
            401
        )
        return

    if session["role"] != "admin":

        send_json(
            handler,
            {"success": False, "message": "Access denied"},
            403
        )
        return

    try:

        user_id = int(path.split("/")[-1])

    except ValueError:

        send_json(
            handler,
            {"success": False, "message": "Invalid admin ID"},
            400
        )
        return

    try:

        result = delete_admin(
            user_id,
            session["user_id"]
        )

        if not result["success"]:

            send_json(handler, result, 400)
            return

        send_json(handler, result)

    except Exception as e:

        print("Error deleting admin:", e)

        send_json(
            handler,
            {"success": False, "message": "Unable to delete admin"},
            500
        )


# =================================================
# Subjects APIs
# =================================================

def get_subjects_api(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        subjects = get_all_subjects()
        send_json(handler, {"success": True, "subjects": subjects})
    except Exception as e:
        print("Error getting subjects:", e)
        send_json(handler, {"success": False, "message": "Unable to load subjects"}, 500)


def add_subject_api(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    data = get_json_body(handler)
    if not data:
        send_json(handler, {"success": False, "message": "Invalid request body"}, 400)
        return

    subject_name = data.get("subject_name")
    description = data.get("description", "")

    if not isinstance(subject_name, str) or not subject_name.strip():
        send_json(handler, {"success": False, "message": "Subject name is required"}, 400)
        return

    try:
        result = add_subject(subject_name.strip(), description.strip() if isinstance(description, str) else "")
        status_code = 201 if result["success"] else 400
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error adding subject:", e)
        send_json(handler, {"success": False, "message": "Unable to create subject"}, 500)


# =================================================
# Exams APIs
# =================================================

def get_exams_api(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        exams = get_all_exams()
        send_json(handler, {"success": True, "exams": exams})
    except Exception as e:
        print("Error getting exams:", e)
        send_json(handler, {"success": False, "message": "Unable to load exams"}, 500)


def get_exam_by_id_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        exam_id = int(path.split("/")[-1])
    except ValueError:
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
        return

    try:
        exam = get_exam_by_id(exam_id)
        if not exam:
            send_json(handler, {"success": False, "message": "Exam not found"}, 404)
            return

        send_json(handler, {"success": True, "exam": exam})
    except Exception as e:
        print("Error getting exam details:", e)
        send_json(handler, {"success": False, "message": "Unable to load exam details"}, 500)


def add_exam_api(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    data = get_json_body(handler)
    if not data:
        send_json(handler, {"success": False, "message": "Invalid request body"}, 400)
        return

    exam_name = data.get("exam_name")
    subject_id = data.get("subject_id")
    description = data.get("description", "")
    duration_minutes = data.get("duration_minutes")
    total_marks = data.get("total_marks")
    passing_marks = data.get("passing_marks")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    status = data.get("status", "draft")

    if not isinstance(exam_name, str) or not exam_name.strip():
        send_json(handler, {"success": False, "message": "Exam name is required"}, 400)
        return

    try:
        subject_id = int(subject_id)
        duration_minutes = int(duration_minutes)
        total_marks = int(total_marks)
        passing_marks = int(passing_marks)
    except (ValueError, TypeError):
        send_json(handler, {"success": False, "message": "Subject, duration, and marks must be valid numbers"}, 400)
        return

    if duration_minutes <= 0:
        send_json(handler, {"success": False, "message": "Duration must be greater than 0 minutes"}, 400)
        return

    if total_marks <= 0:
        send_json(handler, {"success": False, "message": "Total marks must be greater than 0"}, 400)
        return

    if passing_marks < 0 or passing_marks > total_marks:
        send_json(handler, {"success": False, "message": "Passing marks must be between 0 and total marks"}, 400)
        return

    try:
        result = create_exam(
            subject_id=subject_id,
            exam_name=exam_name.strip(),
            description=description.strip() if isinstance(description, str) else "",
            duration_minutes=duration_minutes,
            total_marks=total_marks,
            passing_marks=passing_marks,
            start_time=start_time,
            end_time=end_time,
            status=status,
            created_by=session["user_id"]
        )
        status_code = 201 if result["success"] else 400
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error creating exam:", e)
        send_json(handler, {"success": False, "message": "Unable to create exam"}, 500)


def update_exam_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        exam_id = int(path.split("/")[-1])
    except ValueError:
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
        return

    data = get_json_body(handler)
    if not data:
        send_json(handler, {"success": False, "message": "Invalid request body"}, 400)
        return

    exam_name = data.get("exam_name")
    subject_id = data.get("subject_id")
    description = data.get("description", "")
    duration_minutes = data.get("duration_minutes")
    total_marks = data.get("total_marks")
    passing_marks = data.get("passing_marks")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    status = data.get("status", "draft")

    if not isinstance(exam_name, str) or not exam_name.strip():
        send_json(handler, {"success": False, "message": "Exam name is required"}, 400)
        return

    try:
        subject_id = int(subject_id)
        duration_minutes = int(duration_minutes)
        total_marks = int(total_marks)
        passing_marks = int(passing_marks)
    except (ValueError, TypeError):
        send_json(handler, {"success": False, "message": "Subject, duration, and marks must be valid numbers"}, 400)
        return

    if duration_minutes <= 0:
        send_json(handler, {"success": False, "message": "Duration must be greater than 0 minutes"}, 400)
        return

    if total_marks <= 0:
        send_json(handler, {"success": False, "message": "Total marks must be greater than 0"}, 400)
        return

    if passing_marks < 0 or passing_marks > total_marks:
        send_json(handler, {"success": False, "message": "Passing marks must be between 0 and total marks"}, 400)
        return

    try:
        result = update_exam(
            exam_id=exam_id,
            subject_id=subject_id,
            exam_name=exam_name.strip(),
            description=description.strip() if isinstance(description, str) else "",
            duration_minutes=duration_minutes,
            total_marks=total_marks,
            passing_marks=passing_marks,
            start_time=start_time,
            end_time=end_time,
            status=status
        )
        status_code = 200 if result["success"] else 400
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error updating exam:", e)
        send_json(handler, {"success": False, "message": "Unable to update exam"}, 500)


def delete_exam_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        exam_id = int(path.split("/")[-1])
    except ValueError:
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
        return

    try:
        result = delete_exam(exam_id)
        if result.get("code") == "EXAM_HAS_ATTEMPTS":
            status_code = 409
        else:
            status_code = 200 if result["success"] else 400
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error deleting exam:", e)
        send_json(handler, {"success": False, "message": "Unable to delete exam"}, 500)


def toggle_exam_status_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return

    if session["role"] != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        # Expected path: /api/admin/exams/<id>/status
        parts = [p for p in path.split("/") if p]
        exam_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
        return

    try:
        result = toggle_exam_status(exam_id)
        status_code = 200 if result["success"] else 400
        send_json(handler, result, status_code)
    except Exception as e:
        print("Error toggling exam status:", e)
        send_json(handler, {"success": False, "message": "Unable to change exam status"}, 500)
