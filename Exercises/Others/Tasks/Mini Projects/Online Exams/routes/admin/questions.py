"""Database operations for admin-managed exam questions and MCQ options."""
from database import get_connection


def get_exam_questions(exam_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT exam_id, exam_name, status, total_marks FROM exams WHERE exam_id = %s",
            (exam_id,),
        )
        exam = cursor.fetchone()
        if not exam:
            return None

        cursor.execute(
            "SELECT question_id, exam_id, question_text, marks FROM questions WHERE exam_id = %s ORDER BY question_id",
            (exam_id,),
        )
        questions = cursor.fetchall()
        for question in questions:
            cursor.execute(
                "SELECT option_id, option_text, is_correct FROM options WHERE question_id = %s ORDER BY option_id",
                (question["question_id"],),
            )
            question["options"] = cursor.fetchall()
        return {"exam": exam, "questions": questions}
    finally:
        cursor.close()
        connection.close()


def _validate_question(question_text, marks, options):
    if not isinstance(question_text, str) or not question_text.strip():
        return "Question text is required."
    try:
        marks = int(marks)
    except (ValueError, TypeError):
        return "Marks must be a whole number greater than zero."
    if marks <= 0:
        return "Marks must be a whole number greater than zero."
    if not isinstance(options, list) or not 2 <= len(options) <= 6:
        return "Provide between 2 and 6 answer options."
    if any(not isinstance(o, dict) or not isinstance(o.get("option_text"), str) or not o["option_text"].strip() for o in options):
        return "Every option must have text."
    if sum(1 for o in options if o.get("is_correct") is True or o.get("is_correct") == 1) != 1:
        return "Select exactly one correct option."
    return None


def create_question(exam_id, question_text, marks, options):
    error = _validate_question(question_text, marks, options)
    if error:
        return {"success": False, "message": error}
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT exam_id, status FROM exams WHERE exam_id = %s", (exam_id,))
        exam = cursor.fetchone()
        if not exam:
            return {"success": False, "message": "Exam not found."}
        if exam[1] == "published":
            return {"success": False, "message": "Unpublish the exam before changing its questions."}
        cursor.execute("SELECT COUNT(*) FROM exam_attempts WHERE exam_id = %s", (exam_id,))
        if cursor.fetchone()[0]:
            return {"success": False, "message": "Questions cannot be changed after a student has started this exam."}
        cursor.execute(
            "INSERT INTO questions (exam_id, question_text, marks) VALUES (%s, %s, %s)",
            (exam_id, question_text.strip(), int(marks)),
        )
        question_id = cursor.lastrowid
        for option in options:
            cursor.execute(
                "INSERT INTO options (question_id, option_text, is_correct) VALUES (%s, %s, %s)",
                (question_id, option["option_text"].strip(), int(bool(option.get("is_correct")))),
            )
        connection.commit()
        return {"success": True, "question_id": question_id, "message": "Question created successfully."}
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def update_question(question_id, question_text, marks, options):
    error = _validate_question(question_text, marks, options)
    if error:
        return {"success": False, "message": error}
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT q.question_id, q.exam_id, e.status FROM questions q JOIN exams e ON e.exam_id = q.exam_id WHERE q.question_id = %s",
            (question_id,),
        )
        question = cursor.fetchone()
        if not question:
            return {"success": False, "message": "Question not found."}
        if question["status"] == "published":
            return {"success": False, "message": "Unpublish the exam before changing its questions."}
        cursor.execute("SELECT COUNT(*) AS total FROM exam_attempts WHERE exam_id = %s", (question["exam_id"],))
        if cursor.fetchone()["total"]:
            return {"success": False, "message": "Questions cannot be changed after a student has started this exam."}
        cursor.execute("SELECT COUNT(*) AS total FROM student_answers WHERE question_id = %s", (question_id,))
        if cursor.fetchone()["total"]:
            return {"success": False, "message": "This question has student answer records and cannot be edited."}
        cursor.execute("UPDATE questions SET question_text = %s, marks = %s WHERE question_id = %s", (question_text.strip(), int(marks), question_id))
        cursor.execute("DELETE FROM options WHERE question_id = %s", (question_id,))
        for option in options:
            cursor.execute(
                "INSERT INTO options (question_id, option_text, is_correct) VALUES (%s, %s, %s)",
                (question_id, option["option_text"].strip(), int(bool(option.get("is_correct")))),
            )
        connection.commit()
        return {"success": True, "message": "Question updated successfully."}
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def delete_question(question_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT q.question_id, q.exam_id, e.status FROM questions q JOIN exams e ON e.exam_id = q.exam_id WHERE q.question_id = %s",
            (question_id,),
        )
        question = cursor.fetchone()
        if not question:
            return {"success": False, "message": "Question not found."}
        if question["status"] == "published":
            return {"success": False, "message": "Unpublish the exam before deleting its questions."}
        cursor.execute("SELECT COUNT(*) AS total FROM exam_attempts WHERE exam_id = %s", (question["exam_id"],))
        if cursor.fetchone()["total"]:
            return {"success": False, "message": "Questions cannot be changed after a student has started this exam."}
        # Keep foreign-key integrity: answers may refer to this question, so don't silently delete submitted history.
        cursor.execute("SELECT COUNT(*) AS total FROM student_answers WHERE question_id = %s", (question_id,))
        if cursor.fetchone()["total"]:
            return {"success": False, "message": "This question has student answer records and cannot be deleted."}
        cursor.execute("DELETE FROM questions WHERE question_id = %s", (question_id,))
        connection.commit()
        return {"success": True, "message": "Question deleted successfully."}
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
