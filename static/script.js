document.querySelectorAll(".doc-item").forEach(item => {
    const button = item.querySelector(".doc-button");
    const content = item.querySelector(".doc-content");
    button.addEventListener("click", () => {
        const allItems = document.querySelectorAll(".doc-item");
        allItems.forEach(i => {
            if (i !== item) {
                i.querySelector(".doc-content").classList.remove("active");
            }
        });
        content.classList.toggle("active");
    });
});
