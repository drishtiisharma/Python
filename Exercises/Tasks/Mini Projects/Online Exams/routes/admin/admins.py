
from database import get_connection


# -------------------------------------------------
# Get all other admins
# -------------------------------------------------

def get_all_admins(current_user_id):

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
            WHERE role = 'admin'
            AND user_id != %s
            ORDER BY user_id
        """

        cursor.execute(query, (current_user_id,))

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Update Admin
# -------------------------------------------------

def update_admin(user_id, fname, lname, current_user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            UPDATE users
            SET fname = %s,
                lname = %s
            WHERE user_id = %s
            AND role = 'admin'
            AND user_id != %s
        """

        cursor.execute(
            query,
            (fname, lname, user_id, current_user_id)
        )

        connection.commit()

        if cursor.rowcount > 0:
            return {"success": True}

        return {
            "success": False,
            "message": "Admin not found or no changes made"
        }

    finally:

        cursor.close()
        connection.close()


# -------------------------------------------------
# Delete Admin
# -------------------------------------------------

def delete_admin(user_id, current_user_id):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            DELETE FROM users
            WHERE user_id = %s
            AND role = 'admin'
            AND user_id != %s
        """

        cursor.execute(
            query,
            (user_id, current_user_id)
        )

        connection.commit()

        if cursor.rowcount > 0:
            return {"success": True}

        return {
            "success": False,
            "message": "Admin not found or cannot delete this account"
        }

    finally:

        cursor.close()
        connection.close()
