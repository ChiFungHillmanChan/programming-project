function reveal(){
    var reveals = document.querySelectorAll('.reveal');

    for (var i =0; i < reveals.length; i++){
        var Height = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;

        if(elementTop < Height - elementVisible){
            reveals[i].classList.add('active');
        }
        else{
            reveals[i].classList.remove('active')
        }
    } 
}

window.addEventListener('scroll', reveal)