// =================================================
// State & Elements
// =================================================

let allExams = [];
let selectedExamForStart = null;

const availableExamsContainer = document.getElementById("availableExamsContainer");
const filterSubject = document.getElementById("filterSubject");
const searchExam = document.getElementById("searchExam");
const studentNameBadge = document.getElementById("studentNameBadge");
const messageEl = document.getElementById("message");

// Modal Elements
const startExamModal = document.getElementById("startExamModal");
const closeStartExamModal = document.getElementById("closeStartExamModal");
const cancelStartBtn = document.getElementById("cancelStartBtn");
const confirmStartBtn = document.getElementById("confirmStartBtn");

const modalExamTitle = document.getElementById("modalExamTitle");
const modalExamSubject = document.getElementById("modalExamSubject");
const modalExamDesc = document.getElementById("modalExamDesc");
const modalExamDuration = document.getElementById("modalExamDuration");
const modalExamMarks = document.getElementById("modalExamMarks");
const modalExamPass = document.getElementById("modalExamPass");

const logoutBtn = document.getElementById("logoutBtn");


// =================================================
// Load Student Profile
// =================================================

async function loadStudentInfo() {
    try {
        const response = await fetch("/api/student/me");
        const data = await response.json();

        if (data.success && data.student) {
            if (studentNameBadge) {
                studentNameBadge.textContent = `${data.student.fname} ${data.student.lname}`;
            }
        }
    } catch (err) {
        console.error("Error loading student info:", err);
    }
}


// =================================================
// Load Available Exams
// =================================================

async function loadAvailableExams() {
    if (!availableExamsContainer) return;
    availableExamsContainer.innerHTML = '<p class="loading-state">Loading active tests...</p>';

    try {
        const response = await fetch("/api/student/exams");
        const data = await response.json();

        if (!data.success) {
            availableExamsContainer.innerHTML = `<p class="error">${data.message || "Unable to load exams"}</p>`;
            return;
        }

        allExams = data.exams || [];
        populateSubjectFilter();
        renderExams();
    } catch (err) {
        console.error("Error fetching student exams:", err);
        availableExamsContainer.innerHTML = '<p class="error">Failed to connect to server.</p>';
    }
}


// =================================================
// Populate Subject Filter
// =================================================

function populateSubjectFilter() {
    if (!filterSubject) return;

    const subjectsMap = new Map();
    allExams.forEach(e => {
        if (!subjectsMap.has(e.subject_id)) {
            subjectsMap.set(e.subject_id, e.subject_name);
        }
    });

    const currentVal = filterSubject.value;
    filterSubject.innerHTML = '<option value="all">All Subjects</option>';
    subjectsMap.forEach((name, id) => {
        const opt = document.createElement("option");
        opt.value = id;
        opt.textContent = name;
        filterSubject.appendChild(opt);
    });
    filterSubject.value = currentVal || "all";
}


// =================================================
// Format Helpers
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

