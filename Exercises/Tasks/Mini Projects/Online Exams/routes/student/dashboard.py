from database import get_connection


# -------------------------------------------------
# Get student details
# -------------------------------------------------

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

        cursor.execute(
            query,
            (user_id,)
        )

        student = cursor.fetchone()

        return student

    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Update student profile
# -------------------------------------------------

def update_student_profile(
    user_id,
    fname,
    lname
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            UPDATE users
            SET
                fname = %s,
                lname = %s
            WHERE user_id = %s
              AND role = 'student'
        """

        cursor.execute(
            query,
            (
                fname,
                lname,
                user_id
            )
        )

        connection.commit()


        if cursor.rowcount == 0:

            return {
                "success": False,
                "message": "Student not found"
            }


        return {
            "success": True,
            "message": "Profile updated successfully"
        }

    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Change student password
# -------------------------------------------------

def change_student_password(
    user_id,
    old_password,
    new_password
):

    connection = get_connection()
    cursor = connection.cursor(
        dictionary=True
    )

    try:

        # -----------------------------------------
        # Get current password
        # -----------------------------------------

        query = """
            SELECT
                password_hash
            FROM users
            WHERE user_id = %s
              AND role = 'student'
        """

        cursor.execute(
            query,
            (user_id,)
        )

        user = cursor.fetchone()


        if not user:

            return {
                "success": False,
                "message": "Student not found"
            }


        # -----------------------------------------
        # Check old password
        # -----------------------------------------

        if old_password != user["password_hash"]:

            return {
                "success": False,
                "message": "Old password is incorrect"
            }


        # -----------------------------------------
        # Update password
        # -----------------------------------------

        query = """
            UPDATE users
            SET
                password_hash = %s
            WHERE user_id = %s
              AND role = 'student'
        """

        cursor.execute(
            query,
            (
                new_password,
                user_id
            )
        )

        connection.commit()


        return {
            "success": True,
            "message": "Password changed successfully"
        }

    finally:

        cursor.close()
        connection.close()