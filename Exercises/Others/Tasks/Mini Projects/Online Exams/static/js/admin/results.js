let adminResults = [];
const resultsContainer = document.getElementById("adminResultsContainer");
const resultsMessage = document.getElementById("message");

function resultMessage(text, ok = true) {
    resultsMessage.textContent = text;
    resultsMessage.className = ok ? "success" : "error";
}
function escResult(value) {
    return String(value ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}
function renderAdminResults() {
    const status = document.getElementById("resultStatusFilter").value;
    const term = document.getElementById("resultSearch").value.trim().toLowerCase();
    const rows = adminResults.filter(r => {
        if (status === "published" && !r.is_published) return false;
        if (status === "pending" && r.is_published) return false;
        return !term || `${r.fname} ${r.lname} ${r.email} ${r.exam_name} ${r.subject_name}`.toLowerCase().includes(term);
    });
    document.getElementById("totalResults").textContent = adminResults.length;
    document.getElementById("publishedResults").textContent = adminResults.filter(r => r.is_published).length;
    document.getElementById("pendingResults").textContent = adminResults.filter(r => !r.is_published).length;
    if (!rows.length) {
        resultsContainer.innerHTML = '<div class="empty-state"><p>No results match your filters.</p></div>';
        return;
    }
    resultsContainer.innerHTML = `<div class="table-responsive"><table class="students-table results-table">
      <thead><tr><th>Student</th><th>Exam</th><th>Score</th><th>Outcome</th><th>Submitted</th><th>Publication</th><th>Action</th></tr></thead>
      <tbody>${rows.map(r => `<tr>
        <td><strong>${escResult(r.fname)} ${escResult(r.lname)}</strong><small class="table-subtext">${escResult(r.email)}</small></td>
        <td><strong>${escResult(r.exam_name)}</strong><small class="table-subtext">${escResult(r.subject_name)}</small></td>
        <td>${Number(r.marks_obtained).toFixed(2)} / ${escResult(r.total_marks)}<small class="table-subtext">${Number(r.percentage).toFixed(1)}% · ${r.correct_answers} correct</small></td>
        <td><span class="badge ${r.results_status === "pass" ? "badge-published" : "badge-draft"}">${r.results_status === "pass" ? "Passed" : "Failed"}</span></td>
        <td>${escResult(r.submitted_at || r.generated_at || "—")}</td>
        <td><span class="badge ${r.is_published ? "badge-published" : "badge-draft"}">${r.is_published ? "Published" : "Pending"}</span></td>
        <td><button class="action-btn ${r.is_published ? "btn-status" : "btn-edit"}" title="${r.is_published ? "Unpublish result" : "Publish result"}" aria-label="${r.is_published ? "Unpublish result" : "Publish result"}" onclick="toggleResultPublication(${r.attempt_id}, ${r.is_published})">${r.is_published ? "◉" : "↗"}</button></td>
      </tr>`).join("")}</tbody></table></div>`;
}
async function loadAdminResults() {
    resultsContainer.innerHTML = '<p class="loading-state">Loading results...</p>';
    try {
        const response = await fetch("/api/admin/results");
        const data = await response.json();
        if (!response.ok || !data.success) throw new Error(data.message || "Could not load results.");
        adminResults = data.results || [];
        renderAdminResults();
    } catch (error) {
        resultsContainer.innerHTML = `<div class="empty-state"><p>${escResult(error.message)}</p></div>`;
    }
}
window.toggleResultPublication = async function(attemptId, currentlyPublished) {
    const action = currentlyPublished ? "unpublish" : "publish";
    const confirmed = await showAppConfirm(`Are you sure you want to ${action} this result? ${currentlyPublished ? "The student will no longer be able to see it." : "The student will be able to see the score and review."}`, {title: `${action[0].toUpperCase()}${action.slice(1)} result`});
    if (!confirmed) return;
    try {
        const response = await fetch(`/api/admin/results/${attemptId}/publish`, {method: "PUT"});
        const data = await response.json();
        if (!response.ok || !data.success) throw new Error(data.message || "Unable to update publication.");
        resultMessage(data.message, true);
        await loadAdminResults();
    } catch (error) { resultMessage(error.message, false); }
};
document.getElementById("resultStatusFilter").addEventListener("change", renderAdminResults);
document.getElementById("resultSearch").addEventListener("input", renderAdminResults);
document.getElementById("refreshResultsBtn").addEventListener("click", loadAdminResults);
document.getElementById("logoutBtn").addEventListener("click", async () => { try { await fetch("/api/logout", {method:"POST"}); } finally { location.href="/"; }});
loadAdminResults();
