const notification = document.querySelector('.notification');
const btn = document.querySelector('.notification_button');
const check = document.getElementById('checkbrowser');
const switchbrowser = document.getElementById('switchbrowser');

btn.addEventListener('click' ,() => {
    notification.classList.remove('active');
    localStorage.setItem('notificationDisplayed' , 'true');
});

setTimeout(checkBrowser, 1500);

function checkBrowser(){
    if(!localStorage.getItem('notificationDisplayed')){
        if(navigator.userAgent.indexOf("Chrome") != -1 ){
            check.innerHTML = ''
            notification.style.display = 'none';
        }
        else{
            notification.classList.add('active');
            notification.style.transition = '1s ease';
            notification.style.display = 'flex';

            check.innerHTML = 'Your current browser is not chrome';
            switchbrowser.style.display = 'block';
            switchbrowser.innerHTML = 'Please switch to Chrome for a better experience.';
        }
    }
}