function shuffleArray(arr) {
    const array = [...arr]
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array
}

function fadeOutAndHide (elem,sec)
{
    elem.style.transition = `${sec}s`
    elem.style.opacity = 0;
    elem.style.top = "40%"
    setTimeout(()=>{
        elem.remove()
    }, sec*1000)
}
