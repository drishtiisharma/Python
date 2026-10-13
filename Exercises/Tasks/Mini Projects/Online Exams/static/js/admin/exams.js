// =================================================
// State & Elements
// =================================================

let allExams = [];
let allSubjects = [];

const messageEl = document.getElementById("message");
const examsContainer = document.getElementById("examsContainer");

// Stats Elements
const statTotalExams = document.getElementById("statTotalExams");
const statPublishedExams = document.getElementById("statPublishedExams");
const statDraftExams = document.getElementById("statDraftExams");
const statTotalSubjects = document.getElementById("statTotalSubjects");

// Filter Elements
const filterSubject = document.getElementById("filterSubject");
const filterStatus = document.getElementById("filterStatus");

// Modal Elements - Create Exam
const createExamModal = document.getElementById("createExamModal");
const openExamModalBtn = document.getElementById("openExamModalBtn");
const closeCreateExamModal = document.getElementById("closeCreateExamModal");
const cancelCreateExamBtn = document.getElementById("cancelCreateExamBtn");
const createExamForm = document.getElementById("createExamForm");
const createExamSubject = document.getElementById("createExamSubject");
const quickAddSubjectBtn = document.getElementById("quickAddSubjectBtn");

// Modal Elements - Edit Exam
const editExamModal = document.getElementById("editExamModal");
const closeEditExamModal = document.getElementById("closeEditExamModal");
const cancelEditExamBtn = document.getElementById("cancelEditExamBtn");
const editExamForm = document.getElementById("editExamForm");
const editExamSubject = document.getElementById("editExamSubject");

// Modal Elements - Add Subject
const addSubjectModal = document.getElementById("addSubjectModal");
const openSubjectModalBtn = document.getElementById("openSubjectModalBtn");
const closeSubjectModal = document.getElementById("closeSubjectModal");
const cancelSubjectBtn = document.getElementById("cancelSubjectBtn");
const addSubjectForm = document.getElementById("addSubjectForm");

const logoutBtn = document.getElementById("logoutBtn");


// =================================================
// Helper: Show Feedback Message
// =================================================

function showMessage(text, isSuccess = true) {
    if (!messageEl) return;
    messageEl.textContent = text;
    messageEl.className = isSuccess ? "success" : "error";
    messageEl.scrollIntoView({ behavior: "smooth", block: "nearest" });

    setTimeout(() => {
        if (messageEl.textContent === text) {
            messageEl.textContent = "";
            messageEl.className = "";
        }
    }, 4500);
}


// =================================================
// Helper: Format DateTime
// =================================================

function formatDateTime(dtStr) {
    if (!dtStr) return null;
    try {
        const d = new Date(dtStr);
        if (isNaN(d.getTime())) return dtStr;
        return d.toLocaleString([], {
            year: "numeric",
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });
    } catch {
        return dtStr;
    }
}

function toLocalInputFormat(dtStr) {
    if (!dtStr) return "";
    try {
        const d = new Date(dtStr);
        if (isNaN(d.getTime())) return "";
        const offset = d.getTimezoneOffset() * 60000;
        return (new Date(d.getTime() - offset)).toISOString().slice(0, 16);
    } catch {
        return "";
    }
}


// =================================================
// Load Subjects
// =================================================

async function loadSubjects() {
    try {
        const response = await fetch("/api/admin/subjects");
        const data = await response.json();

        if (!data.success) {
            console.error("Failed to load subjects:", data.message);
            return;
        }

        allSubjects = data.subjects || [];
        if (statTotalSubjects) {
            statTotalSubjects.textContent = allSubjects.length;
        }

        populateSubjectDropdowns();
    } catch (err) {
        console.error("Error fetching subjects:", err);
    }
}

function populateSubjectDropdowns(selectedSubjectId = null) {
    // 1. Filter dropdown
    const currentFilterVal = filterSubject.value;
    filterSubject.innerHTML = '<option value="all">All Subjects</option>';
    allSubjects.forEach(s => {
        const opt = document.createElement("option");
        opt.value = s.subject_id;
        opt.textContent = s.subject_name;
        filterSubject.appendChild(opt);
    });
    filterSubject.value = currentFilterVal || "all";

    // 2. Create exam subject dropdown
    createExamSubject.innerHTML = '<option value="">Select a subject...</option>';
    allSubjects.forEach(s => {
        const opt = document.createElement("option");
        opt.value = s.subject_id;
        opt.textContent = s.subject_name;
        createExamSubject.appendChild(opt);
    });
    if (selectedSubjectId) {
        createExamSubject.value = selectedSubjectId;
    }

    // 3. Edit exam subject dropdown
    editExamSubject.innerHTML = '<option value="">Select a subject...</option>';
    allSubjects.forEach(s => {
        const opt = document.createElement("option");
        opt.value = s.subject_id;
        opt.textContent = s.subject_name;
        editExamSubject.appendChild(opt);
    });
}


