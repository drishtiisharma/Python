(function () {
    let activeResolver = null;
    function ensureDialog() {
        let overlay = document.getElementById("appDialogOverlay");
        if (overlay) return overlay;
        overlay = document.createElement("div");
        overlay.id = "appDialogOverlay";
        overlay.className = "app-dialog-overlay";
        overlay.innerHTML = `
          <section class="app-dialog" role="dialog" aria-modal="true" aria-labelledby="appDialogTitle">
            <div class="app-dialog-top"><span class="app-dialog-icon" id="appDialogIcon">i</span><button type="button" class="app-dialog-close" aria-label="Close dialog">&times;</button></div>
            <h2 id="appDialogTitle">Notice</h2><p id="appDialogMessage"></p>
            <div class="app-dialog-actions"><button type="button" class="btn-secondary" id="appDialogCancel">Cancel</button><button type="button" class="btn-primary" id="appDialogOk">OK</button></div>
          </section>`;
        document.body.appendChild(overlay);
        const finish = value => { overlay.style.display = "none"; const resolver = activeResolver; activeResolver = null; if (resolver) resolver(value); };
        overlay.querySelector(".app-dialog-close").addEventListener("click", () => finish(false));
        overlay.querySelector("#appDialogCancel").addEventListener("click", () => finish(false));
        overlay.querySelector("#appDialogOk").addEventListener("click", () => finish(true));
        overlay.addEventListener("click", e => { if (e.target === overlay) finish(false); });
        document.addEventListener("keydown", e => { if (e.key === "Escape" && overlay.style.display === "flex") finish(false); });
        overlay._finish = finish;
        return overlay;
    }
    function openDialog(message, options = {}) {
        const overlay = ensureDialog();
        const confirmMode = options.confirm === true;
        document.getElementById("appDialogTitle").textContent = options.title || (confirmMode ? "Please confirm" : "Notice");
        document.getElementById("appDialogMessage").textContent = String(message ?? "");
        document.getElementById("appDialogIcon").textContent = options.type === "error" ? "!" : (confirmMode ? "?" : "i");
        document.getElementById("appDialogCancel").style.display = confirmMode ? "" : "none";
        document.getElementById("appDialogOk").textContent = options.okText || (confirmMode ? "Confirm" : "OK");
        overlay.style.display = "flex";
        document.getElementById("appDialogOk").focus();
        return new Promise(resolve => { activeResolver = resolve; });
    }
    window.showAppDialog = (message, options = {}) => openDialog(message, options);
    window.showAppConfirm = (message, options = {}) => openDialog(message, {...options, confirm: true});
})();