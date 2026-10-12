from utils.responses import (
    send_json,
    get_json_body
)

from routes.signup.signup import signup


# -------------------------------------------------
# Signup API
# -------------------------------------------------

def signup_api(handler):

    data = get_json_body(handler)


    # ---------------------------------------------
    # Check request body
    # ---------------------------------------------

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


    # ---------------------------------------------
    # Get form data
    # ---------------------------------------------

    fname = data.get("fname")

    lname = data.get("lname")

    email = data.get("email")

    password = data.get("password")


    # ---------------------------------------------
    # Validate fields
    # ---------------------------------------------

    if (
        not fname or
        not lname or
        not email or
        not password
    ):

        send_json(
            handler,
            {
                "success": False,
                "message": "All fields are required"
            },
            400
        )

        return


    # ---------------------------------------------
    # Create account
    # ---------------------------------------------

    result = signup(
            fname,
            lname,
            email,
            password
        )


    if not result["success"]:

        send_json(
            handler,
            result,
            400
        )

        return


    # ---------------------------------------------
    # Success
    # ---------------------------------------------

    send_json(
        handler,
        result,
        201
    )
