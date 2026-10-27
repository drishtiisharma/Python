from datetime import datetime
from database import get_connection


# -------------------------------------------------
# Student Available Exams Operations
# -------------------------------------------------

def get_available_exams(user_id):
    """
    Fetches all published exams, including scheduled/upcoming exams, so students
    can see them. The API separately marks exams as not_started/expired, and
    start_exam_attempt enforces the actual availability window.
    """
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
                ea.attempt_id,
                ea.status AS attempt_status,
                r.is_published AS result_published,
                CASE
                    WHEN e.start_time IS NOT NULL AND NOW() < e.start_time THEN 'not_started'
                    WHEN e.end_time IS NOT NULL AND NOW() > e.end_time THEN 'expired'
                    ELSE 'available'
                END AS availability_status,
                COUNT(DISTINCT q.question_id) AS total_questions
            FROM exams e
            JOIN subjects s ON e.subject_id = s.subject_id
            LEFT JOIN exam_attempts ea ON e.exam_id = ea.exam_id AND ea.user_id = %s
            LEFT JOIN results r ON r.attempt_id = ea.attempt_id
            LEFT JOIN questions q ON e.exam_id = q.exam_id
            WHERE e.status = 'published' 
            GROUP BY
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
                ea.attempt_id,
                ea.status,
                r.is_published,
                availability_status
            ORDER BY e.exam_id DESC
        """
        cursor.execute(query, (user_id,))
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


# -------------------------------------------------
# Start / Resume Exam Attempt
# -------------------------------------------------

def start_exam_attempt(user_id, exam_id):
    """
    Starts a new attempt or resumes an in-progress attempt for a student.
    Enforces single-attempt rule and validates availability.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # 1. Verify exam exists, is published, and is active
        exam_query = """
            SELECT
                exam_id,
                exam_name,
                status,
                start_time,
                end_time
            FROM exams
            WHERE exam_id = %s
        """
        cursor.execute(exam_query, (exam_id,))
        exam = cursor.fetchone()

        if not exam:
            return {"success": False, "message": "Exam not found.", "status_code": 404}

        if exam["status"] != "published":
            return {"success": False, "message": "This exam is currently not available.", "status_code": 403}

        now = datetime.now()
        if exam["start_time"] and now < exam["start_time"]:
            return {"success": False, "message": "This exam has not started yet.", "status_code": 403}

        if exam["end_time"] and now > exam["end_time"]:
            return {"success": False, "message": "This exam has ended.", "status_code": 403}

        # 2. Check for existing attempt
        cursor.execute(
            "SELECT attempt_id, status FROM exam_attempts WHERE user_id = %s AND exam_id = %s",
            (user_id, exam_id)
        )
        existing = cursor.fetchone()

        if existing:
            if existing["status"] == "submitted":
                return {
                    "success": False,
                    "message": "You have already submitted this exam and cannot attempt it again.",
                    "status_code": 400
                }
            # Resume existing in-progress attempt
            return {
                "success": True,
                "attempt_id": existing["attempt_id"],
                "resumed": True,
                "message": "Resumed in-progress exam attempt."
            }

        # 3. Create new attempt
        insert_cursor = connection.cursor()
        insert_query = """
            INSERT INTO exam_attempts (user_id, exam_id, status, started_at)
            VALUES (%s, %s, 'in_progress', NOW())
        """
        insert_cursor.execute(insert_query, (user_id, exam_id))
        connection.commit()
        attempt_id = insert_cursor.lastrowid
        insert_cursor.close()

        return {
            "success": True,
            "attempt_id": attempt_id,
            "resumed": False,
            "message": "Exam attempt started successfully."
        }

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Get Attempt Quiz Data (Questions & Options)
# -------------------------------------------------

