let currentStudent = null;


// =================================================
// Load Student Details
// =================================================

async function loadStudentDetails() {

    try {

        const response = await fetch(
            "/api/student/me"
        );

        const data = await response.json();


        if (!data.success) {

            window.location.href = "/";

            return;

        }


        currentStudent = data.student;


        document.getElementById("fname").textContent =
            currentStudent.fname;

        document.getElementById("lname").textContent =
            currentStudent.lname;

        document.getElementById("email").textContent =
            currentStudent.email;

        document.getElementById("userId").textContent =
            currentStudent.user_id;

        document.getElementById("welcomeMessage").textContent =
            `Welcome, ${currentStudent.fname}!`;

    }

    catch (error) {

        console.error(error);

    }

}


// =================================================
// Logout
// =================================================

document
    .getElementById("logoutBtn")
    .addEventListener(
        "click",
        async function(event) {

            event.preventDefault();


            await fetch(
                "/api/logout",
                {
                    method: "POST"
                }
            );


            window.location.href = "/";

        }
    );


// =================================================
// Profile Elements
// =================================================

const editProfileBtn =
    document.getElementById("editProfileBtn");

const editProfileSection =
    document.getElementById("editProfileSection");

const editProfileForm =
    document.getElementById("editProfileForm");

const editFname =
    document.getElementById("editFname");

const editLname =
    document.getElementById("editLname");

const cancelEditBtn =
    document.getElementById("cancelEditBtn");

const editProfileMessage =
    document.getElementById("editProfileMessage");


// =================================================
// Password Elements
// =================================================

const changePasswordBtn =
    document.getElementById("changePasswordBtn");

const passwordModal =
    document.getElementById("passwordModal");

const closePasswordModal =
    document.getElementById("closePasswordModal");

const changePasswordForm =
    document.getElementById("changePasswordForm");

const oldPassword =
    document.getElementById("oldPassword");

const newPassword =
    document.getElementById("newPassword");

const passwordMessage =
    document.getElementById("passwordMessage");


// =================================================
// Edit Profile
// =================================================

editProfileBtn.addEventListener(
    "click",
    function() {

        editFname.value =
            currentStudent.fname;

        editLname.value =
            currentStudent.lname;

        editProfileSection.style.display =
            "block";

    }
);


// =================================================
// Cancel Edit
// =================================================

cancelEditBtn.addEventListener(
    "click",
    function() {

        editProfileSection.style.display =
            "none";

        editProfileMessage.textContent =
            "";

    }
);


// =================================================
// Save Profile
// =================================================

editProfileForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const fname =
            editFname.value.trim();

        const lname =
            editLname.value.trim();


        // -----------------------------------------
        // Validate fields
        // -----------------------------------------

        if (!fname || !lname) {

            editProfileMessage.textContent =
                "All fields are required.";

            return;

        }


        try {

            const response =
                await fetch(
                    "/api/student/profile",
                    {
                        method: "PUT",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            fname: fname,

                            lname: lname

                        })
                    }
                );


            const data =
                await response.json();


            // -------------------------------------
            // Error
            // -------------------------------------

            if (!data.success) {

                editProfileMessage.textContent =
                    data.message;

                return;

            }


            // -------------------------------------
            // Update current student
            // -------------------------------------

            currentStudent.fname =
                fname;

            currentStudent.lname =
                lname;


            // -------------------------------------
            // Update dashboard
            // -------------------------------------

            document.getElementById("fname").textContent =
                currentStudent.fname;

            document.getElementById("lname").textContent =
                currentStudent.lname;

            document.getElementById("welcomeMessage").textContent =
                `Welcome, ${currentStudent.fname}!`;


            editProfileMessage.textContent =
                "Profile updated successfully.";

        }

        catch (error) {

            console.error(error);

            editProfileMessage.textContent =
                "Unable to update profile.";

        }

    }
);


// =================================================
// Change Password Popup
// =================================================

changePasswordBtn.addEventListener(
    "click",
    function() {

        passwordModal.style.display =
            "flex";

    }
);


// =================================================
// Close Password Popup
// =================================================

closePasswordModal.addEventListener(
    "click",
    function() {

        passwordModal.style.display =
            "none";

        changePasswordForm.reset();

        passwordMessage.textContent =
            "";

    }
);


// =================================================
// Change Password
// =================================================

changePasswordForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const oldPass =
            oldPassword.value;

        const newPass =
            newPassword.value;


        // -----------------------------------------
        // Validate fields
        // -----------------------------------------

        if (!oldPass || !newPass) {

            passwordMessage.textContent =
                "All fields are required.";

            return;

        }


        try {

            const response =
                await fetch(
                    "/api/student/password",
                    {
                        method: "PUT",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            old_password:
                                oldPass,

                            new_password:
                                newPass

                        })
                    }
                );


            const data =
                await response.json();


            // -------------------------------------
            // Error
            // -------------------------------------

            if (!data.success) {

                passwordMessage.textContent =
                    data.message;

                return;

            }


            // -------------------------------------
            // Success
            // -------------------------------------

            passwordMessage.textContent =
                "Password changed successfully.";

            changePasswordForm.reset();


            setTimeout(
                function() {

                    passwordModal.style.display =
                        "none";

                    passwordMessage.textContent =
                        "";

                },
                1500
            );

        }

        catch (error) {

            console.error(error);

            passwordMessage.textContent =
                "Unable to change password.";

        }

    }
);


// =================================================
// Load Student
// =================================================

loadStudentDetails();