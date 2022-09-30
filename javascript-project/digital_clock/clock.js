function startTime(check = false){

    const today = new Date();

    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();


    let hi = today.toDateString();

    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML = h + ":" + m + ":" + s
    document.getElementById('date').innerHTML = hi
    setTimeout(startTime, 1000);

}
function checkTime(i){
    if (i < 10 ){
        i = '0'+ i
    }
    return i 
}

function change(){
    const today = new Date()

    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();

    m = checkTime(m);
    s = checkTime(s);

    var timeValue;

    if(h > 0 && h <= 12){
        timeValue = "" + h;
    }
    else if (h > 12) {
        timeValue = "" + (h-12);
    }
    else if (h == 0) {
        timeValue = "12";
    }
    timeValue += (m < 10) ? ":0" + m : ":" + m;  // get minutes
    timeValue += (s < 10) ? ":0" + s : ":" + s;  // get seconds
    timeValue += (h >= 12) ? " P.M." : " A.M.";  // get AM/PM

    const value = True
    startTime(value)
    document.getElementById('time').innerHTML = timeValue 

}