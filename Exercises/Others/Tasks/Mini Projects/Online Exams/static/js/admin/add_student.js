// =================================================
// Elements
// =================================================

const message =
    document.getElementById("message");

const logoutBtn =
    document.getElementById("logoutBtn");


// =================================================
// Add Student Elements
// =================================================

const addStudentForm =
    document.getElementById("addStudentForm");

const addFname =
    document.getElementById("addFname");

const addLname =
    document.getElementById("addLname");

const addEmail =
    document.getElementById("addEmail");

const addRole =
    document.getElementById("addRole");

const addStudentBtn =
    document.getElementById("addStudentBtn");

const cancelAddStudentBtn =
    document.getElementById("cancelAddStudentBtn");


// =================================================
// Close add student form
// =================================================

function closeAddStudentForm() {

    if (!addStudentForm) {

        return;

    }


    addStudentForm.reset();

}


// =================================================
// Add Student
// =================================================

if (addStudentForm) {

    addStudentForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const fname =
                addFname.value.trim();

            const lname =
                addLname.value.trim();

            const email =
                addEmail.value.trim();

            const role =
                addRole.value;


            // -------------------------------------
            // Validate fields
            // -------------------------------------

            if (
                !fname ||
                !lname ||
                !email ||
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
                        "/api/admin/students",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({

                                fname: fname,

                                lname: lname,

                                email: email,

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
                    "Student added successfully.";

                message.className =
                    "success";


                addStudentForm.reset();

            }

            catch (error) {

                console.error(error);

                message.textContent =
                    "Unable to add student.";

                message.className =
                    "error";

            }

        }
    );

}


// =================================================
// Cancel add student
// =================================================

if (cancelAddStudentBtn) {

    cancelAddStudentBtn.addEventListener(
        "click",
        function() {

            closeAddStudentForm();

        }
    );

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
