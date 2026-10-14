from database import get_connection
from utils.sessions import get_session
from utils.responses import send_json


def get_admin_results_api(handler):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return
    if session.get("role") != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                r.result_id, r.attempt_id, r.total_questions,
                r.correct_answers, r.wrong_answers, r.unanswered,
                r.marks_obtained, r.percentage, r.results_status,
                r.generated_at, r.is_published,
                ea.status AS attempt_status, ea.submitted_at,
                u.user_id, u.fname, u.lname, u.email,
                e.exam_id, e.exam_name, e.total_marks,
                s.subject_name
            FROM results r
            JOIN exam_attempts ea ON ea.attempt_id = r.attempt_id
            JOIN users u ON u.user_id = ea.user_id
            JOIN exams e ON e.exam_id = ea.exam_id
            JOIN subjects s ON s.subject_id = e.subject_id
            ORDER BY r.generated_at DESC, r.result_id DESC
        """)
        rows = cursor.fetchall()
        for row in rows:
            for key in ("generated_at", "submitted_at"):
                if row.get(key):
                    row[key] = row[key].isoformat()
            row["marks_obtained"] = float(row["marks_obtained"])
            row["percentage"] = float(row["percentage"])
            row["is_published"] = bool(row["is_published"])
        send_json(handler, {"success": True, "results": rows})
    except Exception as exc:
        print("Error loading admin results:", exc)
        send_json(handler, {"success": False, "message": "Unable to load results"}, 500)
    finally:
        cursor.close()
        connection.close()


def toggle_result_publication_api(handler, path):
    session = get_session(handler)
    if not session:
        send_json(handler, {"success": False, "message": "Not logged in"}, 401)
        return
    if session.get("role") != "admin":
        send_json(handler, {"success": False, "message": "Access denied"}, 403)
        return

    try:
        parts = [part for part in path.split("/") if part]
        attempt_id = int(parts[-2])
    except (ValueError, IndexError):
        send_json(handler, {"success": False, "message": "Invalid attempt ID"}, 400)
        return

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT is_published FROM results WHERE attempt_id = %s",
            (attempt_id,)
        )
        row = cursor.fetchone()
        if not row:
            send_json(handler, {"success": False, "message": "Result not found"}, 404)
            return
        new_value = not bool(row["is_published"])
        cursor.execute(
            "UPDATE results SET is_published = %s WHERE attempt_id = %s",
            (new_value, attempt_id)
        )
        connection.commit()
        send_json(handler, {
            "success": True,
            "is_published": new_value,
            "message": "Result published to the student." if new_value else "Result unpublished."
        })
    except Exception as exc:
        connection.rollback()
        print("Error changing result publication:", exc)
        send_json(handler, {"success": False, "message": "Unable to update result publication"}, 500)
    finally:
        cursor.close()
        connection.close()