// =================================================
// Load Exams
// =================================================

async function loadExams() {
    if (!examsContainer) return;
    examsContainer.innerHTML = '<p class="loading-state">Loading exams...</p>';

    try {
        const response = await fetch("/api/admin/exams");
        const data = await response.json();

        if (!data.success) {
            showMessage(data.message || "Failed to load exams", false);
            examsContainer.innerHTML = '<p class="error">Unable to load exams.</p>';
            return;
        }

        allExams = data.exams || [];

        // Update stats
        if (statTotalExams) statTotalExams.textContent = allExams.length;
        const pubCount = allExams.filter(e => e.status === "published").length;
        const draftCount = allExams.filter(e => e.status === "draft").length;
        if (statPublishedExams) statPublishedExams.textContent = pubCount;
        if (statDraftExams) statDraftExams.textContent = draftCount;

        renderExams();
    } catch (err) {
        console.error("Error fetching exams:", err);
        showMessage("Server connection failed", false);
        examsContainer.innerHTML = '<p class="error">Server error loading exams.</p>';
    }
}


// =================================================
// Render Exams Table
// =================================================

function renderExams() {
    const selectedSub = filterSubject.value;
    const selectedStatus = filterStatus.value;

    let filtered = allExams.filter(exam => {
        if (selectedSub !== "all" && String(exam.subject_id) !== String(selectedSub)) {
            return false;
        }
        if (selectedStatus !== "all" && exam.status !== selectedStatus) {
            return false;
        }
        return true;
    });

    if (filtered.length === 0) {
        examsContainer.innerHTML = `
            <div class="empty-state">
                <p>No exams found.</p>
                <button onclick="document.getElementById('openExamModalBtn').click()" class="btn-primary btn-small">
                    Create First Exam
                </button>
            </div>
        `;
        return;
    }

    let html = `
        <table class="students-table exams-table">
            <thead>
                <tr>
                    <th style="width: 50px;">ID</th>
                    <th>Exam Title</th>
                    <th>Subject</th>
                    <th>Duration</th>
                    <th>Marks</th>
                    <th>Passing</th>
                    <th>Schedule</th>
                    <th>Status</th>
                    <th style="text-align: center; width: 220px;">Actions</th>
                </tr>
            </thead>
            <tbody>
    `;

    filtered.forEach(exam => {
        const isPublished = exam.status === "published";
        const badgeClass = isPublished ? "badge-published" : "badge-draft";
        const statusLabel = isPublished ? "Published" : "Draft";

        let scheduleText = "Always Active";
        const start = formatDateTime(exam.start_time);
        const end = formatDateTime(exam.end_time);
        if (start && end) {
            scheduleText = `${start} &rarr; ${end}`;
        } else if (start) {
            scheduleText = `From ${start}`;
        } else if (end) {
            scheduleText = `Until ${end}`;
        }

        html += `
            <tr>
                <td><strong>#${exam.exam_id}</strong></td>
                <td>
                    <div class="exam-title-cell">
                        <strong>${escapeHtml(exam.exam_name)}</strong>
                        ${exam.description ? `<span class="exam-desc-preview">${escapeHtml(exam.description)}</span>` : ""}
                    </div>
                </td>
                <td><span class="subject-tag">${escapeHtml(exam.subject_name)}</span></td>
                <td>${exam.duration_minutes} min</td>
                <td>${exam.total_marks}</td>
                <td>${exam.passing_marks}</td>
                <td class="schedule-cell"><small>${scheduleText}</small></td>
                <td>
                    <span class="badge ${badgeClass}">${statusLabel}</span>
                </td>
                <td style="text-align: center;">
                    <div class="table-actions">
                        <button
                            class="action-btn btn-status"
                            title="${isPublished ? 'Unpublish to Draft' : 'Publish to Students'}"
                            onclick="handleToggleStatus(${exam.exam_id})"
                        >
                            ${isPublished ? 'Unpublish' : 'Publish'}
                        </button>
                        <button
                            class="action-btn btn-edit"
                            title="Edit Exam"
                            onclick="handleOpenEditModal(${exam.exam_id})"
                        >
                            Edit
                        </button>
                        <button
                            class="action-btn btn-delete"
                            title="Delete Exam"
                            onclick="handleDeleteExam(${exam.exam_id}, '${escapeForJs(exam.exam_name)}')"
                        >
                            Delete
                        </button>
                    </div>
                </td>
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
    `;

    examsContainer.innerHTML = html;
}


// =================================================
// HTML escaping helpers
// =================================================

function escapeHtml(str) {
    if (!str) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

function escapeForJs(str) {
    if (!str) return "";
    return String(str).replace(/'/g, "\\'").replace(/"/g, '\\"');
}


// =================================================
// Create Exam Handler
// =================================================

if (createExamForm) {
    createExamForm.addEventListener("submit", async function(e) {
        e.preventDefault();

        const subject_id = parseInt(createExamSubject.value);
        const exam_name = document.getElementById("createExamName").value.trim();
        const description = document.getElementById("createExamDesc").value.trim();
        const duration_minutes = parseInt(document.getElementById("createExamDuration").value);
        const total_marks = parseInt(document.getElementById("createExamTotalMarks").value);
        const passing_marks = parseInt(document.getElementById("createExamPassMarks").value);
        const start_time = document.getElementById("createExamStartTime").value || null;
        const end_time = document.getElementById("createExamEndTime").value || null;
        const status = document.getElementById("createExamStatus").value;

        if (passing_marks > total_marks) {
            alert("Passing marks cannot exceed total marks.");
            return;
        }

        if (start_time && end_time && new Date(start_time) >= new Date(end_time)) {
            alert("End schedule must be later than start schedule.");
            return;
        }

        try {
            const response = await fetch("/api/admin/exams", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    subject_id,
                    exam_name,
                    description,
                    duration_minutes,
                    total_marks,
                    passing_marks,
                    start_time,
                    end_time,
                    status
                })
            });

            const data = await response.json();

            if (!data.success) {
                showMessage(data.message || "Failed to create exam", false);
                return;
            }

            showMessage("Exam created successfully!", true);
            closeModal(createExamModal);
            createExamForm.reset();
            loadExams();
        } catch (err) {
            console.error("Error creating exam:", err);
            showMessage("Network error creating exam", false);
        }
    });
}


