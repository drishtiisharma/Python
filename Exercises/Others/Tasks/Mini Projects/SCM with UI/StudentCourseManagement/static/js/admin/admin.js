function showSection(sectionId) {

    const sections =
        document.querySelectorAll(".content-section");


    sections.forEach(function(section) {

        section.classList.add("hidden");

    });


    const selectedSection =
        document.getElementById(sectionId);

    selectedSection.classList.remove("hidden");


    if (sectionId === "students") {

        loadStudents();

    }


    if (sectionId === "courses") {

        loadCourses();

    }

    if (sectionId === "enrollments") {

    loadEnrollments();

    }

    if (sectionId === "dashboard") {

    loadDashboard();

    }

}


async function loadDashboard() {

    const response =
        await fetch("/api/dashboard");


    const data =
        await response.json();


    document.getElementById(
        "totalStudents"
    ).textContent =
        data.total_students;


    document.getElementById(
        "totalCourses"
    ).textContent =
        data.total_courses;


    document.getElementById(
        "totalEnrolledStudents"
    ).textContent =
        data.total_enrolled_students;

}

async function loadEnrollments() {

    const response =
        await fetch("/api/enrollments");


    const enrollments =
        await response.json();


    const tableBody =
        document.getElementById(
            "enrollmentsTableBody"
        );


    tableBody.innerHTML = "";


    enrollments.forEach(function(enrollment) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td>${enrollment.student_id}</td>
            <td>${enrollment.student_name}</td>
            <td>${enrollment.course_id}</td>
            <td>${enrollment.course_name}</td>
            <td>${enrollment.enrolled_on}</td>
        `;


        tableBody.appendChild(row);

    });

}

async function loadCourses() {

    const response =
        await fetch("/api/courses");


    const courses =
        await response.json();


    const tableBody =
        document.getElementById(
            "coursesTableBody"
        );


    tableBody.innerHTML = "";


    courses.forEach(function(course) {

        const row =
            document.createElement("tr");


        row.innerHTML = `
            <td>${course.course_id}</td>
            <td>${course.course_name}</td>
            <td>${course.credits}</td>
        `;


        tableBody.appendChild(row);

    });

}


async function loadStudents() {

    const response = await fetch("/api/students");

    const students = await response.json();

    const tableBody = document.getElementById("studentsTableBody");

    tableBody.innerHTML = "";


    students.forEach(function(student) {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.student_id}</td>
            <td>${student.fname}</td>
            <td>${student.lname}</td>
            <td>${student.age}</td>
            <td>${student.gender}</td>
            <td>${student.email_id}</td>
        `;

        tableBody.appendChild(row);

    });

}

const registerForm = document.getElementById("registerStudentForm");


registerForm.addEventListener("submit", async function(event) {

    event.preventDefault();


    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    const email = document.getElementById("email_id").value;
    const password = document.getElementById("password").value;


    const response = await fetch("/api/students/register", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            fname: fname,
            lname: lname,
            age: age,
            gender: gender,
            email: email,
            password: password
        })

    });


    const data = await response.json();


    const message = document.getElementById("registerMessage");


    if (data.success) {

        message.textContent = "Student registered successfully!";
        message.className = "success";

        registerForm.reset();

    } else {

        message.textContent = data.message;
        message.className = "error";

    }

});


const changeStudentForm =
    document.getElementById("changeStudentForm");


changeStudentForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const studentId =
            document.getElementById(
                "changeStudentId"
            ).value;

        const fname =
            document.getElementById(
                "changeFname"
            ).value;

        const lname =
            document.getElementById(
                "changeLname"
            ).value;

        const age =
            document.getElementById(
                "changeAge"
            ).value;

        const gender =
            document.getElementById(
                "changeGender"
            ).value;

        const email =
            document.getElementById(
                "changeEmail"
            ).value;


        const response = await fetch(
            "/api/students/update",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    student_id: studentId,
                    fname: fname,
                    lname: lname,
                    age: age,
                    gender: gender,
                    email: email
                })
            }
        );


        const data = await response.json();


        const message =
            document.getElementById(
                "changeStudentMessage"
            );


        if (data.success) {

            message.textContent =
                "Student details updated successfully!";

            message.className = "success";

            changeStudentForm.reset();

        } else {

            message.textContent =
                "Cannot update student: "
                + data.message;

            message.className = "error";

        }

    }
);

const removeStudentForm =
    document.getElementById("removeStudentForm");


removeStudentForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const studentId =
            document.getElementById(
                "removeStudentId"
            ).value;


        const response = await fetch(
            "/api/students/remove",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    student_id: studentId
                })
            }
        );


        const data = await response.json();


        const message =
            document.getElementById(
                "removeStudentMessage"
            );


        if (data.success) {

            message.textContent =
                "Student removed successfully!";

            message.className = "success";

            removeStudentForm.reset();


        } else {

            message.textContent =
                "Cannot remove student: "
                + data.message;

            message.className = "error";

        }

    }
);

const addCourseForm =
    document.getElementById("addCourseForm");


addCourseForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const courseName =
            document.getElementById(
                "courseName"
            ).value;

        const credits =
            document.getElementById(
                "courseCredits"
            ).value;


        const response = await fetch(
            "/api/courses/add",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    course_name: courseName,
                    credits: credits
                })
            }
        );


        const data =
            await response.json();


        const message =
            document.getElementById(
                "addCourseMessage"
            );


        if (data.success) {

            message.textContent =
                "Course added successfully!";

            message.className = "success";

            addCourseForm.reset();

        } else {

            message.textContent =
                "Cannot add course: "
                + data.message;

            message.className = "error";

        }

    }
);


const enrollStudentForm =
    document.getElementById(
        "enrollStudentForm"
    );


enrollStudentForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const studentId =
            document.getElementById(
                "enrollStudentId"
            ).value;

        const courseId =
            document.getElementById(
                "enrollCourseId"
            ).value;


        const response = await fetch(
            "/api/enrollments/add",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    student_id: studentId,
                    course_id: courseId
                })
            }
        );


        const data =
            await response.json();


        const message =
            document.getElementById(
                "enrollStudentMessage"
            );


        if (data.success) {

            message.textContent =
                "Student enrolled successfully!";

            message.className = "success";

            enrollStudentForm.reset();

        } else {

            message.textContent =
                "Cannot enroll student: "
                + data.message;

            message.className = "error";

        }

    }
);


const removeEnrollmentForm =
    document.getElementById(
        "removeEnrollmentForm"
    );


removeEnrollmentForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const studentId =
            document.getElementById(
                "removeEnrollmentStudentId"
            ).value;

        const courseId =
            document.getElementById(
                "removeEnrollmentCourseId"
            ).value;


        const response = await fetch(
            "/api/enrollments/remove",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    student_id: studentId,
                    course_id: courseId
                })
            }
        );


        const data =
            await response.json();


        const message =
            document.getElementById(
                "removeEnrollmentMessage"
            );


        if (data.success) {

            message.textContent =
                "Student removed from course successfully!";

            message.className = "success";

            removeEnrollmentForm.reset();

        } else {

            message.textContent =
                "Cannot remove student from course: "
                + data.message;

            message.className = "error";

        }

    }
);
