let img = document.getElementById("image");
let button = document.getElementById("imgChange");

button.addEventListener('click', function(){

    img.src = "KnightArtorias.jpg";
    button.textContent = "Image Changed";

})