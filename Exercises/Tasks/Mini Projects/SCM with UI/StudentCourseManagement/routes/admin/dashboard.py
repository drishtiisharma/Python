from database import get_connection


def get_dashboard_data():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            (SELECT COUNT(*) FROM students) AS total_students,
            (SELECT COUNT(*) FROM courses) AS total_courses,
            (SELECT COUNT(DISTINCT student_id) FROM enrollments) AS total_enrolled_students
    """

    cursor.execute(query)

    dashboard = cursor.fetchone()

    cursor.close()
    connection.close()

    return dashboard