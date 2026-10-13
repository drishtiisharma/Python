from database import get_connection


# -------------------------------------------------
# Subjects Operations
# -------------------------------------------------

def get_all_subjects():
    """Fetches all subjects from the database."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                subject_id,
                subject_name,
                description
            FROM subjects
            ORDER BY subject_name ASC
        """
        cursor.execute(query)
        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def add_subject(subject_name, description=""):
    """Adds a new subject if it does not already exist."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        check_query = """
            SELECT subject_id
            FROM subjects
            WHERE subject_name = %s
        """
        cursor.execute(check_query, (subject_name,))
        if cursor.fetchone():
            return {
                "success": False,
                "message": "A subject with this name already exists."
            }

        insert_query = """
            INSERT INTO subjects (subject_name, description)
            VALUES (%s, %s)
        """
        cursor.execute(insert_query, (subject_name, description or ""))
        connection.commit()

        return {
            "success": True,
            "subject_id": cursor.lastrowid,
            "message": "Subject created successfully."
        }

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Helper: Format Datetime for MySQL
# -------------------------------------------------

def _clean_datetime(dt_str):
    if not dt_str:
        return None
    dt_str = str(dt_str).strip()
    if not dt_str:
        return None
    # Convert '2026-10-15T14:30' to '2026-10-15 14:30:00'
    cleaned = dt_str.replace("T", " ")
    if len(cleaned) == 16:
        cleaned += ":00"
    return cleaned


# -------------------------------------------------
# Exams Operations
# -------------------------------------------------

def get_all_exams():
    """Fetches all exams with subject name, creator name, and question count."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                e.exam_id,
                e.subject_id,
                s.subject_name,
                e.exam_name,
                e.description,
                e.duration_minutes,
                e.total_marks,
                e.passing_marks,
                e.start_time,
                e.end_time,
                e.status,
                e.created_by,
                CONCAT(u.fname, ' ', u.lname) AS created_by_name,
                COUNT(q.question_id) AS total_questions
            FROM exams e
            JOIN subjects s ON e.subject_id = s.subject_id
            JOIN users u ON e.created_by = u.user_id
            LEFT JOIN questions q ON e.exam_id = q.exam_id
            GROUP BY e.exam_id
            ORDER BY e.exam_id DESC
        """
        cursor.execute(query)
        exams = cursor.fetchall()

        for exam in exams:
            if exam.get("start_time"):
                exam["start_time"] = exam["start_time"].isoformat()
            if exam.get("end_time"):
                exam["end_time"] = exam["end_time"].isoformat()

        return exams

    finally:
        cursor.close()
        connection.close()


def get_exam_by_id(exam_id):
    """Fetches single exam details by exam_id."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                e.exam_id,
                e.subject_id,
                s.subject_name,
                e.exam_name,
                e.description,
                e.duration_minutes,
                e.total_marks,
                e.passing_marks,
                e.start_time,
                e.end_time,
                e.status,
                e.created_by,
                CONCAT(u.fname, ' ', u.lname) AS created_by_name
            FROM exams e
            JOIN subjects s ON e.subject_id = s.subject_id
            JOIN users u ON e.created_by = u.user_id
            WHERE e.exam_id = %s
        """
        cursor.execute(query, (exam_id,))
        exam = cursor.fetchone()

        if exam:
            if exam.get("start_time"):
                exam["start_time"] = exam["start_time"].isoformat()
            if exam.get("end_time"):
                exam["end_time"] = exam["end_time"].isoformat()

        return exam

    finally:
        cursor.close()
        connection.close()


def create_exam(
    subject_id,
    exam_name,
    description,
    duration_minutes,
    total_marks,
    passing_marks,
    start_time,
    end_time,
    status,
    created_by
):
    """Creates a new test/exam in the exams table."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Verify subject exists
        cursor.execute(
            "SELECT subject_id FROM subjects WHERE subject_id = %s",
            (subject_id,)
        )
        if not cursor.fetchone():
            return {
                "success": False,
                "message": "Selected subject does not exist."
            }

        start_dt = _clean_datetime(start_time)
        end_dt = _clean_datetime(end_time)

        if status not in ["draft", "published"]:
            status = "draft"

        query = """
            INSERT INTO exams (
                subject_id,
                exam_name,
                description,
                duration_minutes,
                total_marks,
                passing_marks,
                start_time,
                end_time,
                status,
                created_by
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                subject_id,
                exam_name,
                description or "",
                duration_minutes,
                total_marks,
                passing_marks,
                start_dt,
                end_dt,
                status,
                created_by
            )
        )
        connection.commit()

        return {
            "success": True,
            "exam_id": cursor.lastrowid,
            "message": "Exam created successfully."
        }

    finally:
        cursor.close()
        connection.close()


def update_exam(
    exam_id,
    subject_id,
    exam_name,
    description,
    duration_minutes,
    total_marks,
    passing_marks,
    start_time,
    end_time,
    status
):
    """Updates an existing exam."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Verify exam exists
        cursor.execute(
            "SELECT exam_id FROM exams WHERE exam_id = %s",
            (exam_id,)
        )
        if not cursor.fetchone():
            return {
                "success": False,
                "message": "Exam not found."
            }

        start_dt = _clean_datetime(start_time)
        end_dt = _clean_datetime(end_time)

        if status not in ["draft", "published"]:
            status = "draft"

        query = """
            UPDATE exams
            SET
                subject_id = %s,
                exam_name = %s,
                description = %s,
                duration_minutes = %s,
                total_marks = %s,
                passing_marks = %s,
                start_time = %s,
                end_time = %s,
                status = %s
            WHERE exam_id = %s
        """
        cursor.execute(
            query,
            (
                subject_id,
                exam_name,
                description or "",
                duration_minutes,
                total_marks,
                passing_marks,
                start_dt,
                end_dt,
                status,
                exam_id
            )
        )
        connection.commit()

        return {
            "success": True,
            "message": "Exam updated successfully."
        }

    finally:
        cursor.close()
        connection.close()


def delete_exam(exam_id):
    """Deletes an exam and cascades related questions/attempts."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = "DELETE FROM exams WHERE exam_id = %s"
        cursor.execute(query, (exam_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return {
                "success": True,
                "message": "Exam deleted successfully."
            }

        return {
            "success": False,
            "message": "Exam not found."
        }

    finally:
        cursor.close()
        connection.close()


def toggle_exam_status(exam_id):
    """Toggles status between 'draft' and 'published'."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT status FROM exams WHERE exam_id = %s", (exam_id,))
        exam = cursor.fetchone()

        if not exam:
            return {
                "success": False,
                "message": "Exam not found."
            }

        new_status = "published" if exam["status"] == "draft" else "draft"

        update_cursor = connection.cursor()
        update_cursor.execute(
            "UPDATE exams SET status = %s WHERE exam_id = %s",
            (new_status, exam_id)
        )
        connection.commit()
        update_cursor.close()

        return {
            "success": True,
            "status": new_status,
            "message": f"Exam status changed to {new_status}."
        }

    finally:
        cursor.close()
        connection.close()
