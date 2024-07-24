let index = 0;

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

function advance() {
    let slides = document.querySelector("#slides");
    let firstChild = slides.children[0];
    let circles = document.querySelector("#circles");

    firstChild.classList.toggle("selected");
    slides.removeChild(firstChild);
    slides.appendChild(firstChild);
    slides.children[0].classList.toggle("selected");

    circles.children[index].classList.toggle("selected");
    index++;
    if (index > 3) {
        index = 0;
    }
    circles.children[index].classList.toggle("selected");
}

function goBack() {
    let slides = document.querySelector("#slides");
    let lastChild = slides.children[slides.children.length - 1];
    let firstChild = slides.children[0];

    slides.removeChild(lastChild);
    firstChild.classList.toggle("selected");
    slides.insertBefore(lastChild, firstChild);
    lastChild.classList.toggle("selected");

    circles.children[index].classList.toggle("selected");
    index--;
    if (index < 0) {
        index = 3;
    }
    circles.children[index].classList.toggle("selected");
}

function configureDate(dateField) {
    let date = new Date();

    let rangeDate = date.getFullYear() - 18;
    console.log("hola fechas")
    console.log(`$${rangeDate}-${date.getUTCMonth()}-${date.getUTCDate()}`)
    let month = date.getMonth()
    if (month < 10) {
        month = `0${month}`;
    }
    let day = date.getDate();
    if (day < 10) {
        day = `0${day}`;
    }
    dateField.setAttribute("max", `${rangeDate}-${month}-${day}`);
}

document.addEventListener("DOMContentLoaded", function () {
    let footerBtn = document.querySelector("#expand-btn");
    footerBtn.addEventListener("click", handleFooter);
    
    let nextBtn = document.querySelector("#next");
    let prevBtn = document.querySelector("#prev");

    if (nextBtn && prevBtn) {
        nextBtn.addEventListener("click", advance);
    prevBtn.addEventListener("click", goBack);
    }

    let dateField = document.querySelector("#date-field");
    if (dateField) {
        configureDate(dateField);
    }   
});
