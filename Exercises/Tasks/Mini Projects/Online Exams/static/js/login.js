// =================================================
// Get form elements
// =================================================

const loginForm =
    document.getElementById("loginForm");

const message =
    document.getElementById("message");


// =================================================
// Login
// =================================================

loginForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        // -----------------------------------------
        // Get input values
        // -----------------------------------------

        const email =
            document.getElementById("email").value;

        const password =
            document.getElementById("password").value;


        try {

            // -------------------------------------
            // Send login request
            // -------------------------------------

            const response = await fetch(
                "/api/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                }
            );


            // -------------------------------------
            // Convert response to JSON
            // -------------------------------------

            const data =
                await response.json();


            // -------------------------------------
            // Successful login
            // -------------------------------------

            if (data.success) {

                message.textContent =
                    "Login successful.";

                message.className =
                    "success";


                // ---------------------------------
                // Redirect based on role
                // ---------------------------------

                setTimeout(function() {

                    if (data.role === "admin") {

                        window.location.href =
                            "/admin";

                    }

                    else {

                        window.location.href =
                            "/student";

                    }

                }, 500);

            }


            // -------------------------------------
            // Login failed
            // -------------------------------------

            else {

                message.textContent =
                    data.message;

                message.className =
                    "error";

            }

        }


        // -----------------------------------------
        // Server connection error
        // -----------------------------------------

        catch (error) {

            console.error(error);

            message.textContent =
                "Unable to connect to server.";

            message.className =
                "error";

        }

    }
);