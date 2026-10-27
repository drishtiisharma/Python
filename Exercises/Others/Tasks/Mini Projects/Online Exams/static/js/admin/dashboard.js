// =================================================
// Elements
// =================================================

const logoutBtn =
    document.getElementById("logoutBtn");


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
