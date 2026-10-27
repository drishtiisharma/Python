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


# -------------------------------------------------
# Edit Student Details
# -------------------------------------------------

def update_student(
    user_id,
    fname,
    lname,
    role
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            UPDATE users
            SET
                fname = %s,
                lname = %s,
                role = %s
            WHERE user_id = %s
            AND role = 'student'
        """

        cursor.execute(
            query,
            (
                fname,
                lname,
                role,
                user_id
            )
        )

        connection.commit()


        if cursor.rowcount > 0:

            return {
                "success": True
            }


        return {
            "success": False,
            "message": "Student not found"
        }


    finally:

        cursor.close()
        connection.close()



# -------------------------------------------------
# Add Student
# -------------------------------------------------

def add_student(
    fname,
    lname,
    email,
    role
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # Check if email already exists

        query = """
            SELECT user_id
            FROM users
            WHERE email = %s
        """

        cursor.execute(
            query,
            (email,)
        )

        existing_user = cursor.fetchone()


        if existing_user:

            return {
                "success": False,
                "message": "Email already exists"
            }


        # Default password is first name

        password = fname


        # Insert user

        query = """
            INSERT INTO users
            (
                fname,
                lname,
                email,
                password_hash,
                role
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        cursor.execute(
            query,
            (
                fname,
                lname,
                email,
                password,
                role
            )
        )

        connection.commit()


        return {
            "success": True
        }


    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Delete Student Record
# -------------------------------------------------

def delete_student(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            DELETE FROM users
            WHERE user_id = %s
            AND role = 'student'
        """

        cursor.execute(
            query,
            (user_id,)
        )

        connection.commit()


        if cursor.rowcount > 0:

            return {
                "success": True
            }


        return {
            "success": False,
            "message": "Student not found"
        }


    finally:

        cursor.close()
        connection.close()
