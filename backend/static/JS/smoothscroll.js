var sidebarNewsBlock = document.getElementById("sidebarNewsBlock"),
children = sidebarNewsBlock.children,
allChildren =[],
stepScroll = 20,//регулировка скорости прокрутки №1
nodeElem;

//получаем всех детей sidebarNewsBlock
for (var i=0; i<children.length; i++){
 if (children[i].children.length > 0) {
     for (var h=0; h<children[i].children.length; h++){
         allChildren.push(children[i].children[h]);
     }
 } else if(children[i].children.length == 0){
     allChildren.push(children[i]);
 }
}

sidebarNewsBlock.onwheel = function(event){
window.event.returnValue = false;
var r = event.deltaY;
//определяем направление движения колесика мышки
    if (r>0){
        for (var i=0; i<allChildren.length; i++){
        var t = allChildren[i].getBoundingClientRect();
            if (t.top >0) {
                nodeElem = allChildren[i]
                lowScroll();
                break;
                }
        }
} else if (r<0) {
    for (var i=0; i<allChildren.length; i++){
        var t = allChildren[i].getBoundingClientRect();
        if ((t.top <= 0 && t.top > -2) || t.top > 0){
            var g = i-1;
            if (g>=0) {
                nodeElem = allChildren[g];
                lowScroll();
                break;
                }else if (g<0){
                    sidebarNewsBlock.scrollTo(0,0)
                    break;				
                }
            }
        }
}
}

function lowScroll(){
var k = nodeElem.getBoundingClientRect();
var t = sidebarNewsBlock.scrollTop+sidebarNewsBlock.clientHeight;
var timer = 0;
if (k.top >0){
    if (t == sidebarNewsBlock.scrollHeight) {return};//определяем достигла ли прокрутка низа
    if (stepScroll < k.top){
        sidebarNewsBlock.scrollBy(0,stepScroll);
        timer = setTimeout(lowScroll, 50);//регулировка скорости прокрутки №2
    } else if (stepScroll > k.top) {
        sidebarNewsBlock.scrollBy(0,k.top+1);
        if (timer == 0) return;
        clearTimeout(timer);
        
    }

} else if (k.top < 0) {
    var reverseStepScroll = 0-stepScroll;
    if (reverseStepScroll > k.top){
        sidebarNewsBlock.scrollBy(0,reverseStepScroll);
        timer = setTimeout(lowScroll, 50);//регулировка скорости прокрутки №2
    } else if (stepScroll >= k.top) {
        sidebarNewsBlock.scrollBy(0,k.top+1);
        clearTimeout(timer);
    }
}
}