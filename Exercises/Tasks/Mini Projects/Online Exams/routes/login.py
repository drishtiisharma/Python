import secrets

from database import get_connection


# -------------------------------------------------
# Login
# -------------------------------------------------

def login(email, password, sessions):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        query = """
            SELECT
                user_id,
                fname,
                lname,
                email,
                password_hash,
                role
            FROM users
            WHERE email = %s
        """

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        # User does not exist
        if user is None:

            return {
                "success": False,
                "message": "Invalid email or password"
            }

        # Normal password comparison
        if password != user["password_hash"]:

            return {
                "success": False,
                "message": "Invalid email or password"
            }

        # -------------------------------------------------
        # Create session
        # -------------------------------------------------

        session_id = secrets.token_hex(32)

        sessions[session_id] = {

            "user_id": user["user_id"],

            "role": user["role"],

            "fname": user["fname"],

            "lname": user["lname"],

            "email": user["email"]

        }

        return {

            "success": True,

            "session_id": session_id,

            "role": user["role"],

            "user": {

                "user_id": user["user_id"],

                "fname": user["fname"],

                "lname": user["lname"],

                "email": user["email"],

                "role": user["role"]

            }

        }

    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Logout
# -------------------------------------------------

def logout(session_id, sessions):

    if session_id in sessions:

        del sessions[session_id]

    return {
        "success": True
    }