const navtog = document.querySelector(".nav-toggler");
navtog.addEventListener("click", navtoggle);

function navtoggle(){
    navtog.classList.toggle("active");
    const nav = document.querySelector(".nav-links");
    nav.classList.toggle("nav-active");
}

 