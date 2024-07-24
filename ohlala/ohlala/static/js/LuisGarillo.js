let index = 0;
let pediServices = ["Pedicura básica", "Pedicura Spa"];
let pediPrices = [600, 900];
let maniServices = ["Manicura básica", "Manicura rusa", "Manicura en gel", "Aprés Gel X", "Dip Powder", "Polygel"];
let maniPrices = [600, 900, 1000, 1200, 1500, 1200, 1200];
let maniPrice = 0;
let pediPrice = 0;

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

function setDate(event) {
    let date = new Date(event.target.value);
    let today = new Date()
    if (date.getTime() < today.getTime()) {
        document.querySelector("#date-error").textContent = "Solo se pueden agendar citas a partir de mañana.";
        document.querySelector("#agendar-fecha").value = "0000-00-00";
        return;
    }
    if (date.getDay() == 6) {
        document.querySelector("#date-error").textContent = "No se trabajan los domingos.";
        document.querySelector("#agendar-fecha").value = "0000-00-00";
        return;
    }
    document.querySelector("#date-error").textContent = "";
    document.querySelector("#confirm-date").textContent = event.target.value;
}

function setHour(event) {
    let hour = event.target.value;
    let time = "AM";
    if (hour > 11) {
        time = "PM";
    }

    if (hour > 12) {
        hour -= 12;
    }
    document.querySelector("#confirm-hour").textContent = hour + ":00 " + time;
}

function setManicure(event) {
    let value = event.target.value;
    
    if (value == 0) {
        return;
    }

    document.querySelector("#confirm-mani").textContent = maniServices[value - 1];
    document.querySelector("#mani-price").textContent = maniPrices[value - 1];

    calculatePrice(maniPrices[value - 1], pediPrice);
}

function cancelMani() {
    document.querySelector("#confirm-mani").textContent = "No se hará manicura";
    document.querySelector("#mani-price").textContent = 0;
    document.querySelector("#manicura").value = 0;
    calculatePrice(0, pediPrice);
}

function cancelPedi() {
    document.querySelector("#confirm-pedi").textContent = "No se hará pedicura";
    document.querySelector("#pedi-price").textContent = 0;
    document.querySelector("#pedicura").value = 0;
    calculatePrice(maniPrice, 0);
}

function setPedicure(event) {
    let value = event.target.value;
    
    if (value == 0) {
        return;
    }
    
    document.querySelector("#confirm-pedi").textContent = pediServices[value - 7];
    document.querySelector("#pedi-price").textContent = pediPrices[value - 7];

    calculatePrice(maniPrice, pediPrices[value - 7]);
}

function calculatePrice(mp, pp) {
    maniPrice = mp;
    pediPrice = pp;
    document.querySelector("#total").textContent = maniPrice + pediPrice;
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
    
    let dateDate = document.querySelector("#agendar-fecha");
    let hora = document.querySelector("#hora");
    let manicura = document.querySelector("#manicura");
    let pedicura = document.querySelector("#pedicura");
    let maniCancel = document.querySelector("#mani-cancel");
    let pediCancel = document.querySelector("#pedi-cancel");

    dateDate.addEventListener("input", setDate);
    hora.addEventListener("input", setHour);
    manicura.addEventListener("input", setManicure);
    pedicura.addEventListener("input", setPedicure);
    maniCancel.addEventListener("click", cancelMani);
    pediCancel.addEventListener("click", cancelPedi);
});
