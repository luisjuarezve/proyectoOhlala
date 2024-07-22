
function handleFooter() {
    let footerSection = document.querySelector("#hideable");
    let footerBtn = document.querySelector("#expand-btn");
    if (footerSection.classList.length < 2) {
        footerBtn.textContent = "Colapsar";
    }
    else {
        footerBtn.textContent = "Expandir";
    }
    footerSection.classList.toggle("show");
}

document.addEventListener("DOMContentLoaded", function () {
    let footerBtn = document.querySelector("#expand-btn");
    console.log(footerBtn);
    footerBtn.addEventListener("click", handleFooter);
});
