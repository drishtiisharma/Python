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


        const student = data.student;


        document.getElementById("fname").textContent =
            student.fname;

        document.getElementById("lname").textContent =
            student.lname;

        document.getElementById("email").textContent =
            student.email;

        document.getElementById("userId").textContent =
            student.user_id;


        document.getElementById("welcomeMessage").textContent =
            `Welcome, ${student.fname}!`;

    }

    catch (error) {

        console.error(error);

    }

}


document
    .getElementById("logoutBtn")
    .addEventListener("click", async function(event) {

        event.preventDefault();


        await fetch(
            "/api/logout",
            {
                method: "POST"
            }
        );


        window.location.href = "/";

    });


loadStudentDetails();