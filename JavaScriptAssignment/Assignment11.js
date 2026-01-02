let timer = document.getElementById('timer');
let startTime = 10;


let counter = setInterval(function (){
    timer.textContent = startTime;
    startTime--;

    if (startTime < 0){
        timer.textContent = "Time's Up";
        
    }

}, 1000)