function escapeHtml(str) {
    if (!str) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


// =================================================
// Render Exams
// =================================================

function renderExams() {
    const selectedSub = filterSubject ? filterSubject.value : "all";
    const searchVal = searchExam ? searchExam.value.trim().toLowerCase() : "";

    const filtered = allExams.filter(exam => {
        if (selectedSub !== "all" && String(exam.subject_id) !== String(selectedSub)) {
            return false;
        }
        if (searchVal && !exam.exam_name.toLowerCase().includes(searchVal)) {
            return false;
        }
        return true;
    });

    if (filtered.length === 0) {
        availableExamsContainer.innerHTML = `
            <div class="empty-state">
                <p>No published exams are currently available for you.</p>
                <small style="color: #64748b;">Check back later or contact your instructor.</small>
            </div>
        `;
        return;
    }

    let html = '<div class="student-exams-grid">';

    filtered.forEach(exam => {
        const isSubmitted = exam.attempt_status === "submitted";
        const isInProgress = exam.attempt_status === "in_progress";

        let scheduleNotice = "";
        const start = formatDateTime(exam.start_time);
        const end = formatDateTime(exam.end_time);
        if (start && end) {
            scheduleNotice = `<div class="exam-schedule-pill">📅 ${start} &rarr; ${end}</div>`;
        } else if (end) {
            scheduleNotice = `<div class="exam-schedule-pill">⏳ Closes on ${end}</div>`;
        }

        let actionButtonHtml = "";
        if (isSubmitted) {
            actionButtonHtml = `
                <button
                    class="btn-secondary btn-completed"
                    onclick="window.location.href='/student/results?attempt_id=${exam.attempt_id}'"
                    title="View scorecard and review"
                >
                    ✓ View Result &rarr;
                </button>
            `;
        } else if (isInProgress) {
            actionButtonHtml = `
                <button
                    class="btn-primary btn-resume"
                    onclick="handleOpenStartModal(${exam.exam_id})"
                >
                    Resume Test &rarr;
                </button>
            `;
        } else {
            actionButtonHtml = `
                <button
                    class="btn-primary btn-start-test"
                    onclick="handleOpenStartModal(${exam.exam_id})"
                >
                    Start Test &rarr;
                </button>
            `;
        }

        html += `
            <div class="student-exam-card">
                <div class="card-header">
                    <span class="subject-tag">${escapeHtml(exam.subject_name)}</span>
                    ${isSubmitted ? '<span class="badge badge-published">Submitted</span>' : ''}
                    ${isInProgress ? '<span class="badge badge-draft">In Progress</span>' : ''}
                </div>

                <h3 class="exam-card-title">${escapeHtml(exam.exam_name)}</h3>

                <p class="exam-card-desc">
                    ${exam.description ? escapeHtml(exam.description) : 'No specific instructions provided.'}
                </p>

                <div class="exam-metrics-row">
                    <div class="metric-item">
                        <span class="metric-label">Duration</span>
                        <strong class="metric-val">⏱ ${exam.duration_minutes} Mins</strong>
                    </div>
                    <div class="metric-item">
                        <span class="metric-label">Total Marks</span>
                        <strong class="metric-val">🎯 ${exam.total_marks}</strong>
                    </div>
                    <div class="metric-item">
                        <span class="metric-label">Pass Marks</span>
                        <strong class="metric-val">🏁 ${exam.passing_marks}</strong>
                    </div>
                </div>

                ${scheduleNotice}

                <div class="card-footer">
                    ${actionButtonHtml}
                </div>
            </div>
        `;
    });

    html += '</div>';

    availableExamsContainer.innerHTML = html;
}


// =================================================
// Start Test Confirmation Modal
// =================================================

window.handleOpenStartModal = function(examId) {
    const exam = allExams.find(e => e.exam_id === examId);
    if (!exam) return;

    selectedExamForStart = exam;

    modalExamTitle.textContent = exam.exam_name;
    modalExamSubject.textContent = exam.subject_name;
    modalExamDesc.textContent = exam.description || "Answer all questions within the allocated time.";
    modalExamDuration.textContent = `${exam.duration_minutes} minutes`;
    modalExamMarks.textContent = `${exam.total_marks} marks`;
    modalExamPass.textContent = `${exam.passing_marks} marks`;

    if (startExamModal) {
        startExamModal.style.display = "flex";
    }
};

function closeConfirmModal() {
    if (startExamModal) {
        startExamModal.style.display = "none";
    }
    selectedExamForStart = null;
}

if (closeStartExamModal) closeStartExamModal.addEventListener("click", closeConfirmModal);
if (cancelStartBtn) cancelStartBtn.addEventListener("click", closeConfirmModal);

if (confirmStartBtn) {
    confirmStartBtn.addEventListener("click", async () => {
        if (!selectedExamForStart) return;
        const examId = selectedExamForStart.exam_id;
        confirmStartBtn.disabled = true;
        confirmStartBtn.textContent = "Starting...";

        try {
            const response = await fetch(`/api/student/exams/${examId}/start`, {
                method: "POST"
            });
            const data = await response.json();

            if (!data.success) {
                alert(data.message || "Failed to start exam.");
                confirmStartBtn.disabled = false;
                confirmStartBtn.textContent = "Begin Test";
                return;
            }

            closeConfirmModal();
            window.location.href = `/student/quiz?attempt_id=${data.attempt_id}`;
        } catch (err) {
            console.error("Error starting exam:", err);
            alert("Network error starting exam. Please try again.");
            confirmStartBtn.disabled = false;
            confirmStartBtn.textContent = "Begin Test";
        }
    });
}

window.addEventListener("click", (e) => {
    if (e.target === startExamModal) closeConfirmModal();
});

window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeConfirmModal();
});


// =================================================
// Filter & Search Listeners
// =================================================

if (filterSubject) filterSubject.addEventListener("change", renderExams);
if (searchExam) searchExam.addEventListener("input", renderExams);


// =================================================
// Logout
// =================================================

if (logoutBtn) {
    logoutBtn.addEventListener("click", async (e) => {
        e.preventDefault();
        try {
            await fetch("/api/logout", { method: "POST" });
        } catch {}
        window.location.href = "/";
    });
}


// =================================================
// Page Initialization
// =================================================

document.addEventListener("DOMContentLoaded", () => {
    loadStudentInfo();
    loadAvailableExams();
});
