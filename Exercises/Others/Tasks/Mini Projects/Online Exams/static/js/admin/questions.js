const examId = new URLSearchParams(window.location.search).get("exam_id");
const messageEl = document.getElementById("message");
const form = document.getElementById("questionForm");
const optionsEditor = document.getElementById("optionsEditor");
const questionsContainer = document.getElementById("questionsContainer");
const cancelEditBtn = document.getElementById("cancelEditBtn");
let questions = [];
let editingQuestionId = null;

function showMessage(text, success = true) {
  messageEl.textContent = text;
  messageEl.className = success ? "success" : "error";
}
function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]));
}
function renderOptionInputs(values = ["", "", "", ""]) {
  optionsEditor.innerHTML = values.map((value, index) => `
    <div class="option-editor">
      <input type="radio" name="correctOption" value="${index}" aria-label="Option ${index + 1} is correct" ${value && value.is_correct ? "checked" : ""}>
      <input type="text" class="option-text" maxlength="1000" placeholder="Option ${index + 1}" value="${escapeHtml(typeof value === "string" ? value : value.option_text)}" required>
    </div>`).join("");
}
function collectOptions() {
  const texts = [...document.querySelectorAll(".option-text")].map(el => el.value.trim());
  const selected = document.querySelector('input[name="correctOption"]:checked');
  if (texts.some(text => !text)) throw new Error("Please fill in every option field.");
  if (!selected) throw new Error("Please select the correct option.");
  return texts.map((option_text, index) => ({ option_text, is_correct: index === Number(selected.value) }));
}
function resetForm() {
  editingQuestionId = null;
  form.reset();
  document.getElementById("questionMarks").value = 1;
  document.getElementById("formTitle").textContent = "Add Question";
  document.getElementById("saveQuestionBtn").textContent = "Save Question";
  cancelEditBtn.hidden = true;
  renderOptionInputs();
}
async function loadQuestions() {
  if (!examId || !/^\d+$/.test(examId)) {
    showMessage("A valid exam_id is missing from the URL.", false);
    questionsContainer.innerHTML = "";
    return;
  }
  try {
    const response = await fetch(`/api/admin/exams/${examId}/questions`);
    const data = await response.json();
    if (!response.ok || !data.success) throw new Error(data.message || "Unable to load questions.");
    document.getElementById("examSubtitle").textContent = `${data.exam.exam_name} · ${data.questions.length} question(s) · ${data.exam.status}`;
    questions = data.questions || [];
    document.getElementById("questionCount").textContent = `${questions.length} question(s)`;
    renderQuestions();
  } catch (error) {
    showMessage(error.message || "Server error loading questions.", false);
    questionsContainer.innerHTML = "";
  }
}
function renderQuestions() {
  if (!questions.length) {
    questionsContainer.innerHTML = '<div class="empty-state"><p>No questions added yet.</p></div>';
    return;
  }
  const rows = questions.map((question, index) => `
    <tr>
      <td><strong>${index + 1}</strong></td>
      <td><div class="exam-title-cell"><strong>${escapeHtml(question.question_text)}</strong></div></td>
      <td>${Number(question.marks)}</td>
      <td><div class="question-table-options">${(question.options || []).map((option, optionIndex) => `<div class="question-table-option ${option.is_correct ? "correct-option" : ""}"><span class="option-letter">${String.fromCharCode(65 + optionIndex)}.</span> ${escapeHtml(option.option_text)}${option.is_correct ? ' <span class="correct-label">✓ Correct</span>' : ""}</div>`).join("")}</div></td>
      <td><div class="table-actions">
        <button type="button" class="action-btn btn-edit icon-action" title="Edit question" aria-label="Edit question" onclick="editQuestion(${question.question_id})"><span aria-hidden="true">✎</span></button>
        <button type="button" class="action-btn btn-delete icon-action" title="Delete question" aria-label="Delete question" onclick="removeQuestion(${question.question_id})"><span aria-hidden="true">⌫</span></button>
      </div></td>
    </tr>`).join("");
  questionsContainer.innerHTML = `
    <div class="table-container">
      <table class="students-table questions-table">
        <thead><tr><th style="width:60px">#</th><th>Question</th><th style="width:80px">Marks</th><th>Options and correct answer</th><th style="width:110px">Actions</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>`;
}
window.editQuestion = function(id) {
  const question = questions.find(item => item.question_id === id);
  if (!question) return;
  editingQuestionId = id;
  document.getElementById("questionText").value = question.question_text;
  document.getElementById("questionMarks").value = question.marks;
  document.getElementById("formTitle").textContent = "Edit Question";
  document.getElementById("saveQuestionBtn").textContent = "Update Question";
  cancelEditBtn.hidden = false;
  renderOptionInputs(question.options || []);
  form.scrollIntoView({ behavior: "smooth", block: "start" });
};
window.removeQuestion = async function(id) {
  if (!await showAppConfirm("Delete this question and its options?", { title: "Delete question" })) return;
  try {
    const response = await fetch(`/api/admin/questions/${id}`, { method: "DELETE" });
    const data = await response.json();
    if (!response.ok || !data.success) throw new Error(data.message || "Could not delete question.");
    showMessage(data.message || "Question deleted.");
    if (editingQuestionId === id) resetForm();
    await loadQuestions();
  } catch (error) { showMessage(error.message, false); }
};
form.addEventListener("submit", async event => {
  event.preventDefault();
  let options;
  try { options = collectOptions(); } catch (error) { showMessage(error.message, false); return; }
  const payload = { question_text: document.getElementById("questionText").value.trim(), marks: Number(document.getElementById("questionMarks").value), options };
  if (!payload.question_text || !Number.isInteger(payload.marks) || payload.marks < 1) { showMessage("Enter a question and positive whole-number marks.", false); return; }
  const url = editingQuestionId ? `/api/admin/questions/${editingQuestionId}` : `/api/admin/exams/${examId}/questions`;
  try {
    const response = await fetch(url, { method: editingQuestionId ? "PUT" : "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
    const data = await response.json();
    if (!response.ok || !data.success) throw new Error(data.message || "Unable to save question.");
    showMessage(data.message || "Question saved.");
    resetForm();
    await loadQuestions();
  } catch (error) { showMessage(error.message || "Server error saving question.", false); }
});
cancelEditBtn.addEventListener("click", resetForm);
document.getElementById("logoutBtn").addEventListener("click", async () => {
  try { await fetch("/api/logout", { method: "POST" }); } finally { window.location.href = "/"; }
});
renderOptionInputs();
loadQuestions();
