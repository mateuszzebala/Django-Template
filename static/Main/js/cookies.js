
function cookieExists(name) {
    var cks = document.cookie.split(';');
    for(i = 0; i < cks.length; i++)
    if (cks[i].split('=')[0].trim() == name) return true;
}
var cookie_window = document.querySelector(".cookie-window");
var agree_cookie = document.querySelector("button.agree-cookie");
var exit_cookie = document.querySelector(".cookie-window button.exit");
window.addEventListener("load", () => {
    if(cookieExists("agree_cookie")){
        cookie_window.style.display = "none";
    }
});
function setCookie(c_name, value, exdays=365) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    console.log(exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
}
function getCookie(cName) {
    const name = cName + "=";
    const cDecoded = decodeURIComponent(document.cookie); //to be careful
    const cArr = cDecoded.split('; ');
    let res;
    cArr.forEach(val => {
      if (val.indexOf(name) === 0) res = val.substring(name.length);
    })
    return res
  }
agree_cookie.addEventListener("click", function(){
    setCookie("agree_cookie", "true", 365);
    cookie_window.style.display = "none";
});
exit_cookie.addEventListener("click", function(){
    cookie_window.style.display = "none";
});
const form_sended = document.querySelector(".form_sended");
let message_to_hide = false;
function hide_message(){
    form_sended.style.transform = 'translateY(-150%)';
    setTimeout(()=>{
        form_sended.display = "none";
    }, 3000)
}
window.addEventListener("load", ()=>{
    if(message_to_hide){
        setTimeout(()=>{
            hide_message();
        }, 10000);
    }
})
if(getCookie("form_sended") == "true"){
    form_sended.style.display="flex";
    setCookie("form_sended", "false");
    message_to_hide = true;
}
var exit = null
if(form_sended != null){
	exit = form_sended.querySelector(".exit")
}
if(exit != null){
	exit.addEventListener("click", ()=>{
    		hide_message();
	})
}
