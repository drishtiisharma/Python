// =================================================
// Elements
// =================================================

const signupForm =
    document.getElementById("signupForm");

const fname =
    document.getElementById("fname");

const lname =
    document.getElementById("lname");

const email =
    document.getElementById("email");

const password =
    document.getElementById("password");

const confirmPassword =
    document.getElementById("confirmPassword");

const message =
    document.getElementById("message");


// =================================================
// Sign Up
// =================================================

signupForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const firstName =
            fname.value.trim();

        const lastName =
            lname.value.trim();

        const userEmail =
            email.value.trim();

        const userPassword =
            password.value;

        const confirmedPassword =
            confirmPassword.value;


        // -----------------------------------------
        // Validate fields
        // -----------------------------------------

        if (
            !firstName ||
            !lastName ||
            !userEmail ||
            !userPassword ||
            !confirmedPassword
        ) {

            message.textContent =
                "All fields are required.";

            message.className =
                "error";

            return;

        }


        // -----------------------------------------
        // Check passwords
        // -----------------------------------------

        if (
            userPassword !==
            confirmedPassword
        ) {

            message.textContent =
                "Passwords do not match.";

            message.className =
                "error";

            return;

        }


        try {

            const response =
                await fetch(
                    "/api/signup",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            fname: firstName,

                            lname: lastName,

                            email: userEmail,

                            password: userPassword

                        })

                    }
                );


            const data =
                await response.json();


            // -------------------------------------
            // Error
            // -------------------------------------

            if (!data.success) {

                message.textContent =
                    data.message;

                message.className =
                    "error";

                return;

            }


            // -------------------------------------
            // Success
            // -------------------------------------

            message.textContent =
                "Account created successfully. Redirecting to login...";

            message.className =
                "success";


            signupForm.reset();


            setTimeout(
                function() {

                    window.location.href =
                        "/";

                },
                1500
            );

        }

        catch (error) {

            console.error(error);

            message.textContent =
                "Unable to create account.";

            message.className =
                "error";

        }

    }
);
