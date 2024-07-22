
function handleFooter() {
    let footerSection = document.querySelector(".hideable-section");
    let footerBtn = document.querySelector("#expand-btn");
    if (footerSection.classList.length > 1) {
        footerSection.classList.remove("hidden");
        footerBtn.textContent = "Colapsar";
    }
    else {
        footerSection.classList.add("hidden");
        footerBtn.textContent = "Expandir";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    let footerBtn = document.querySelector("#expand-btn");
    console.log(footerBtn);
    footerBtn.addEventListener("click", handleFooter);
});
