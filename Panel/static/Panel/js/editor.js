const ff_tiles = document.querySelectorAll('a.ff')
const movable_tiles = document.querySelectorAll('a.ff:not(:first-child)')
const tail_info = document.createElement('div')
tail_info.classList.add('tail_info')
document.body.appendChild(tail_info)
const isMobile = navigator.userAgentData.mobile

if(!isMobile)
ff_tiles.forEach(elem => {
    elem.addEventListener("mousemove", (e)=>{
        tail_info.innerHTML=elem.querySelector('span.filename').innerHTML
        tail_info.style.display = "inline-block"
        tail_info.style.left = (e.clientX + 20) + "px"
        tail_info.style.top = (e.clientY + document.body.scrollTop) + "px"
    })
    elem.addEventListener("mouseleave", (e)=>{
        tail_info.style.display = "none"
    })
})

ff_tiles.forEach(elem => {
    const i = elem.querySelector('i')

    if(i.classList.contains('icon-dir')){
        i.classList.add('fa-regular')
        i.classList.add('fa-folder')
    }
    if(i.classList.contains('icon-file')){
        i.classList.add('fa-solid')
        i.classList.add('fa-file')
    }
    if(i.classList.contains('icon-music')){
        i.classList.add('fa-solid')
        i.classList.add('fa-music')
    }
    if(i.classList.contains('icon-image')){
        i.classList.add('fa-solid')
        i.classList.add('fa-image')
    }
    if(i.classList.contains('icon-video')){
        i.classList.add('fa-solid')
        i.classList.add('fa-video')
    }
    if(i.classList.contains('icon-code')){
        i.classList.add('fa-solid')
        i.classList.add('fa-code')
    }
    if(i.classList.contains('icon-run')){
        i.classList.add('fa-solid')
        i.classList.add('fa-person-running')
    }
    if(i.classList.contains('icon-database')){
        i.classList.add('fa-solid')
        i.classList.add('fa-database')
    }
    if(i.classList.contains('icon-up')){
        i.classList.add('fa-solid')
        i.classList.add('fa-chevron-up')
    }
})


const window_form = document.createElement("form")
window_form.setAttribute("enctype", 'multipart/form-data')
window_form.method = "POST"
window_form.classList.add("window_form")
let new_window = null

const topbar_btns = document.querySelectorAll('.editor-tools button')
topbar_btns.forEach(btn => {
    btn.addEventListener("click", e => {
        if(new_window !== null)
            new_window.remove()
        new_window = window_form.cloneNode()
        const input_type = btn.getAttribute("input-type")
        new_window.innerHTML = btn.innerHTML
        const input = document.createElement('input')
        input.type = input_type

        input.name = btn.getAttribute("name")
        if (btn.getAttribute("args") !== null)
        btn.getAttribute('args').split(";").forEach(arg=>{
            input.setAttribute(arg, "")
        })
        new_window.appendChild(input)
        const button = document.createElement("button")
        button.type = "submit"
        button.innerHTML = "OK"
        new_window.appendChild(button)
        const exit_btn = document.createElement('button')
        exit_btn.setAttribute("type", "button")
        exit_btn.innerHTML = "<i class=\"fa-solid fa-xmark\"></i>"
        exit_btn.classList.add("x-btn")

        new_window.appendChild(exit_btn)
        new_window.innerHTML += `<input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">`
        showAndFadeIn(new_window, 0.3, document.body)
        document.querySelector('.window_form .x-btn').addEventListener("click", (e)=>{
            fadeOutAndHide(new_window, 0.3)
        })
    })
})




function showAndFadeIn (elem,sec, parent)
{
    parent.appendChild(elem)
    elem.style.transition = `0s`
    elem.style.opacity = 0;
    elem.style.transition = `${sec}s`
    elem.style.opacity = 1;

}
let mouse_down = false
let dragable = document.createElement('div')
let dragable_elem = null
dragable.classList.add('dragable')
dragable.style.position = "absolute"
dragable.style.transform = "translate(-50%, -50%)"
dragable.innerHTML ="ITEM"
dragable.style.zIndex = 10
movable_tiles.forEach(elem => {
    elem.addEventListener("mousedown", ()=>{

        mouse_down = true

    })
    elem.addEventListener("mousemove", ()=>{
        if(mouse_down && dragable_elem === null){
            dragable_elem = elem

        elem.style.opacity = "0"
        dragable.innerHTML = elem.innerHTML
        document.body.appendChild(dragable)
        }
    })
})

window.addEventListener("mousemove", (e)=>{
    dragable.style.top = e.clientY + "px"
    dragable.style.left = e.clientX + "px"

})

window.addEventListener("mouseup", (e)=>{
    dragable.remove()
    dragable_elem.style.opacity = "0.8"
    dragable_elem = null
    mouse_down = false
})


window.onblur = () =>{
    mouse_down = false
}