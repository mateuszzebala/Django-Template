const search_window = $("<div><input><button><i class=\"fa-solid fa-xmark\"></i></button></div>")
search_window.addClass("search-window")
$('body').after(search_window)

const exit_btn = search_window.find('button')
exit_btn.click(hide_search)
const search_input = search_window.find('input')
search_input.on("keydown", function (e){
    if(e.code === 'Enter'){
        alert(e.target.value)
    }
})
function show_search(){
    search_window.css("top", "0")
    search_window.css("transform", "scale(1)")
    $('body').css("overflow", "hidden")
    search_input.focus()
}

function hide_search(){
    search_window.css("top", "-100%")
    $('body').css("overflow", "hidden")
}
