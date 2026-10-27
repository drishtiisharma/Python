from database import get_connection


def get_all_courses():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            course_id,
            course_name,
            credits
        FROM courses
    """

    cursor.execute(query)

    courses = cursor.fetchall()

    cursor.close()
    connection.close()

    return courses


def add_course(course_name, credits):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        query = """
            INSERT INTO courses
            (course_name, credits)
            VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (course_name, credits)
        )

        connection.commit()

        return {
            "success": True,
            "message": "Course added successfully"
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

def enroll_student(student_id, course_id):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        query = """
            INSERT INTO enrollments
            (student_id, course_id)
            VALUES (%s, %s)
        """

        cursor.execute(
            query,
            (student_id, course_id)
        )

        connection.commit()

        return {
            "success": True,
            "message": "Student enrolled successfully"
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


def remove_student_from_course(student_id, course_id):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        query = """
            DELETE FROM enrollments
            WHERE student_id = %s
            AND course_id = %s
        """

        cursor.execute(
            query,
            (student_id, course_id)
        )


        if cursor.rowcount == 0:

            return {
                "success": False,
                "message": "Student is not enrolled in this course"
            }


        connection.commit()


        return {
            "success": True,
            "message": "Student removed from course successfully"
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


