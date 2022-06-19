var getlocation = document.getElementById("check_location");
var button = document.getElementById('button_location');
var showlocation = document.getElementById('location');

function getLocation(){
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(checkposition, showError);
  } 
  else{
    check_location.innerHTML = "Sorry. Your browser does not support gelocation and you cannot join this event";
  }
}

function checkposition(position){
  if(position.coords.latitude <= 54 && position.coords.latitude >= 53 && position.coords.longitude < 0){
    getlocation.innerHTML = "Congratulations!! your location is in the range!! you have donated a bonus £10!!"
    if (typeof(Storage) !== "undefined"){
      localStorage.setItem("checkedlocation" , 'true');
      if(localStorage.getItem("checkedlocation")){
        getlocation.innerHTML = 'You have already donated. Thank you for joining us!'
        document.getElementById("current_donation").innerHTML = "Thank you for your support! You have now donated £" + sessionStorage.clickcount;
      } 
      else{
        sessionStorage.clickcount = Number(sessionStorage.clickcount) + 20;
        showlocation.innerHTML = "Your location latitude is " + position.coords.latitude + " and longitude is " + position.coords.longitude;
        getlocation.innerHTML = 'Congratulation! Your location is in range!!';
        document.getElementById("current_donation").innerHTML = "Thank you for your support! You have now donated £" + sessionStorage.clickcount;
      }
    }
    else{
      document.getElementById("current_donation").innerHTML = "Sorry, your browser does not support web storage and you cannot join this event.";
    }
  }
  else{
    location.innerHTML = "Your location latitude is " + position.coords.latitude + " and longitude is " + position.coords.longitude;
    getlocation.innerHTML = "Sorry your location is not in range! Please look forward to seeing our next event!"
  }
}
function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "You denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Sorry!Your location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "Sorry! the request is denied due to time out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "Oops! Some unknown error occurred."
      break;
    }
}

function clickCounter(){
  if (typeof(Storage) !== "undefined"){
    if (sessionStorage.clickcount){
      sessionStorage.clickcount = Number(sessionStorage.clickcount) + 1;
    } 
    else{
      sessionStorage.clickcount = 1;
    }
    document.getElementById("current_donation").innerHTML = "Thank you for your support! You have now donated £" + sessionStorage.clickcount;
  } 
  else{
    document.getElementById("current_donation").innerHTML = "Sorry, your browser does not support web storage and you cannot join this event.";
  }
}