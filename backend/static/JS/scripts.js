function textAreaInput(textarea){
    textarea.style.height = '1px';
    textarea.style.height = (textarea.scrollHeight + 6) + 'px';
}


function initTextArea(){
    let areas = document.getElementsByClassName('js-textarea');
    for (let textarea of areas){
        textarea.oninput = function(){ textAreaInput(textarea); };
        textAreaInput(textarea);
    }
}
