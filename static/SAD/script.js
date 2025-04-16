document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".faq-item").forEach(item => {
        const question = item.querySelector(".faq-question");
        const answer = item.querySelector(".faq-answer");
        const icon = item.querySelector(".faq-icon");
        question.addEventListener("click", () => {
            answer.classList.toggle("active");
            icon.textContent = answer.classList.contains("active") ? "⬇" : "➡";
        });
    });

    document.querySelectorAll(".tab-button").forEach(button => {
        button.addEventListener("click", () => {
            const tab = button.parentElement;
            const content = tab.querySelector(".tab-content");
            const icon = button.querySelector(".icon");

            document.querySelectorAll(".tab").forEach(t => {
                if (t !== tab) {
                    t.classList.remove("active");
                    t.querySelector(".tab-content").style.maxHeight = null;
                    t.querySelector(".icon").textContent = "➡";
                }
            });

            tab.classList.toggle("active");
            content.style.maxHeight = tab.classList.contains("active")
                ? content.scrollHeight + "px"
                : null;

            icon.textContent = tab.classList.contains("active") ? "⬇" : "➡";
        });
    });
});