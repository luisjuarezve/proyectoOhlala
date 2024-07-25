let body = document.querySelector("#value-body");
let title = document.querySelector(".values-title");
let container = document.querySelector(".about-container-values");
let selected = document.querySelector("#elegant");
let separator = document.querySelector("#value-separator");
let onGoing = false;

function change(event) {
    if (event.target.id !== "delicate" && event.target.id !== "elegant" && event.target.id !== "feminine") {
        return;
    }
    if (!onGoing) {
        onGoing = true;
        configure(selected);
        selected = event.target;
        configure(selected);
        onGoing = false;
    }
}

function configure(selected) {
    selected.classList.toggle("selected");
    selected.children[1].classList.toggle("selected");
    container.classList.toggle(selected.id);
    title.classList.toggle(selected.id);
    separator.classList.toggle(selected.id);
}

document.addEventListener("DOMContentLoaded", () => {
    for (let children of body.children) {
        console.log(children);
        children.addEventListener("click", change);
    }
});