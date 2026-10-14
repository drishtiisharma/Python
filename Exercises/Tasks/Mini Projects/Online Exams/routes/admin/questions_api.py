"""HTTP API handlers for admin question and MCQ option CRUD."""
from utils.sessions import get_session
from utils.responses import send_json, get_json_body
from routes.admin.questions import get_exam_questions, create_question, update_question, delete_question


def _admin_session(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return None
    if session.get("role") != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return None
    return session


def get_questions_api(handler, path):
    if not _admin_session(handler):
        return
    try:
        parts = [p for p in path.split("/") if p]
        exam_id = int(parts[3])
        data = get_exam_questions(exam_id)
        if data is None:
            send_json(handler, {"success": False, "message": "Exam not found"}, 404)
            return
        send_json(handler, {"success": True, **data})
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid exam ID"}, 400)
    except Exception as exc:
        print("Error loading exam questions:", exc)
        send_json(handler, {"success": False, "message": "Unable to load questions"}, 500)


def add_question_api(handler, path):
    session = _admin_session(handler)
    if not session:
        return
    try:
        parts = [p for p in path.split("/") if p]
        exam_id = int(parts[3])
        data = get_json_body(handler)
        result = create_question(exam_id, data.get("question_text"), data.get("marks", 1), data.get("options"))
        send_json(handler, result, 201 if result.get("success") else 400)
    except (ValueError, TypeError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid exam ID or request body"}, 400)
    except Exception as exc:
        print("Error creating question:", exc)
        send_json(handler, {"success": False, "message": "Unable to create question"}, 500)


def update_question_api(handler, path):
    if not _admin_session(handler):
        return
    try:
        question_id = int([p for p in path.split("/") if p][-1])
        data = get_json_body(handler)
        result = update_question(question_id, data.get("question_text"), data.get("marks", 1), data.get("options"))
        send_json(handler, result, 200 if result.get("success") else 400)
    except (ValueError, TypeError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid question ID or request body"}, 400)
    except Exception as exc:
        print("Error updating question:", exc)
        send_json(handler, {"success": False, "message": "Unable to update question"}, 500)


def delete_question_api(handler, path):
    if not _admin_session(handler):
        return
    try:
        question_id = int([p for p in path.split("/") if p][-1])
        result = delete_question(question_id)
        send_json(handler, result, 200 if result.get("success") else 400)
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid question ID"}, 400)
    except Exception as exc:
        print("Error deleting question:", exc)
        send_json(handler, {"success": False, "message": "Unable to delete question"}, 500)
