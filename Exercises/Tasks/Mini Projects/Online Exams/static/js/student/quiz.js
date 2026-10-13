// =================================================
// State & URL Parsing
// =================================================

const urlParams = new URLSearchParams(window.location.search);
const attemptId = urlParams.get("attempt_id");

if (!attemptId) {
    alert("No attempt ID provided.");
    window.location.href = "/student/exams";
}

let attemptInfo = null;
let questions = [];
let answers = {};
let currentIndex = 0;
let remainingSeconds = 0;
let timerInterval = null;
let isSubmitting = false;

// DOM Elements - Topbar
const topbarExamName = document.getElementById("topbarExamName");
const topbarSubjectName = document.getElementById("topbarSubjectName");
const timerDisplay = document.getElementById("timerDisplay");
const quizTimerBox = document.getElementById("quizTimerBox");
const openSubmitModalBtn = document.getElementById("openSubmitModalBtn");

// DOM Elements - Question Panel
const questionCounter = document.getElementById("questionCounter");
const questionMarks = document.getElementById("questionMarks");
const saveStatus = document.getElementById("saveStatus");
const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("optionsContainer");

const prevQuestionBtn = document.getElementById("prevQuestionBtn");
const nextQuestionBtn = document.getElementById("nextQuestionBtn");
const clearSelectionBtn = document.getElementById("clearSelectionBtn");

// DOM Elements - Palette
const paletteGrid = document.getElementById("paletteGrid");
const summaryTotal = document.getElementById("summaryTotal");
const summaryAnswered = document.getElementById("summaryAnswered");
const summaryRemaining = document.getElementById("summaryRemaining");
const sidebarSubmitBtn = document.getElementById("sidebarSubmitBtn");

// DOM Elements - Submit Modal
const submitConfirmModal = document.getElementById("submitConfirmModal");
const closeSubmitModal = document.getElementById("closeSubmitModal");
const cancelSubmitBtn = document.getElementById("cancelSubmitBtn");
const finalSubmitBtn = document.getElementById("finalSubmitBtn");
const modalTotalQuestions = document.getElementById("modalTotalQuestions");
const modalAnsweredQuestions = document.getElementById("modalAnsweredQuestions");
const modalUnansweredQuestions = document.getElementById("modalUnansweredQuestions");

// DOM Elements - Result Modal
const resultModal = document.getElementById("resultModal");
const resultBadgeIcon = document.getElementById("resultBadgeIcon");
const resultTitle = document.getElementById("resultTitle");
const resultStatusBadge = document.getElementById("resultStatusBadge");
const resultScore = document.getElementById("resultScore");
const resultTotalMarks = document.getElementById("resultTotalMarks");
const resultPercentage = document.getElementById("resultPercentage");
const resCorrect = document.getElementById("resCorrect");
const resWrong = document.getElementById("resWrong");
const resUnanswered = document.getElementById("resUnanswered");
const backToExamsBtn = document.getElementById("backToExamsBtn");


// =================================================
// Format Helpers
// =================================================

