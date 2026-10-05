from database import get_connection


def get_all_enrollments():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            s.student_id,
            CONCAT(s.fname, ' ', s.lname) AS student_name,
            c.course_id,
            c.course_name,
            e.enrolled_on
        FROM enrollments e
        JOIN students s
            ON e.student_id = s.student_id
        JOIN courses c
            ON e.course_id = c.course_id
        ORDER BY s.student_id
    """

    cursor.execute(query)

    enrollments = cursor.fetchall()


    for enrollment in enrollments:

        enrollment["enrolled_on"] = \
            enrollment["enrolled_on"].strftime(
                "%Y-%m-%d %H:%M:%S"
            )


    cursor.close()
    connection.close()

    return enrollments