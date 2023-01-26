const edit_page_switch = $('input#edit-page-switch')
const root = $(".root")
const editable = $("editable.editable")
const edit_page_submit = $(".edit-page-submit")

function block_click(e){
                e.stopPropagation();
            e.preventDefault();
}


edit_page_switch.change(e => {
    const clickable = $('a, button, div, span, li, ul, ol, input')
    if (edit_page_switch.is(":checked")) {
        clickable.on("click", block_click);
        $('nav.admin-menu, nav.admin-menu *').off("click", block_click);
        document.querySelector('nav.admin-menu').removeEventListener("click", block_click)
        editable.each(function () {
            $(this).attr("contenteditable", "true")
            $(this).on("input", e => {
                edit_page_submit.removeClass("success")
                edit_page_submit.addClass("alert")
                const me = $(this)
                $(`editable.editable[text=${$(this).attr('text')}]:not(:focus)`).each(function () {

                    $(this).html(me.html())

                })

            })
        })
    } else {
        clickable.off("click", block_click);
        editable.each(function () {
            $(this).removeAttr("contenteditable")
        })
    }
})

edit_page_submit.click(e => {
    const data = {}
    edit_page_submit.css({
        "cursor": "wait"
    })
    let i = 0
    editable.each(function () {
        data[i] = {
            "html": $(this).html(),
            "main": $(this).attr('main'),
            "text": $(this).attr('text'),
            "key": $(this).attr('key')
        }
        i += 1
    })
    postData('/edit-page/', {
        "data": data,
        "language": document.querySelector("html").getAttribute('lang')
    }).then(res => {
        if (res.save === true) {
            edit_page_submit.addClass("success")
            edit_page_submit.removeClass("alert")
        }
        edit_page_submit.css({
            "cursor": "pointer"
        })
    }).catch(()=>{
        edit_page_submit.css({
            "cursor": "pointer"
        })
    })
})

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'multipart/from-data; charset=utf-8'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data)
    });
    return response.json();
}
