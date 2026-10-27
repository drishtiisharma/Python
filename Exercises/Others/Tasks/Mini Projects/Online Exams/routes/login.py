import secrets

from database import get_connection

from utils.responses import send_json, get_json_body
from utils.sessions import get_session_id, sessions


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


# =================================================
# HTTP API
# =================================================

# -------------------------------------------------
# Login API
# -------------------------------------------------

def login_api(handler):

    data = get_json_body(handler)

    if not data:

        send_json(
            handler,
            {
                "success": False,
                "message": "Invalid request body"
            },
            400
        )

        return

    email = data.get("email")
    password = data.get("password")

    if not email or not password:

        send_json(
            handler,
            {
                "success": False,
                "message": "Email and password are required"
            },
            400
        )

        return

    result = login(
        email,
        password,
        sessions
    )

    if not result["success"]:

        send_json(
            handler,
            result,
            401
        )

        return

    session_id = result["session_id"]

    send_json(
        handler,
        {
            "success": True,
            "role": result["role"],
            "user": result["user"]
        },
        200,
        headers={
            "Set-Cookie": (
                f"session_id={session_id}; "
                "HttpOnly; "
                "Path=/"
            )
        }
    )


# -------------------------------------------------
# Logout API
# -------------------------------------------------

def logout_api(handler):

    session_id = get_session_id(handler)

    if session_id:

        logout(
            session_id,
            sessions
        )

    send_json(
        handler,
        {
            "success": True
        },
        200,
        headers={
            "Set-Cookie": (
                "session_id=; "
                "HttpOnly; "
                "Path=/; "
                "Max-Age=0"
            )
        }
    )
