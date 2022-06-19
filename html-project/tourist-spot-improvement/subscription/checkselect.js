function checkselect(){
    var list = document.getElementById("list").value;
    const textarea = document.querySelector("textarea");

    if(list == "Others"){
        textarea.style.display = "block";
    }
    else{
        textarea.style.display = "none";
    }
}