def get_attempt_quiz_data(attempt_id, user_id):
    """
    Returns exam details, duration, remaining seconds, questions,
    and options (WITHOUT exposing is_correct), and student's current answers.
    Enforces student-only access to their own attempt.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # 1. Fetch attempt and exam metadata
        attempt_query = """
            SELECT
                ea.attempt_id,
                ea.user_id,
                ea.exam_id,
                ea.started_at,
                ea.submitted_at,
                ea.status AS attempt_status,
                e.exam_name,
                e.description,
                e.duration_minutes,
                e.total_marks,
                e.passing_marks,
                s.subject_name
            FROM exam_attempts ea
            JOIN exams e ON ea.exam_id = e.exam_id
            JOIN subjects s ON e.subject_id = s.subject_id
            WHERE ea.attempt_id = %s
        """
        cursor.execute(attempt_query, (attempt_id,))
        attempt = cursor.fetchone()

        if not attempt:
            return {"success": False, "message": "Exam attempt not found.", "status_code": 404}

        # Ownership validation
        if attempt["user_id"] != user_id:
            return {"success": False, "message": "Access denied. You can only access your own attempt.", "status_code": 403}

        # Calculate remaining seconds
        now = datetime.now()
        started_at = attempt["started_at"]
        elapsed_seconds = int((now - started_at).total_seconds()) if started_at else 0
        total_seconds = attempt["duration_minutes"] * 60
        remaining_seconds = max(0, total_seconds - elapsed_seconds)

        # 2. Fetch questions for this exam
        cursor.execute(
            "SELECT question_id, question_text, marks FROM questions WHERE exam_id = %s ORDER BY question_id ASC",
            (attempt["exam_id"],)
        )
        questions = cursor.fetchall()

        # 3. Fetch options WITHOUT is_correct (CRITICAL SECURITY)
        question_ids = [q["question_id"] for q in questions]
        options_map = {}
        for qid in question_ids:
            options_map[qid] = []

        if question_ids:
            format_strings = ','.join(['%s'] * len(question_ids))
            options_query = f"""
                SELECT option_id, question_id, option_text
                FROM options
                WHERE question_id IN ({format_strings})
                ORDER BY option_id ASC
            """
            cursor.execute(options_query, tuple(question_ids))
            options = cursor.fetchall()

            for opt in options:
                options_map[opt["question_id"]].append({
                    "option_id": opt["option_id"],
                    "option_text": opt["option_text"]
                })

        for q in questions:
            q["options"] = options_map.get(q["question_id"], [])

        # 4. Fetch student's existing selected answers
        cursor.execute(
            "SELECT question_id, selected_option_id FROM student_answers WHERE attempt_id = %s",
            (attempt_id,)
        )
        saved_answers = cursor.fetchall()
        answers_dict = {a["question_id"]: a["selected_option_id"] for a in saved_answers}

        attempt_info = {
            "attempt_id": attempt["attempt_id"],
            "exam_id": attempt["exam_id"],
            "exam_name": attempt["exam_name"],
            "subject_name": attempt["subject_name"],
            "description": attempt["description"],
            "duration_minutes": attempt["duration_minutes"],
            "total_marks": attempt["total_marks"],
            "passing_marks": attempt["passing_marks"],
            "status": attempt["attempt_status"],
            "started_at": attempt["started_at"].isoformat() if attempt["started_at"] else None,
            "submitted_at": attempt["submitted_at"].isoformat() if attempt["submitted_at"] else None,
            "remaining_seconds": remaining_seconds
        }

        return {
            "success": True,
            "attempt": attempt_info,
            "questions": questions,
            "answers": answers_dict
        }

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Save / Update Single Answer
# -------------------------------------------------

def save_student_answer(attempt_id, user_id, question_id, selected_option_id):
    """
    Saves or updates an individual answer selection in student_answers.
    Validates attempt ownership and in_progress status.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Validate attempt ownership and status
        cursor.execute(
            "SELECT user_id, exam_id, status FROM exam_attempts WHERE attempt_id = %s",
            (attempt_id,)
        )
        attempt = cursor.fetchone()

        if not attempt:
            return {"success": False, "message": "Attempt not found.", "status_code": 404}

        if attempt["user_id"] != user_id:
            return {"success": False, "message": "Access denied.", "status_code": 403}

        if attempt["status"] != "in_progress":
            return {"success": False, "message": "Cannot modify answers for a submitted exam.", "status_code": 400}

        # Verify question belongs to this exam
        cursor.execute(
            "SELECT question_id FROM questions WHERE question_id = %s AND exam_id = %s",
            (question_id, attempt["exam_id"])
        )
        if not cursor.fetchone():
            return {"success": False, "message": "Invalid question for this exam.", "status_code": 400}

        # If option is selected, verify it belongs to this question
        if selected_option_id is not None:
            cursor.execute(
                "SELECT option_id FROM options WHERE option_id = %s AND question_id = %s",
                (selected_option_id, question_id)
            )
            if not cursor.fetchone():
                return {"success": False, "message": "Invalid option for this question.", "status_code": 400}

            # Upsert into student_answers
            write_cursor = connection.cursor()
            upsert_query = """
                INSERT INTO student_answers (attempt_id, question_id, selected_option_id, answered_at)
                VALUES (%s, %s, %s, NOW())
                ON DUPLICATE KEY UPDATE
                    selected_option_id = VALUES(selected_option_id),
                    answered_at = NOW()
            """
            write_cursor.execute(upsert_query, (attempt_id, question_id, selected_option_id))
            connection.commit()
            write_cursor.close()
        else:
            # Clear answer if option is None
            del_cursor = connection.cursor()
            del_cursor.execute(
                "DELETE FROM student_answers WHERE attempt_id = %s AND question_id = %s",
                (attempt_id, question_id)
            )
            connection.commit()
            del_cursor.close()

        return {"success": True, "message": "Answer saved."}

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Submit Quiz & Calculate Results
# -------------------------------------------------

