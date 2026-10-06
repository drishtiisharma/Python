from database import get_connection


# -------------------------------------------------
# Get all students
# -------------------------------------------------

def get_all_students():

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
            WHERE role = 'student'
            ORDER BY user_id
        """

        cursor.execute(query)

        students = cursor.fetchall()

        return students

    finally:

        cursor.close()
        connection.close()