function formatTime(seconds) {
    if (seconds < 0) seconds = 0;
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
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
// Fetch Quiz Data
// =================================================

async function loadQuizData() {
    try {
        const response = await fetch(`/api/student/attempts/${attemptId}`);
        const data = await response.json();

        if (!data.success) {
            alert(data.message || "Failed to load examination.");
            window.location.href = "/student/exams";
            return;
        }

        attemptInfo = data.attempt;
        questions = data.questions || [];
        answers = data.answers || {};

        if (attemptInfo.status === "submitted") {
            // Already submitted, fetch and show score
            await loadExistingResult();
            return;
        }

        if (questions.length === 0) {
            alert("This exam currently has no questions configured.");
            window.location.href = "/student/exams";
            return;
        }

        // Setup topbar
        topbarExamName.textContent = attemptInfo.exam_name;
        topbarSubjectName.textContent = attemptInfo.subject_name;

        // Setup timer
        remainingSeconds = attemptInfo.remaining_seconds;
        startTimer();

        // Render palette & initial question
        renderPalette();
        renderQuestion(0);

    } catch (err) {
        console.error("Error loading quiz:", err);
        alert("Server error connecting to quiz. Please try again.");
    }
}


// =================================================
// Timer Management
// =================================================

function startTimer() {
    updateTimerUI();

    if (timerInterval) clearInterval(timerInterval);

    timerInterval = setInterval(() => {
        remainingSeconds--;
        updateTimerUI();

        if (remainingSeconds <= 0) {
            clearInterval(timerInterval);
            alert("Time has expired! Submitting your exam automatically now.");
            submitExam(true);
        }
    }, 1000);
}

function updateTimerUI() {
    timerDisplay.textContent = formatTime(remainingSeconds);

    if (remainingSeconds <= 60) {
        quizTimerBox.className = "quiz-timer-box timer-danger";
    } else if (remainingSeconds <= 300) {
        quizTimerBox.className = "quiz-timer-box timer-warning";
    } else {
        quizTimerBox.className = "quiz-timer-box";
    }
}


// =================================================
// Render Question
// =================================================

function renderQuestion(index) {
    if (index < 0 || index >= questions.length) return;
    currentIndex = index;

    const q = questions[currentIndex];
    const totalQ = questions.length;

    questionCounter.textContent = `Question ${currentIndex + 1} of ${totalQ}`;
    questionMarks.textContent = `${q.marks} Mark${q.marks > 1 ? 's' : ''}`;
    questionText.textContent = q.question_text;

    // Render options
    optionsContainer.innerHTML = "";
    const letters = ["A", "B", "C", "D", "E", "F"];

    const selectedOptId = answers[q.question_id];

    q.options.forEach((opt, idx) => {
        const isSelected = selectedOptId === opt.option_id;
        const letter = letters[idx] || `${idx + 1}`;

        const optDiv = document.createElement("div");
        optDiv.className = `option-card ${isSelected ? "selected-option" : ""}`;
        optDiv.onclick = () => selectOption(q.question_id, opt.option_id);

        optDiv.innerHTML = `
            <div class="option-letter">${letter}</div>
            <div class="option-content">${escapeHtml(opt.option_text)}</div>
            <div class="option-radio-circle"></div>
        `;

        optionsContainer.appendChild(optDiv);
    });

    // Update navigation button states
    prevQuestionBtn.disabled = currentIndex === 0;

    if (currentIndex === totalQ - 1) {
        nextQuestionBtn.textContent = "Review & Submit \u2192";
    } else {
        nextQuestionBtn.textContent = "Next \u2192";
    }

    updatePaletteActiveState();
}


// =================================================
// Option Selection & Auto-Save
// =================================================

async function selectOption(questionId, optionId) {
    if (isSubmitting) return;

    answers[questionId] = optionId;
    renderQuestion(currentIndex);
    renderPalette();

    // Auto-save to backend
    saveStatus.textContent = "Saving answer...";
    saveStatus.className = "save-status-indicator status-saving";

    try {
        const response = await fetch(`/api/student/attempts/${attemptId}/answer`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                question_id: questionId,
                selected_option_id: optionId
            })
        });

        const data = await response.json();

        if (data.success) {
            saveStatus.textContent = "All changes saved";
            saveStatus.className = "save-status-indicator status-saved";
        } else {
            saveStatus.textContent = "Error saving answer";
            saveStatus.className = "save-status-indicator status-error";
        }
    } catch (err) {
        console.error("Auto-save error:", err);
        saveStatus.textContent = "Network error saving answer";
        saveStatus.className = "save-status-indicator status-error";
    }
}

// Clear Selection
if (clearSelectionBtn) {
    clearSelectionBtn.addEventListener("click", async () => {
        const q = questions[currentIndex];
        if (!q || !answers[q.question_id]) return;

        delete answers[q.question_id];
        renderQuestion(currentIndex);
        renderPalette();

        saveStatus.textContent = "Clearing answer...";
        saveStatus.className = "save-status-indicator status-saving";

        try {
            await fetch(`/api/student/attempts/${attemptId}/answer`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    question_id: q.question_id,
                    selected_option_id: null
                })
            });
            saveStatus.textContent = "All changes saved";
            saveStatus.className = "save-status-indicator status-saved";
        } catch {
            saveStatus.textContent = "Error clearing answer";
            saveStatus.className = "save-status-indicator status-error";
        }
    });
}


// =================================================
// Palette Rendering & Navigation
// =================================================

function renderPalette() {
    if (!paletteGrid) return;
    paletteGrid.innerHTML = "";

    const answeredCount = Object.keys(answers).length;
    const totalQ = questions.length;
    const remainingCount = totalQ - answeredCount;

    if (summaryTotal) summaryTotal.textContent = totalQ;
    if (summaryAnswered) summaryAnswered.textContent = answeredCount;
    if (summaryRemaining) summaryRemaining.textContent = remainingCount;

    questions.forEach((q, idx) => {
        const isAnswered = answers[q.question_id] !== undefined;
        const isActive = idx === currentIndex;

        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = `palette-btn ${isAnswered ? "palette-answered" : "palette-unanswered"} ${isActive ? "palette-active" : ""}`;
        btn.textContent = idx + 1;
        btn.onclick = () => renderQuestion(idx);

        paletteGrid.appendChild(btn);
    });
}

