// =================================================
// Student Results & Evaluation Review
// =================================================

const urlParams = new URLSearchParams(window.location.search);
const initialAttemptId = urlParams.get("attempt_id");

let allResults = [];
let currentFilterSubject = "all";
let currentFilterStatus = "all";
let currentSearch = "";

// DOM Elements
const studentNameBadge = document.getElementById("studentNameBadge");
const resultsContainer = document.getElementById("resultsContainer");
const filterSubject = document.getElementById("filterSubject");
const filterStatus = document.getElementById("filterStatus");
const searchExam = document.getElementById("searchExam");
const logoutBtn = document.getElementById("logoutBtn");

// Stats Elements
const statTotalTests = document.getElementById("statTotalTests");
const statPassedTests = document.getElementById("statPassedTests");
const statFailedTests = document.getElementById("statFailedTests");
const statAvgScore = document.getElementById("statAvgScore");

// Detailed Review Modal Elements
const detailedReviewModal = document.getElementById("detailedReviewModal");
const modalReviewExamTitle = document.getElementById("modalReviewExamTitle");
const modalReviewExamSubject = document.getElementById("modalReviewExamSubject");
const modalReviewBody = document.getElementById("modalReviewBody");
const closeReviewModal = document.getElementById("closeReviewModal");


// =================================================
// Format Helpers
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

