
const adminsContainer =
    document.getElementById("adminsContainer");

const message =
    document.getElementById("message");

const logoutBtn =
    document.getElementById("logoutBtn");

const editAdminForm =
    document.getElementById("editAdminForm");

const editAdminId =
    document.getElementById("editAdminId");

const editAdminFname =
    document.getElementById("editAdminFname");

const editAdminLname =
    document.getElementById("editAdminLname");

const saveAdminBtn =
    document.getElementById("saveAdminBtn");

const cancelEditBtn =
    document.getElementById("cancelEditBtn");


// -------------------------------------------------
// Escape HTML before displaying database values
// -------------------------------------------------

function escapeHtml(value) {

    return String(value ?? "").replace(
        /[&<>"']/g,
        function(character) {

            const entities = {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;"
            };

            return entities[character];

        }
    );

}


// -------------------------------------------------
// Load all other admins
// -------------------------------------------------

async function loadAdmins() {

    try {

        const response = await fetch(
            "/api/admin/admins"
        );

        const data = await response.json();

        if (!response.ok || !data.success) {

            message.textContent =
                data.message || "Unable to load admins.";

            message.className = "error";

            if (response.status === 401) {
                window.location.href = "/";
            }

            return;

        }

        if (data.admins.length === 0) {

            adminsContainer.innerHTML =
                "<p>No other admins found.</p>";

            return;

        }

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

        data.admins.forEach(function(admin) {

            table += `

                <tr>

                    <td>${escapeHtml(admin.user_id)}</td>

                    <td>${escapeHtml(admin.fname)}</td>

                    <td>${escapeHtml(admin.lname)}</td>

                    <td>${escapeHtml(admin.email)}</td>

                    <td>${escapeHtml(admin.role)}</td>

                    <td>${escapeHtml(admin.created_at)}</td>

                    
                    <td class="actions-cell">

                        <button
                            class="action-btn edit-btn"
                            data-user-id="${escapeHtml(admin.user_id)}"
                            title="Edit admin"
                        >
                            ✎
                        </button>

                        <button
                            class="action-btn delete-btn"
                            data-user-id="${escapeHtml(admin.user_id)}"
                            title="Delete admin"
                        >
                            🗑
                        </button>

                    </td>


                </tr>

            `;

        });

        table += `
                </tbody>

            </table>
        `;

        adminsContainer.innerHTML = table;


        // -----------------------------------------
        // Edit buttons
        // -----------------------------------------

        document.querySelectorAll(".edit-btn").forEach(
            function(button) {

                button.addEventListener("click", function() {

                    const userId =
                        Number(button.dataset.userId);

                    const admin = data.admins.find(
                        function(item) {
                            return item.user_id === userId;
                        }
                    );

                    if (admin) {
                        openEditForm(admin);
                    }

                });

            }
        );


        // -----------------------------------------
        // Delete buttons
        // -----------------------------------------

        document.querySelectorAll(".delete-btn").forEach(
            function(button) {

                button.addEventListener("click", function() {

                    const userId =
                        Number(button.dataset.userId);

                    deleteAdmin(userId);

                });

            }
        );

    }

    catch (error) {

        console.error("Error loading admins:", error);

        message.textContent =
            "Unable to load admins.";

        message.className = "error";

    }

}


// -------------------------------------------------
// Open edit form
// -------------------------------------------------

function openEditForm(admin) {

    editAdminId.value = admin.user_id;

    editAdminFname.value = admin.fname;

    editAdminLname.value = admin.lname;

    editAdminForm.style.display = "block";

    editAdminFname.focus();

}


// -------------------------------------------------
// Close edit form
// -------------------------------------------------

function closeEditForm() {

    editAdminForm.style.display = "none";

    editAdminId.value = "";

    editAdminFname.value = "";

    editAdminLname.value = "";

}


// -------------------------------------------------
// Save updated admin
// -------------------------------------------------

saveAdminBtn.addEventListener("click", async function() {

    const userId = editAdminId.value;

    const fname = editAdminFname.value.trim();

    const lname = editAdminLname.value.trim();

    if (!fname || !lname) {

        message.textContent =
            "First and last names are required.";

        message.className = "error";

        return;

    }

    saveAdminBtn.disabled = true;

    try {

        const response = await fetch(
            `/api/admin/admins/${userId}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    fname: fname,
                    lname: lname
                })
            }
        );

        const data = await response.json();

        if (!response.ok || !data.success) {

            message.textContent =
                data.message || "Unable to update admin.";

            message.className = "error";

            return;

        }

        message.textContent =
            "Admin updated successfully.";

        message.className = "success";

        closeEditForm();

        await loadAdmins();

    }

    catch (error) {

        console.error("Error updating admin:", error);

        message.textContent =
            "Unable to update admin.";

        message.className = "error";

    }

    finally {

        saveAdminBtn.disabled = false;

    }

});


// -------------------------------------------------
// Cancel edit
// -------------------------------------------------

cancelEditBtn.addEventListener("click", function() {

    closeEditForm();

});


// -------------------------------------------------
// Delete admin
// -------------------------------------------------

async function deleteAdmin(userId) {

    const confirmed = await showAppConfirm(
        "Are you sure you want to delete this admin account?", { title: "Delete admin" }
    );

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch(
            `/api/admin/admins/${userId}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        if (!response.ok || !data.success) {

            message.textContent =
                data.message || "Unable to delete admin.";

            message.className = "error";

            return;

        }

        message.textContent =
            "Admin deleted successfully.";

        message.className = "success";

        await loadAdmins();

    }

    catch (error) {

        console.error("Error deleting admin:", error);

        message.textContent =
            "Unable to delete admin.";

        message.className = "error";

    }

}


// -------------------------------------------------
// Logout
// -------------------------------------------------

if (logoutBtn) {

    logoutBtn.addEventListener("click", async function() {

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

            console.error("Logout error:", error);

        }

    });

}


// -------------------------------------------------
// Load admins when page opens
// -------------------------------------------------

loadAdmins();