def submit_exam_attempt(attempt_id, user_id, final_answers=None):
    """
    Finalizes the quiz submission:
    1. Validates ownership and prevents multiple submissions.
    2. Persists any final uncommitted answers.
    3. Evaluates answers against options.is_correct.
    4. Marks attempt as 'submitted' with submitted_at timestamp.
    5. Inserts scorecard into the results table.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # 1. Fetch attempt and exam data
        cursor.execute(
            """
            SELECT
                ea.attempt_id,
                ea.user_id,
                ea.exam_id,
                ea.status,
                e.total_marks,
                e.passing_marks
            FROM exam_attempts ea
            JOIN exams e ON ea.exam_id = e.exam_id
            WHERE ea.attempt_id = %s
            """,
            (attempt_id,)
        )
        attempt = cursor.fetchone()

        if not attempt:
            return {"success": False, "message": "Attempt not found.", "status_code": 404}

        if attempt["user_id"] != user_id:
            return {"success": False, "message": "Access denied.", "status_code": 403}

        # Prevent duplicate submissions
        if attempt["status"] == "submitted":
            return {
                "success": False,
                "message": "This exam has already been submitted and cannot be submitted again.",
                "status_code": 400
            }

        # 2. Save final answers only after validating that each question and option
        # belongs to this exam. This prevents forged answer IDs at submission time.
        if final_answers is not None:
            if not isinstance(final_answers, dict):
                return {"success": False, "message": "Invalid answer payload.", "status_code": 400}
            upsert_cursor = connection.cursor()
            try:
                for q_str, opt_id in final_answers.items():
                    try:
                        qid = int(q_str)
                        opt_id = int(opt_id) if opt_id is not None else None
                    except (ValueError, TypeError):
                        connection.rollback()
                        return {"success": False, "message": "Invalid question or option ID.", "status_code": 400}

                    cursor.execute(
                        "SELECT question_id FROM questions WHERE question_id = %s AND exam_id = %s",
                        (qid, attempt["exam_id"])
                    )
                    if not cursor.fetchone():
                        connection.rollback()
                        return {"success": False, "message": "An answer references a question outside this exam.", "status_code": 400}

                    if opt_id is not None:
                        cursor.execute(
                            "SELECT option_id FROM options WHERE option_id = %s AND question_id = %s",
                            (opt_id, qid)
                        )
                        if not cursor.fetchone():
                            connection.rollback()
                            return {"success": False, "message": "An answer option does not belong to its question.", "status_code": 400}

                    upsert_cursor.execute(
                        """
                        INSERT INTO student_answers (attempt_id, question_id, selected_option_id, answered_at)
                        VALUES (%s, %s, %s, NOW())
                        ON DUPLICATE KEY UPDATE
                            selected_option_id = VALUES(selected_option_id),
                            answered_at = NOW()
                        """,
                        (attempt_id, qid, opt_id)
                    )
                connection.commit()
            finally:
                upsert_cursor.close()

        # 3. Grade the attempt
        # Fetch questions & marks
        cursor.execute(
            "SELECT question_id, marks FROM questions WHERE exam_id = %s",
            (attempt["exam_id"],)
        )
        questions = cursor.fetchall()

        # Fetch correct options
        q_ids = [q["question_id"] for q in questions]
        correct_options = {}
        if q_ids:
            format_strings = ','.join(['%s'] * len(q_ids))
            cursor.execute(
                f"SELECT question_id, option_id FROM options WHERE question_id IN ({format_strings}) AND is_correct = 1",
                tuple(q_ids)
            )
            for row in cursor.fetchall():
                correct_options[row["question_id"]] = row["option_id"]

        # Fetch student's selected answers
        cursor.execute(
            "SELECT question_id, selected_option_id FROM student_answers WHERE attempt_id = %s",
            (attempt_id,)
        )
        answers_rows = cursor.fetchall()
        student_answers_map = {r["question_id"]: r["selected_option_id"] for r in answers_rows}

        total_questions = len(questions)
        correct_count = 0
        wrong_count = 0
        unanswered_count = 0
        marks_obtained = 0

        for q in questions:
            qid = q["question_id"]
            q_marks = q["marks"]
            selected_opt = student_answers_map.get(qid)
            correct_opt = correct_options.get(qid)

            if selected_opt is None:
                unanswered_count += 1
            elif selected_opt == correct_opt:
                correct_count += 1
                marks_obtained += q_marks
            else:
                wrong_count += 1

        total_exam_marks = attempt["total_marks"] or 1
        percentage = round((marks_obtained / total_exam_marks) * 100, 2)
        results_status = "pass" if marks_obtained >= attempt["passing_marks"] else "fail"

        # 4. Mark attempt as submitted
        update_cursor = connection.cursor()
        update_cursor.execute(
            "UPDATE exam_attempts SET status = 'submitted', submitted_at = NOW() WHERE attempt_id = %s",
            (attempt_id,)
        )

        # 5. Insert scorecard into results
        results_query = """
            INSERT INTO results (
                attempt_id,
                total_questions,
                correct_answers,
                wrong_answers,
                unanswered,
                marks_obtained,
                percentage,
                results_status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                total_questions = VALUES(total_questions),
                correct_answers = VALUES(correct_answers),
                wrong_answers = VALUES(wrong_answers),
                unanswered = VALUES(unanswered),
                marks_obtained = VALUES(marks_obtained),
                percentage = VALUES(percentage),
                results_status = VALUES(results_status),
                generated_at = NOW()
        """
        update_cursor.execute(
            results_query,
            (
                attempt_id,
                total_questions,
                correct_count,
                wrong_count,
                unanswered_count,
                marks_obtained,
                percentage,
                results_status
            )
        )
        connection.commit()
        update_cursor.close()

        scorecard = {
            "attempt_id": attempt_id,
            "total_questions": total_questions,
            "correct_answers": correct_count,
            "wrong_answers": wrong_count,
            "unanswered": unanswered_count,
            "marks_obtained": marks_obtained,
            "total_marks": total_exam_marks,
            "percentage": percentage,
            "results_status": results_status
        }

        return {
            "success": True,
            "message": "Exam submitted successfully. Your result will be available after the administrator publishes it.",
            "result_pending": True
        }

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Get Attempt Result Scorecard
# -------------------------------------------------

def get_attempt_result(attempt_id, user_id):
    """
    Fetches the result and detailed breakdown for a submitted attempt.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                r.result_id,
                r.attempt_id,
                r.total_questions,
                r.correct_answers,
                r.wrong_answers,
                r.unanswered,
                r.marks_obtained,
                r.percentage,
                r.results_status,
                r.generated_at,
                e.exam_name,
                e.total_marks,
                e.passing_marks,
                s.subject_name,
                ea.started_at,
                ea.submitted_at
            FROM results r
            JOIN exam_attempts ea ON r.attempt_id = ea.attempt_id
            JOIN exams e ON ea.exam_id = e.exam_id
            JOIN subjects s ON e.subject_id = s.subject_id
            WHERE r.attempt_id = %s AND ea.user_id = %s AND r.is_published = TRUE
        """
        cursor.execute(query, (attempt_id, user_id))
        result = cursor.fetchone()

        if not result:
            return {"success": False, "message": "Result not found.", "status_code": 404}

        if result.get("generated_at"):
            result["generated_at"] = result["generated_at"].isoformat()
        if result.get("started_at"):
            result["started_at"] = result["started_at"].isoformat()
        if result.get("submitted_at"):
            result["submitted_at"] = result["submitted_at"].isoformat()

        # Convert decimal fields to float/int
        result["marks_obtained"] = float(result["marks_obtained"])
        result["percentage"] = float(result["percentage"])

        return {"success": True, "result": result}

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Get All Student Results
# -------------------------------------------------

def get_student_all_results(user_id):
    """
    Fetches all completed examination results for the specified student.
    Enforces user_id ownership to ensure students can only view their own results.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        query = """
            SELECT
                r.result_id,
                r.attempt_id,
                r.total_questions,
                r.correct_answers,
                r.wrong_answers,
                r.unanswered,
                r.marks_obtained,
                r.percentage,
                r.results_status,
                r.generated_at,
                e.exam_id,
                e.exam_name,
                e.description,
                e.duration_minutes,
                e.total_marks,
                e.passing_marks,
                s.subject_name,
                ea.started_at,
                ea.submitted_at
            FROM results r
            JOIN exam_attempts ea ON r.attempt_id = ea.attempt_id
            JOIN exams e ON ea.exam_id = e.exam_id
            JOIN subjects s ON e.subject_id = s.subject_id
            WHERE ea.user_id = %s AND r.is_published = TRUE
            ORDER BY r.generated_at DESC, r.result_id DESC
        """
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        for res in results:
            if res.get("generated_at"):
                res["generated_at"] = res["generated_at"].isoformat()
            if res.get("started_at"):
                res["started_at"] = res["started_at"].isoformat()
            if res.get("submitted_at"):
                res["submitted_at"] = res["submitted_at"].isoformat()
            res["marks_obtained"] = float(res["marks_obtained"])
            res["percentage"] = float(res["percentage"])

        return results

    finally:
        cursor.close()
        connection.close()


# -------------------------------------------------
# Get Detailed Attempt Result with Question Breakdown
# -------------------------------------------------

def get_detailed_attempt_result(attempt_id, user_id):
    """
    Fetches comprehensive result details for a student's attempt,
    including the scorecard, performance metrics, and question-by-question review
    showing student's answers, correct answers, and marks earned.
    Strictly enforces user ownership.
    """
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # 1. Fetch scorecard and exam metadata
        scorecard_query = """
            SELECT
                r.result_id,
                r.attempt_id,
                r.total_questions,
                r.correct_answers,
                r.wrong_answers,
                r.unanswered,
                r.marks_obtained,
                r.percentage,
                r.results_status,
                r.generated_at,
                ea.user_id,
                ea.exam_id,
                ea.started_at,
                ea.submitted_at,
                e.exam_name,
                e.description,
                e.duration_minutes,
                e.total_marks,
                e.passing_marks,
                s.subject_name
            FROM results r
            JOIN exam_attempts ea ON r.attempt_id = ea.attempt_id
            JOIN exams e ON ea.exam_id = e.exam_id
            JOIN subjects s ON e.subject_id = s.subject_id
            WHERE r.attempt_id = %s AND r.is_published = TRUE
        """
        cursor.execute(scorecard_query, (attempt_id,))
        scorecard = cursor.fetchone()

        if not scorecard:
            return {"success": False, "message": "Result not found.", "status_code": 404}

        # Ownership validation
        if scorecard["user_id"] != user_id:
            return {"success": False, "message": "Access denied. You can only view your own results.", "status_code": 403}

        # Format timestamps & floats
        if scorecard.get("generated_at"):
            scorecard["generated_at"] = scorecard["generated_at"].isoformat()
        if scorecard.get("started_at"):
            scorecard["started_at"] = scorecard["started_at"].isoformat()
        if scorecard.get("submitted_at"):
            scorecard["submitted_at"] = scorecard["submitted_at"].isoformat()
        scorecard["marks_obtained"] = float(scorecard["marks_obtained"])
        scorecard["percentage"] = float(scorecard["percentage"])

        exam_id = scorecard["exam_id"]

        # 2. Fetch all questions for this exam
        cursor.execute(
            "SELECT question_id, question_text, marks FROM questions WHERE exam_id = %s ORDER BY question_id ASC",
            (exam_id,)
        )
        questions = cursor.fetchall()
        q_ids = [q["question_id"] for q in questions]

        # 3. Fetch options WITH is_correct (allowed for post-submission review)
        options_map = {}
        for qid in q_ids:
            options_map[qid] = []

        if q_ids:
            format_strings = ','.join(['%s'] * len(q_ids))
            cursor.execute(
                f"""
                SELECT option_id, question_id, option_text, is_correct
                FROM options
                WHERE question_id IN ({format_strings})
                ORDER BY option_id ASC
                """,
                tuple(q_ids)
            )
            for opt in cursor.fetchall():
                options_map[opt["question_id"]].append({
                    "option_id": opt["option_id"],
                    "option_text": opt["option_text"],
                    "is_correct": bool(opt["is_correct"])
                })

        # 4. Fetch student's selected answers
        cursor.execute(
            "SELECT question_id, selected_option_id FROM student_answers WHERE attempt_id = %s",
            (attempt_id,)
        )
        saved_answers = {a["question_id"]: a["selected_option_id"] for a in cursor.fetchall()}

        # 5. Assemble question review list
        review_questions = []
        for q in questions:
            qid = q["question_id"]
            q_options = options_map.get(qid, [])
            selected_opt_id = saved_answers.get(qid)

            # Find correct option id
            correct_opt_id = None
            for opt in q_options:
                if opt["is_correct"]:
                    correct_opt_id = opt["option_id"]
                    break

            if selected_opt_id is None:
                q_status = "unanswered"
                marks_awarded = 0
            elif selected_opt_id == correct_opt_id:
                q_status = "correct"
                marks_awarded = q["marks"]
            else:
                q_status = "wrong"
                marks_awarded = 0

            review_questions.append({
                "question_id": qid,
                "question_text": q["question_text"],
                "marks": q["marks"],
                "options": q_options,
                "selected_option_id": selected_opt_id,
                "correct_option_id": correct_opt_id,
                "status": q_status,
                "marks_awarded": marks_awarded
            })

        return {
            "success": True,
            "result": scorecard,
            "questions": review_questions
        }

    finally:
        cursor.close()
        connection.close()