// =================================================
// Edit Exam Handler
// =================================================

window.handleOpenEditModal = function(examId) {
    const exam = allExams.find(e => e.exam_id === examId);
    if (!exam) return;

    document.getElementById("editExamId").value = exam.exam_id;
    document.getElementById("editExamName").value = exam.exam_name;
    document.getElementById("editExamSubject").value = exam.subject_id;
    document.getElementById("editExamDesc").value = exam.description || "";
    document.getElementById("editExamDuration").value = exam.duration_minutes;
    document.getElementById("editExamTotalMarks").value = exam.total_marks;
    document.getElementById("editExamPassMarks").value = exam.passing_marks;
    document.getElementById("editExamStartTime").value = toLocalInputFormat(exam.start_time);
    document.getElementById("editExamEndTime").value = toLocalInputFormat(exam.end_time);
    document.getElementById("editExamStatus").value = exam.status || "draft";

    openModal(editExamModal);
};

if (editExamForm) {
    editExamForm.addEventListener("submit", async function(e) {
        e.preventDefault();

        const examId = document.getElementById("editExamId").value;
        const subject_id = parseInt(editExamSubject.value);
        const exam_name = document.getElementById("editExamName").value.trim();
        const description = document.getElementById("editExamDesc").value.trim();
        const duration_minutes = parseInt(document.getElementById("editExamDuration").value);
        const total_marks = parseInt(document.getElementById("editExamTotalMarks").value);
        const passing_marks = parseInt(document.getElementById("editExamPassMarks").value);
        const start_time = document.getElementById("editExamStartTime").value || null;
        const end_time = document.getElementById("editExamEndTime").value || null;
        const status = document.getElementById("editExamStatus").value;

        if (passing_marks > total_marks) {
            alert("Passing marks cannot exceed total marks.");
            return;
        }

        if (start_time && end_time && new Date(start_time) >= new Date(end_time)) {
            alert("End schedule must be later than start schedule.");
            return;
        }

        try {
            const response = await fetch(`/api/admin/exams/${examId}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    subject_id,
                    exam_name,
                    description,
                    duration_minutes,
                    total_marks,
                    passing_marks,
                    start_time,
                    end_time,
                    status
                })
            });

            const data = await response.json();

            if (!data.success) {
                showMessage(data.message || "Failed to update exam", false);
                return;
            }

            showMessage("Exam updated successfully!", true);
            closeModal(editExamModal);
            loadExams();
        } catch (err) {
            console.error("Error updating exam:", err);
            showMessage("Network error updating exam", false);
        }
    });
}


// =================================================
// Delete Exam Handler
// =================================================

window.handleDeleteExam = async function(examId, examName) {
    if (!confirm(`Are you sure you want to delete the exam "${examName}"?\nAll associated questions, student attempts, and results will also be deleted.`)) {
        return;
    }

    try {
        const response = await fetch(`/api/admin/exams/${examId}`, {
            method: "DELETE"
        });

        const data = await response.json();

        if (!data.success) {
            showMessage(data.message || "Failed to delete exam", false);
            return;
        }

        showMessage("Exam deleted successfully", true);
        loadExams();
    } catch (err) {
        console.error("Error deleting exam:", err);
        showMessage("Network error deleting exam", false);
    }
};


// =================================================
// Toggle Status Handler
// =================================================

window.handleToggleStatus = async function(examId) {
    try {
        const response = await fetch(`/api/admin/exams/${examId}/status`, {
            method: "PUT"
        });

        const data = await response.json();

        if (!data.success) {
            showMessage(data.message || "Failed to update status", false);
            return;
        }

        showMessage(data.message || "Status updated", true);
        loadExams();
    } catch (err) {
        console.error("Error toggling status:", err);
        showMessage("Network error toggling status", false);
    }
};


// =================================================
// Add Subject Handler
// =================================================

if (addSubjectForm) {
    addSubjectForm.addEventListener("submit", async function(e) {
        e.preventDefault();

        const subject_name = document.getElementById("subjectNameInput").value.trim();
        const description = document.getElementById("subjectDescInput").value.trim();

        if (!subject_name) {
            alert("Subject name is required");
            return;
        }

        try {
            const response = await fetch("/api/admin/subjects", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    subject_name,
                    description
                })
            });

            const data = await response.json();

            if (!data.success) {
                alert(data.message || "Failed to create subject");
                return;
            }

            showMessage("Subject added successfully!", true);
            closeModal(addSubjectModal);
            addSubjectForm.reset();

            // Reload subjects and pre-select the new one in the create exam form
            await loadSubjects();
            if (data.subject_id) {
                createExamSubject.value = data.subject_id;
            }
        } catch (err) {
            console.error("Error adding subject:", err);
            alert("Network error creating subject");
        }
    });
}


// =================================================
// Modal Helpers & Events
// =================================================

function openModal(modal) {
    if (!modal) return;
    modal.style.display = "flex";
}

function closeModal(modal) {
    if (!modal) return;
    modal.style.display = "none";
}

// Open Modals
if (openExamModalBtn) {
    openExamModalBtn.addEventListener("click", () => openModal(createExamModal));
}
if (openSubjectModalBtn) {
    openSubjectModalBtn.addEventListener("click", () => openModal(addSubjectModal));
}
if (quickAddSubjectBtn) {
    quickAddSubjectBtn.addEventListener("click", () => openModal(addSubjectModal));
}

// Close Modals
if (closeCreateExamModal) {
    closeCreateExamModal.addEventListener("click", () => closeModal(createExamModal));
}
if (cancelCreateExamBtn) {
    cancelCreateExamBtn.addEventListener("click", () => closeModal(createExamModal));
}
if (closeEditExamModal) {
    closeEditExamModal.addEventListener("click", () => closeModal(editExamModal));
}
if (cancelEditExamBtn) {
    cancelEditExamBtn.addEventListener("click", () => closeModal(editExamModal));
}
if (closeSubjectModal) {
    closeSubjectModal.addEventListener("click", () => closeModal(addSubjectModal));
}
if (cancelSubjectBtn) {
    cancelSubjectBtn.addEventListener("click", () => closeModal(addSubjectModal));
}

// Close on backdrop click
window.addEventListener("click", (e) => {
    if (e.target === createExamModal) closeModal(createExamModal);
    if (e.target === editExamModal) closeModal(editExamModal);
    if (e.target === addSubjectModal) closeModal(addSubjectModal);
});

// Close on ESC key
window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
        closeModal(createExamModal);
        closeModal(editExamModal);
        closeModal(addSubjectModal);
    }
});


// =================================================
// Filter Change Listeners
// =================================================

if (filterSubject) filterSubject.addEventListener("change", renderExams);
if (filterStatus) filterStatus.addEventListener("change", renderExams);


// =================================================
// Logout Handler
// =================================================

if (logoutBtn) {
    logoutBtn.addEventListener("click", async function() {
        try {
            await fetch("/api/logout", { method: "POST" });
        } catch {}
        window.location.href = "/";
    });
}


// =================================================
// Init on Page Load
// =================================================

document.addEventListener("DOMContentLoaded", async () => {
    await loadSubjects();
    await loadExams();
});
