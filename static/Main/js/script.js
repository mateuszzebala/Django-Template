const validateEmail = (email) => {
    return email.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};


document.addEventListener("scroll", () => {

    if (window.pageYOffset >= 300) {
        document.querySelector("nav.main").style.backgroundColor = "rgba(255, 255, 255, 1)";
    } else {
        document.querySelector("nav.main").style.backgroundColor = "rgba(255, 255, 255, 0.7)";
    }
})

document.querySelectorAll('#uslugi ol li').forEach(li => {
    li.addEventListener("click", () => {
        if (!li.querySelector(".drop-down").classList.contains('drop-down-open')) {
            document.querySelectorAll(".drop-down-open").forEach(dd => {
                dd.classList.remove('drop-down-open');
                dd.parentElement.querySelector("i").style.transform = "rotate(0deg)";
            })
            li.querySelector(".drop-down").classList.add('drop-down-open');
            li.querySelector("i").style.transform = "rotate(180deg)";
        }
        else {
            li.querySelector(".drop-down").classList.remove('drop-down-open');
            li.querySelector("i").style.transform = "rotate(0deg)";
        }

    })

})
const form_kontakt = document.querySelector("form#kontakt");
if(form_kontakt != null)
form_kontakt.addEventListener("submit", function(event) {
    if (!document.querySelector("#agree_message").checked) {
        event.preventDefault();
        document.querySelector("#kontakt h5").style.color = "red";
        document.querySelector(".slider").style.backgroundColor = "red";
    }
    if (document.querySelector("form#kontakt textarea").value == "") {
        event.preventDefault();
        document.querySelector("form#kontakt textarea").style.borderColor = "red";
    }
    if (document.querySelector("form#kontakt input.email").value == "") {
        event.preventDefault();
        document.querySelector("form#kontakt input.email").style.borderColor = "red";
    }
    if (!validateEmail(document.querySelector("#kontakt input.email").value)) {
        event.preventDefault();
        document.querySelector("#kontakt input").style.borderColor = "red";
    }
})
const textarea = document.querySelector("form#kontakt textarea");
if (textarea != null && textarea.value == "") {
    document.querySelector("form#kontakt textarea").style.display = "flex";
    document.querySelector("form#kontakt textarea").style.justifyContent = "center";
    document.querySelector("form#kontakt textarea").style.alignItems = "center";

}
const kontakt_input = document.querySelector("form#kontakt input");
if(kontakt_input != null)
kontakt_input.addEventListener("focus", function() {
    document.querySelector("form#kontakt input").style.borderColor = "#000";
})
if (textarea != null)
textarea.addEventListener("focus", function() {
    document.querySelector("form#kontakt textarea").style.borderColor = "#000";

})
const switch_input = document.querySelector(".switch input");
if(switch_input != null)
switch_input.addEventListener("click", function() {
    document.querySelector("#kontakt h5").style.color = "black";
    document.querySelector(".slider").style.backgroundColor = "#ccc";
})
let mobilemenu_open = false;
const nav = document.querySelector("nav.main");
const mobilemenu = document.querySelector(".mobilemenu");
const burger = document.querySelector(".burger");
const [burger_span_1, burger_span_2, burger_span_3] = document.querySelectorAll(".burger span");
mobilemenu.style.top = "-100%";
mobilemenu.style.transition = "0.3s";
const mobilemenu_toggle = function() {
    if (mobilemenu_open) {
        if (window.pageYOffset < 300) {
            nav.style.backgroundColor = "rgba(255, 255, 255, 0.7)";
        }
        nav.style.boxShadow = "0 0 10px #000";
        mobilemenu.style.top = "-100%";
        mobilemenu.style.boxShadow = "none";
        burger_span_1.classList.remove("burger-span-1");
        burger_span_2.classList.remove("burger-span-2");
        burger_span_3.classList.remove("burger-span-3");
        mobilemenu_open = false;
    }
    else {
        nav.style.backgroundColor = "rgba(255, 255, 255, 1)";
        mobilemenu.style.top = "0";
        nav.style.boxShadow = "none";
        mobilemenu.style.boxShadow = "0 0 10px #000";
        burger_span_1.classList.add("burger-span-1");
        burger_span_2.classList.add("burger-span-2");
        burger_span_3.classList.add("burger-span-3");
        mobilemenu_open = true;
    }
}
document.querySelector("button.burger").addEventListener("click", mobilemenu_toggle);

window.addEventListener("resize", () => {
    if (window.innerWidth > 1000 && mobilemenu_open) {
        mobilemenu_toggle();
    }
})

document.querySelectorAll(".mobilemenu a").forEach(a => {
    a.addEventListener("click", mobilemenu_toggle)
})
