const form = document.getElementById("loginForm");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/api/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: email,
            password: password
        })

    });

    const data = await response.json();

    const message = document.getElementById("message");

    if (data.success) {

        message.textContent = "Login successful!";
        message.className = "success";

        if (data.role === "admin") {

            window.location.href = "/admin.html";

        }

    } else {

        message.textContent = data.message;
        message.className = "error";

    }

});