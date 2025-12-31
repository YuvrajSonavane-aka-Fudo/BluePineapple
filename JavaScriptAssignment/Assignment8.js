let box = document.querySelector(".box");
let button = document.getElementById("changeColor");

button.addEventListener('click' , function(){
    box.classList.toggle("highlight");
})