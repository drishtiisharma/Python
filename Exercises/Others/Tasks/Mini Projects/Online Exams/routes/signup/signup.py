from database import get_connection


# -------------------------------------------------
# Create new student account
# -------------------------------------------------

def signup(
    fname,
    lname,
    email,
    password
):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        # -----------------------------------------
        # Check if email already exists
        # -----------------------------------------

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


        # -----------------------------------------
        # Insert new student
        # -----------------------------------------

        query = """
            INSERT INTO users
            (
                fname,
                lname,
                email,
                password_hash
            )
            VALUES
            (
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
                password
            )
        )


        connection.commit()


        return {
            "success": True
        }


    finally:

        cursor.close()
        connection.close()
