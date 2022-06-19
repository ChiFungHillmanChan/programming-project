function validation(){
    const deadline_date = document.querySelector("#Deadline");
    const btn = document.querySelector("#button");

    var regExp = /^\(?([0-9]{4})\)?[-]?([0-1][0-9])[-]?([0-3][0-9])$/

    if(deadline_date.value.match(regExp)){
        deadline_date.style.border = '2px solid #000';
        btn.disabled = false;
    }
    else{
        deadline_date.style.border = '2px solid red';
        btn.disabled = true;
    }
}

