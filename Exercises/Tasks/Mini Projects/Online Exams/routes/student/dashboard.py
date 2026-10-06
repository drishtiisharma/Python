from database import get_connection


def get_student_details(user_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                user_id,
                fname,
                lname,
                email,
                role,
                created_at
            FROM users
            WHERE user_id = %s
              AND role = 'student'
        """

        cursor.execute(query, (user_id,))

        student = cursor.fetchone()

        return student

    finally:

        cursor.close()
        connection.close()