function updatePaletteActiveState() {
    const btns = paletteGrid ? paletteGrid.querySelectorAll(".palette-btn") : [];
    btns.forEach((btn, idx) => {
        if (idx === currentIndex) {
            btn.classList.add("palette-active");
        } else {
            btn.classList.remove("palette-active");
        }
    });
}


// =================================================
// Question Stepper Buttons
// =================================================

if (prevQuestionBtn) {
    prevQuestionBtn.addEventListener("click", () => {
        if (currentIndex > 0) {
            renderQuestion(currentIndex - 1);
        }
    });
}

if (nextQuestionBtn) {
    nextQuestionBtn.addEventListener("click", () => {
        if (currentIndex < questions.length - 1) {
            renderQuestion(currentIndex + 1);
        } else {
            openSubmitConfirmation();
        }
    });
}


// =================================================
// Submit Exam Flow
// =================================================

function openSubmitConfirmation() {
    const totalQ = questions.length;
    const answeredCount = Object.keys(answers).length;
    const unansweredCount = totalQ - answeredCount;

    modalTotalQuestions.textContent = totalQ;
    modalAnsweredQuestions.textContent = answeredCount;
    modalUnansweredQuestions.textContent = unansweredCount;

    submitConfirmModal.style.display = "flex";
}

function closeSubmitConfirmation() {
    submitConfirmModal.style.display = "none";
}

if (openSubmitModalBtn) openSubmitModalBtn.addEventListener("click", openSubmitConfirmation);
if (sidebarSubmitBtn) sidebarSubmitBtn.addEventListener("click", openSubmitConfirmation);
if (closeSubmitModal) closeSubmitModal.addEventListener("click", closeSubmitConfirmation);
if (cancelSubmitBtn) cancelSubmitBtn.addEventListener("click", closeSubmitConfirmation);

if (finalSubmitBtn) {
    finalSubmitBtn.addEventListener("click", () => submitExam(false));
}

async function submitExam(autoSubmitted = false) {
    if (isSubmitting) return;
    isSubmitting = true;

    if (timerInterval) clearInterval(timerInterval);

    finalSubmitBtn.disabled = true;
    finalSubmitBtn.textContent = "Submitting & Grading...";

    try {
        const response = await fetch(`/api/student/attempts/${attemptId}/submit`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ answers: answers })
        });

        const data = await response.json();

        if (!data.success) {
            alert(data.message || "Failed to submit exam.");
            isSubmitting = false;
            finalSubmitBtn.disabled = false;
            finalSubmitBtn.textContent = "Confirm Submission";
            return;
        }

        closeSubmitConfirmation();
        displayResult(data.result);

    } catch (err) {
        console.error("Submission error:", err);
        alert("Network error submitting exam. Please check connection and try again.");
        isSubmitting = false;
        finalSubmitBtn.disabled = false;
        finalSubmitBtn.textContent = "Confirm Submission";
    }
}


// =================================================
// Result Modal & Scorecard
// =================================================

function displayResult(res) {
    const isPass = res.results_status === "pass";

    resultTitle.textContent = isPass ? "Congratulations!" : "Test Completed";
    resultBadgeIcon.textContent = isPass ? "🏆" : "📝";
    resultStatusBadge.textContent = isPass ? "PASSED" : "FAILED";
    resultStatusBadge.className = `badge ${isPass ? "badge-published" : "badge-draft"}`;

    resultScore.textContent = res.marks_obtained;
    resultTotalMarks.textContent = `/ ${res.total_marks} Marks`;
    resultPercentage.textContent = `${res.percentage}% Score`;

    resCorrect.textContent = res.correct_answers;
    resWrong.textContent = res.wrong_answers;
    resUnanswered.textContent = res.unanswered;

    resultModal.style.display = "flex";
}

async function loadExistingResult() {
    try {
        const response = await fetch(`/api/student/attempts/${attemptId}/result`);
        const data = await response.json();
        if (data.success && data.result) {
            displayResult(data.result);
        } else {
            window.location.href = "/student/exams";
        }
    } catch {
        window.location.href = "/student/exams";
    }
}

const viewFullReviewBtn = document.getElementById("viewFullReviewBtn");
if (viewFullReviewBtn) {
    viewFullReviewBtn.addEventListener("click", () => {
        window.location.href = `/student/results?attempt_id=${attemptId}`;
    });
}

if (backToExamsBtn) {
    backToExamsBtn.addEventListener("click", () => {
        window.location.href = "/student/exams";
    });
}



// =================================================
// Initialization
// =================================================

document.addEventListener("DOMContentLoaded", loadQuizData);
