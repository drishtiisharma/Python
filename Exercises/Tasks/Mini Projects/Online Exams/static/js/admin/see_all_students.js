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
// Edit Student Elements
// =================================================

const editStudentForm =
    document.getElementById("editStudentForm");

const editUserId =
    document.getElementById("editUserId");

const editFname =
    document.getElementById("editFname");

const editLname =
    document.getElementById("editLname");

const editRole =
    document.getElementById("editRole");

const saveStudentBtn =
    document.getElementById("saveStudentBtn");

const cancelEditBtn =
    document.getElementById("cancelEditBtn");


// =================================================
// Load all students
// =================================================

async function loadStudents() {

    if (!studentsContainer) {

        return;

    }


    try {

        const response =
            await fetch(
                "/api/admin/students"
            );


        const data =
            await response.json();


        // -----------------------------------------
        // Error
        // -----------------------------------------

        if (!data.success) {

            message.textContent =
                data.message;

            message.className =
                "error";

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

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

        `;


        // -----------------------------------------
        // Add students
        // -----------------------------------------

        data.students.forEach(
            function(student) {

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

                        <td class="actions-cell">

                            <button
                                class="action-btn edit-btn"
                                data-user-id="${student.user_id}"
                                title="Edit student"
                            >
                                ✎
                            </button>

                            <button
                                class="action-btn delete-btn"
                                data-user-id="${student.user_id}"
                                title="Delete student"
                            >
                                🗑
                            </button>

                        </td>

                    </tr>

                `;

            }
        );


        table += `

                </tbody>

            </table>

        `;


        studentsContainer.innerHTML =
            table;


        // -----------------------------------------
        // Edit buttons
        // -----------------------------------------

        const editButtons =
            document.querySelectorAll(
                ".edit-btn"
            );


        editButtons.forEach(
            function(button) {

                button.addEventListener(
                    "click",
                    function() {

                        const userId =
                            Number(
                                button.dataset.userId
                            );


                        const student =
                            data.students.find(
                                function(student) {

                                    return (
                                        student.user_id ===
                                        userId
                                    );

                                }
                            );


                        if (!student) {

                            return;

                        }


                        openEditForm(student);

                    }
                );

            }
        );


        // -----------------------------------------
        // Delete buttons
        // -----------------------------------------

        const deleteButtons =
            document.querySelectorAll(
                ".delete-btn"
            );


        deleteButtons.forEach(
            function(button) {

                button.addEventListener(
                    "click",
                    function() {

                        const userId =
                            Number(
                                button.dataset.userId
                            );


                        deleteStudent(userId);

                    }
                );

            }
        );

    }

    catch (error) {

    console.error("DELETE ERROR:", error);

    message.textContent =
        "Unable to delete student.";

    message.className =
        "error";

}

}


// =================================================
// Open edit form
// =================================================

function openEditForm(student) {

    if (!editStudentForm) {

        return;

    }


    editUserId.value =
        student.user_id;

    editFname.value =
        student.fname;

    editLname.value =
        student.lname;

    editRole.value =
        student.role;


    editStudentForm.style.display =
        "block";


    editFname.focus();

}


// =================================================
// Close edit form
// =================================================

function closeEditForm() {

    if (!editStudentForm) {

        return;

    }


    editStudentForm.style.display =
        "none";


    editUserId.value =
        "";

    editFname.value =
        "";

    editLname.value =
        "";

    editRole.value =
        "";

}


// =================================================
// Save edited student
// =================================================

if (saveStudentBtn) {

    saveStudentBtn.addEventListener(
        "click",
        async function() {

            const userId =
                editUserId.value;


            const fname =
                editFname.value.trim();


            const lname =
                editLname.value.trim();


            const role =
                editRole.value;


            // -------------------------------------
            // Validate fields
            // -------------------------------------

            if (
                !fname ||
                !lname ||
                !role
            ) {

                message.textContent =
                    "All fields are required.";

                message.className =
                    "error";

                return;

            }


            try {

                const response =
                    await fetch(
                        `/api/admin/students/${userId}`,
                        {
                            method: "PUT",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({

                                fname: fname,

                                lname: lname,

                                role: role

                            })

                        }
                    );


                const data =
                    await response.json();


                // ---------------------------------
                // Error
                // ---------------------------------

                if (!data.success) {

                    message.textContent =
                        data.message;

                    message.className =
                        "error";

                    return;

                }


                // ---------------------------------
                // Success
                // ---------------------------------

                message.textContent =
                    "User updated successfully.";

                message.className =
                    "success";


                closeEditForm();


                loadStudents();

            }

            catch (error) {

                console.error(error);

                message.textContent =
                    "Unable to update user.";

                message.className =
                    "error";

            }

        }
    );

}


// =================================================
// Cancel edit
// =================================================

if (cancelEditBtn) {

    cancelEditBtn.addEventListener(
        "click",
        function() {

            closeEditForm();

        }
    );

}


// =================================================
// Delete student
// =================================================

async function deleteStudent(userId) {

    const confirmed =
        confirm(
            "Are you sure you want to delete this student?"
        );


    if (!confirmed) {

        return;

    }


    try {

        const response =
            await fetch(
                `/api/admin/students/${userId}`,
                {
                    method: "DELETE"
                }
            );


        const data =
            await response.json();


        // -----------------------------------------
        // Error
        // -----------------------------------------

        if (!data.success) {

            message.textContent =
                data.message;

            message.className =
                "error";

            return;

        }


        // -----------------------------------------
        // Success
        // -----------------------------------------

        message.textContent =
            "Student deleted successfully.";

        message.className =
            "success";


        loadStudents();

    }

    catch (error) {

        console.error(error);

        message.textContent =
            "Unable to delete student.";

        message.className =
            "error";

    }

}


// =================================================
// Logout
// =================================================

if (logoutBtn) {

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


                window.location.href =
                    "/";

            }

            catch (error) {

                console.error(error);

            }

        }
    );

}


// =================================================
// Load students when page opens
// =================================================

loadStudents();
