import mysql.connector


# ---------- Student Dashboard ----------

def student_dashboard(student_id, student_name):

    while True:

        print("\n======= Student Dashboard =======")
        print("""
            1. View Courses
            2. Enroll in Course
            3. My Courses
            4. Drop Course
            5. Logout
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            query ="""
                select course_id, course_name, credits from courses
            """
            cursor.execute(query)
            courses = cursor.fetchall()
            print("\n==== available courses ====")

            for course in courses:
                print(
                    "ID: ",course[0],
                    "| Name: ",course[1],
                    "| Credits: ",course[2]
                )


        elif choice == "2":
            course_id = int(input("enter course ID to enroll: "))

            query = """
            insert into enrollments (student_id,course_id) value (%s, %s)
            """

            try:
                cursor.execute(query,(student_id,course_id))
                db.commit()

                print("successfully enrolled in the course!")
            except mysql.connector.Error as e:
                db.rollback()

                if e.errno == 1062:
                    print("you have already enrolled into this course.")
                elif e.errno == 1452:
                    print("course does not exist")
                else:
                    print("could not enroll in course")
                    print("error: ",e)


        elif choice == "3":
            query = """
                select c.course_id, c.course_name, c.credits, e.enrolled_on 
                from enrollments e 
                join courses c 
                on e.course_id = c.course_id 
                where e.student_id = %s
            """
            cursor.execute(query,(student_id,))
            courses =  cursor.fetchall()
            print("\n==== My Courses ===")
            if not courses:
                print("you are not enrolled in any courses.")
            else:
                for course in courses:
                    print(
                        "ID: ",course[0],
                        "| Name: ",course[1],
                        "| Credits: ",course[2],
                        "| Enrolled On: ", course[3]
                    )

        elif choice == "4":
            course_id =  input("enter course ID to drop: ")

            query = """
                delete from enrollments
                where student_id = %s
                and course_id =  %s
            """

            cursor.execute(query, (student_id,course_id))

            if cursor.rowcount > 0:
                db.commit()
                print("course dropped succcessfully.")

            else:
                print("you are not enrolled in this course")


        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice")


# ---------- MySQL Connection ----------

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="scm",
        use_pure=True
    )

    cursor = db.cursor()

    print("successfully connected to mysql")

except mysql.connector.Error as e:
    print("connection could not be successfully established")
    print("error:", e)


# ---------- Main Menu ----------

while True:

    print("\n======= Student Course Management =======")

    print("""
        1. Register
        2. Login
        3. Exit
    """)

    choice = input("choose an option (1/2/3): ")

    if choice == "1":

        name = input("enter name: ")
        email = input("enter email: ")
        password = input("enter password: ")

        query = """
            INSERT INTO students(name, email, password_hash)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, email, password))
        db.commit()

        print("student successfully registered!")

    elif choice == "2":

        email = input("enter email: ")
        password = input("enter password: ")

        query = """
            SELECT student_id, name, password_hash
            FROM students
            WHERE email = %s
        """

        cursor.execute(query, (email,))
        student = cursor.fetchone()

        if student and student[2] == password:

            print("login successful!")
            print("welcome,", student[1])

            student_dashboard(student[0], student[1])

        else:
            print("invalid email or password")

    elif choice == "3":

        print("Exiting Student Course Management...")
        break

    else:
        print("invalid choice")


cursor.close()
db.close()