function formatDateTime(dtStr) {
    if (!dtStr) return "N/A";
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
// Load All Results
// =================================================

async function loadResults() {
    if (!resultsContainer) return;
    resultsContainer.innerHTML = '<p class="loading-state">Loading your results...</p>';

    try {
        const response = await fetch("/api/student/results");
        const data = await response.json();

        if (!data.success) {
            resultsContainer.innerHTML = `<p class="error">${data.message || "Failed to load results."}</p>`;
            return;
        }

        allResults = data.results || [];
        updateStats();
        populateSubjectFilter();
        renderResults();

        // If URL requested a specific attempt's review, open it
        if (initialAttemptId) {
            openDetailedReview(initialAttemptId);
        }

    } catch (err) {
        console.error("Error fetching results:", err);
        resultsContainer.innerHTML = '<p class="error">Failed to connect to server. Please try again.</p>';
    }
}


// =================================================
// Update Statistics
// =================================================

function updateStats() {
    const total = allResults.length;
    let passed = 0;
    let failed = 0;
    let totalPct = 0;

    allResults.forEach(r => {
        if (r.results_status === "pass") {
            passed++;
        } else {
            failed++;
        }
        totalPct += Number(r.percentage) || 0;
    });

    const avg = total > 0 ? (totalPct / total).toFixed(1) : 0;

    if (statTotalTests) statTotalTests.textContent = total;
    if (statPassedTests) statPassedTests.textContent = passed;
    if (statFailedTests) statFailedTests.textContent = failed;
    if (statAvgScore) statAvgScore.textContent = `${avg}%`;
}


// =================================================
// Populate Subject Filter
// =================================================

function populateSubjectFilter() {
    if (!filterSubject) return;

    const subjects = new Set();
    allResults.forEach(r => {
        if (r.subject_name) subjects.add(r.subject_name);
    });

    const currentVal = filterSubject.value;
    filterSubject.innerHTML = '<option value="all">All Subjects</option>';

    Array.from(subjects).sort().forEach(sub => {
        const opt = document.createElement("option");
        opt.value = sub;
        opt.textContent = sub;
        filterSubject.appendChild(opt);
    });

    filterSubject.value = currentVal || "all";
}


// =================================================
// Render Results List
// =================================================

function renderResults() {
    if (!resultsContainer) return;

    const selectedSub = filterSubject ? filterSubject.value : "all";
    const selectedStatus = filterStatus ? filterStatus.value : "all";
    const searchVal = searchExam ? searchExam.value.trim().toLowerCase() : "";

    const filtered = allResults.filter(r => {
        if (selectedSub !== "all" && r.subject_name !== selectedSub) {
            return false;
        }
        if (selectedStatus !== "all" && r.results_status !== selectedStatus) {
            return false;
        }
        if (searchVal && !r.exam_name.toLowerCase().includes(searchVal)) {
            return false;
        }
        return true;
    });

    if (filtered.length === 0) {
        if (allResults.length === 0) {
            resultsContainer.innerHTML = `
                <div class="empty-state">
                    <div style="font-size: 48px; margin-bottom: 12px;">📊</div>
                    <h3>No Exam Results Yet</h3>
                    <p>You haven't submitted any examinations yet.</p>
                    <button onclick="window.location.href='/student/exams'" class="btn-primary" style="margin-top: 15px;">
                        Browse Available Exams &rarr;
                    </button>
                </div>
            `;
        } else {
            resultsContainer.innerHTML = `
                <div class="empty-state">
                    <p>No results match your filter criteria.</p>
                    <small style="color: #64748b;">Try adjusting your subject, status or search filters.</small>
                </div>
            `;
        }
        return;
    }

    let html = `
        <div class="table-container">
            <table class="data-table results-table">
                <thead>
                    <tr>
                        <th>Exam Details</th>
                        <th>Subject</th>
                        <th>Submitted At</th>
                        <th>Score</th>
                        <th>Percentage</th>
                        <th>Breakdown</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
    `;

    filtered.forEach(r => {
        const isPass = r.results_status === "pass";
        const statusBadge = isPass
            ? '<span class="badge badge-published">PASSED</span>'
            : '<span class="badge badge-draft">FAILED</span>';

        html += `
            <tr>
                <td>
                    <div class="exam-title-cell">
                        <strong>${escapeHtml(r.exam_name)}</strong>
                        <span class="exam-desc-preview">Pass mark: ${r.passing_marks} / ${r.total_marks}</span>
                    </div>
                </td>
                <td>
                    <span class="subject-tag">${escapeHtml(r.subject_name)}</span>
                </td>
                <td style="font-size: 13px; color: #475569;">
                    ${formatDateTime(r.submitted_at || r.generated_at)}
                </td>
                <td>
                    <strong style="font-size: 15px; color: #0f172a;">${r.marks_obtained}</strong>
                    <span style="color: #64748b; font-size: 13px;"> / ${r.total_marks}</span>
                </td>
                <td>
                    <span class="score-percentage-pill ${isPass ? 'score-pct-pass' : 'score-pct-fail'}">
                        ${r.percentage}%
                    </span>
                </td>
                <td>
                    <div class="breakdown-chips-row">
                        <span class="chip-breakdown chip-correct" title="Correct answers">✓ ${r.correct_answers}</span>
                        <span class="chip-breakdown chip-wrong" title="Wrong answers">✗ ${r.wrong_answers}</span>
                        <span class="chip-breakdown chip-unanswered" title="Unanswered">─ ${r.unanswered}</span>
                    </div>
                </td>
                <td>
                    ${statusBadge}
                </td>
                <td>
                    <button
                        class="btn-primary btn-small btn-view-scorecard"
                        onclick="openDetailedReview(${r.attempt_id})"
                    >
                        Review Test &rarr;
                    </button>
                </td>
            </tr>
        `;
    });

    html += `
                </tbody>
            </table>
        </div>
    `;

    resultsContainer.innerHTML = html;
}


// =================================================
// Detailed Scorecard & Question Evaluation Review
// =================================================

async function openDetailedReview(attemptId) {
    if (!detailedReviewModal) return;

    detailedReviewModal.style.display = "flex";
    modalReviewBody.innerHTML = '<p class="loading-state">Loading detailed test evaluation...</p>';

    try {
        const response = await fetch(`/api/student/results/${attemptId}`);
        const data = await response.json();

        if (!data.success) {
            modalReviewBody.innerHTML = `<p class="error">${data.message || "Unable to load review."}</p>`;
            return;
        }

        const res = data.result;
        const questions = data.questions || [];
        const isPass = res.results_status === "pass";

        modalReviewExamTitle.textContent = res.exam_name;
        modalReviewExamSubject.textContent = `${res.subject_name} • Submitted on ${formatDateTime(res.submitted_at || res.generated_at)}`;

        const letters = ["A", "B", "C", "D", "E", "F"];

        let bodyHtml = `
            <!-- Top Scorecard Summary Banner -->
            <div class="review-scorecard-header ${isPass ? 'scorecard-pass-bg' : 'scorecard-fail-bg'}">
                <div class="scorecard-header-left">
                    <div class="review-status-pill ${isPass ? 'status-pill-pass' : 'status-pill-fail'}">
                        ${isPass ? '🏆 PASSED' : '⚠️ FAILED'}
                    </div>
                    <div class="review-score-numbers">
                        <span class="review-marks-big">${res.marks_obtained}</span>
                        <span class="review-marks-total">/ ${res.total_marks} Marks</span>
                    </div>
                    <div class="review-pct-tag">${res.percentage}% Score (Passing Mark: ${res.passing_marks})</div>
                </div>

                <div class="scorecard-header-metrics">
                    <div class="metric-card-mini">
                        <span class="m-val text-success">${res.correct_answers}</span>
                        <span class="m-lbl">Correct</span>
                    </div>
                    <div class="metric-card-mini">
                        <span class="m-val text-danger">${res.wrong_answers}</span>
                        <span class="m-lbl">Wrong</span>
                    </div>
                    <div class="metric-card-mini">
                        <span class="m-val" style="color: #64748b;">${res.unanswered}</span>
                        <span class="m-lbl">Skipped</span>
                    </div>
                    <div class="metric-card-mini">
                        <span class="m-val" style="color: #2563eb;">${res.total_questions}</span>
                        <span class="m-lbl">Total Questions</span>
                    </div>
                </div>
            </div>

            <!-- Question Review Header -->
            <div class="review-questions-title">
                <h3>Question-by-Question Evaluation</h3>
                <p>Review your answers and verified correct answers below.</p>
            </div>

            <!-- Questions List -->
            <div class="review-questions-container">
        `;

        questions.forEach((q, idx) => {
            const isCorrect = q.status === "correct";
            const isWrong = q.status === "wrong";
            const isUnanswered = q.status === "unanswered";

            let statusBadge = "";
            if (isCorrect) {
                statusBadge = `<span class="q-badge q-badge-correct">✓ Correct (+${q.marks_awarded} Marks)</span>`;
            } else if (isWrong) {
                statusBadge = `<span class="q-badge q-badge-wrong">✗ Incorrect (0 Marks)</span>`;
            } else {
                statusBadge = `<span class="q-badge q-badge-unanswered">─ Unanswered (0 Marks)</span>`;
            }

            bodyHtml += `
                <div class="review-question-card ${isCorrect ? 'q-card-correct' : isWrong ? 'q-card-wrong' : 'q-card-unanswered'}">
                    <div class="review-q-header">
                        <div class="review-q-title-group">
                            <span class="review-q-num">Question ${idx + 1}</span>
                            <span class="review-q-marks-pill">${q.marks} Mark${q.marks > 1 ? 's' : ''}</span>
                        </div>
                        <div>
                            ${statusBadge}
                        </div>
                    </div>

                    <div class="review-q-text">
                        ${escapeHtml(q.question_text)}
                    </div>

                    <div class="review-options-list">
            `;

            (q.options || []).forEach((opt, optIdx) => {
                const letter = letters[optIdx] || `${optIdx + 1}`;
                const isSelected = q.selected_option_id === opt.option_id;
                const isRightOption = opt.is_correct;

                let optionClass = "review-opt-card";
                let tagHtml = "";

                if (isRightOption && isSelected) {
                    optionClass += " opt-correct-selected";
                    tagHtml = '<span class="opt-tag tag-correct-choice">✓ Your Answer (Correct)</span>';
                } else if (isRightOption && !isSelected) {
                    optionClass += " opt-correct-unselected";
                    tagHtml = '<span class="opt-tag tag-correct-system">✓ Correct Answer</span>';
                } else if (!isRightOption && isSelected) {
                    optionClass += " opt-wrong-selected";
                    tagHtml = '<span class="opt-tag tag-wrong-choice">✗ Your Answer</span>';
                }

                bodyHtml += `
                    <div class="${optionClass}">
                        <div class="opt-left">
                            <span class="opt-letter-circle">${letter}</span>
                            <span class="opt-text-val">${escapeHtml(opt.option_text)}</span>
                        </div>
                        <div class="opt-right">
                            ${tagHtml}
                        </div>
                    </div>
                `;
            });

            if (isUnanswered) {
                bodyHtml += `
                    <div class="review-skipped-callout">
                        ⚠️ You did not select an answer for this question.
                    </div>
                `;
            }

            bodyHtml += `
                    </div>
                </div>
            `;
        });

        bodyHtml += `
            </div>
            <div style="margin-top: 25px; text-align: right;">
                <button onclick="closeReviewModalFunc()" class="btn-primary">
                    Close Scorecard
                </button>
            </div>
        `;

        modalReviewBody.innerHTML = bodyHtml;

    } catch (err) {
        console.error("Error loading detailed scorecard:", err);
        modalReviewBody.innerHTML = '<p class="error">Failed to connect to server. Please try again.</p>';
    }
}

function closeReviewModalFunc() {
    if (detailedReviewModal) {
        detailedReviewModal.style.display = "none";
    }
}

if (closeReviewModal) {
    closeReviewModal.addEventListener("click", closeReviewModalFunc);
}

window.addEventListener("click", (e) => {
    if (e.target === detailedReviewModal) {
        closeReviewModalFunc();
    }
});


// =================================================
// Filters & Search Event Listeners
// =================================================

if (filterSubject) filterSubject.addEventListener("change", renderResults);
if (filterStatus) filterStatus.addEventListener("change", renderResults);
if (searchExam) searchExam.addEventListener("input", renderResults);


// =================================================
// Logout Handling
// =================================================

if (logoutBtn) {
    logoutBtn.addEventListener("click", async (e) => {
        e.preventDefault();
        try {
            await fetch("/api/logout", { method: "POST" });
        } catch {
            // Ignore
        }
        window.location.href = "/";
    });
}


// =================================================
// Initialization
// =================================================

document.addEventListener("DOMContentLoaded", () => {
    loadStudentInfo();
    loadResults();
});
