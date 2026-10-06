// =================================================
// Elements
// =================================================

const studentsContainer =
    document.getElementById("studentsContainer");

const message =
    document.getElementById("message");

const logoutBtn =
    document.getElementById("logoutBtn");


// =================================================
// Load all students
// =================================================

async function loadStudents() {

    try {

        const response = await fetch(
            "/api/admin/students"
        );


        const data = await response.json();


        // -----------------------------------------
        // Error
        // -----------------------------------------

        if (!data.success) {

            message.textContent =
                data.message;

            message.className = "error";

            return;
        }


        // -----------------------------------------
        // No students
        // -----------------------------------------

        if (data.students.length === 0) {

            studentsContainer.innerHTML =
                "<p>No students found.</p>";

            return;
        }


        // -----------------------------------------
        // Create table
        // -----------------------------------------

        let table = `

            <table class="students-table">

                <thead>

                    <tr>

                        <th>ID</th>

                        <th>First Name</th>

                        <th>Last Name</th>

                        <th>Email</th>

                        <th>Role</th>

                        <th>Created At</th>

                    </tr>

                </thead>

                <tbody>

        `;


        // -----------------------------------------
        // Add students
        // -----------------------------------------

        data.students.forEach(function(student) {

            table += `

                <tr>

                    <td>
                        ${student.user_id}
                    </td>

                    <td>
                        ${student.fname}
                    </td>

                    <td>
                        ${student.lname}
                    </td>

                    <td>
                        ${student.email}
                    </td>

                    <td>
                        ${student.role}
                    </td>

                    <td>
                        ${student.created_at}
                    </td>

                </tr>

            `;

        });


        table += `

                </tbody>

            </table>

        `;


        studentsContainer.innerHTML = table;

    }

    catch (error) {

        console.error(error);

        message.textContent =
            "Unable to load students.";

        message.className = "error";

    }

}


// =================================================
// Logout
// =================================================

logoutBtn.addEventListener(
    "click",
    async function() {

        try {

            await fetch(
                "/api/logout",
                {
                    method: "POST"
                }
            );

            window.location.href = "/";

        }

        catch (error) {

            console.error(error);

        }

    }
);


// =================================================
// Load students when page opens
// =================================================

loadStudents();