from database import get_connection

def login_user(email,password):
    connection =  get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    select user_id,email,password_hash, role
    from users
    where email = %s
    """

    cursor.execute(query,(email,))

    user =  cursor.fetchone()

    cursor.close()

    connection.close()

    if user is None:
        return {
            "success" : False,
            "message" : "Invalid email or password"
        }
    if password != user['password_hash']:
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    return {
        "success" : True,
        "user_id": user["user_id"],
        "role": user['role']
    }