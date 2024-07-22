
function handleFooter() {
    let footerSection = document.querySelector("#hideable");
    let footerBtn = document.querySelector("#expand-btn");
    if (footerSection.classList.length > 1) {
        footerSection.classList.toggle("show");
        footerBtn.textContent = "Colapsar";
    }
    else {
        footerSection.classList.toggle("show");
        footerBtn.textContent = "Expandir";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    let footerBtn = document.querySelector("#expand-btn");
    console.log(footerBtn);
    footerBtn.addEventListener("click", handleFooter);
});
