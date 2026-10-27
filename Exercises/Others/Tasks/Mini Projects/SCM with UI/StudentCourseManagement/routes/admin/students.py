from database import get_connection


def get_all_students():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            student_id,
            fname,
            lname,
            age,
            gender,
            email_id
        FROM students
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


from database import get_connection


def get_all_students():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            student_id,
            fname,
            lname,
            age,
            gender,
            email_id
        FROM students
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


def register_student(fname, lname, age, gender, email, password):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        # Insert user account
        query = """
            INSERT INTO users
            (email, password_hash, role)
            VALUES (%s, %s, 'student')
        """

        cursor.execute(
            query,
            (email, password)
        )

        user_id = cursor.lastrowid


        # Insert student details
        query = """
            INSERT INTO students
            (user_id, fname, lname, age, gender, email_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (user_id, fname, lname, age, gender, email)
        )


        connection.commit()

        return {
            "success": True
        }


    except Exception as e:

        connection.rollback()

        return {
            "success": False,
            "message": str(e)
        }


    finally:

        cursor.close()
        connection.close()

def update_student(student_id, fname, lname, age, gender, email):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        query = """
            UPDATE students
            SET
                fname = %s,
                lname = %s,
                age = %s,
                gender = %s,
                email_id = %s
            WHERE student_id = %s
        """

        cursor.execute(
            query,
            (
                fname,
                lname,
                age,
                gender,
                email,
                student_id
            )
        )

        if cursor.rowcount == 0:

            return {
                "success": False,
                "message": "Student not found"
            }

        connection.commit()

        return {
            "success": True,
            "message": "Student details updated successfully"
        }

    except Exception as e:

        connection.rollback()

        return {
            "success": False,
            "message": str(e)
        }

    finally:

        cursor.close()
        connection.close()


def remove_student(student_id):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        # Get the user_id of the student
        query = """
            SELECT user_id
            FROM students
            WHERE student_id = %s
        """

        cursor.execute(
            query,
            (student_id,)
        )

        student = cursor.fetchone()


        if student is None:

            return {
                "success": False,
                "message": "Student not found"
            }


        user_id = student[0]


        # Remove enrollments first
        query = """
            DELETE FROM enrollments
            WHERE student_id = %s
        """

        cursor.execute(
            query,
            (student_id,)
        )


        # Remove student
        query = """
            DELETE FROM students
            WHERE student_id = %s
        """

        cursor.execute(
            query,
            (student_id,)
        )


        # Remove user account
        query = """
            DELETE FROM users
            WHERE user_id = %s
        """

        cursor.execute(
            query,
            (user_id,)
        )


        connection.commit()


        return {
            "success": True,
            "message": "Student removed successfully"
        }


    except Exception as e:

        connection.rollback()

        return {
            "success": False,
            "message": str(e)
        }


    finally:

        cursor.close()
        connection.close()