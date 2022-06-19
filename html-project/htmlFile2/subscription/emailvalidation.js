function validation(){
    const email = document.querySelector("#email");
    const error_message = document.querySelector(".error-text");
    const btn = document.getElementById("button");

    let regExp = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; 

    if(email.value.match(regExp) || email.value ==""){
        error_message.style.display = "none";
        btn.style.opacity = '1';
        btn.disabled = false;
    }
    else{
        error_message.style.display = "block";
        btn.style.opacity = '0.2';
        btn.disabled = true;
    }
}
