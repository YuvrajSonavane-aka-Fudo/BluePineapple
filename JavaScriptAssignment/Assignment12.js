let modalBox = document.getElementById('modal');
let closeButton = document.getElementById('modalCloseButton');
let openButton = document.getElementById('modalOpenButton');

openButton.addEventListener('click' , function(){

    modalBox.style.display = "block";

})

closeButton.addEventListener('click' , function(){

    modalBox.style.display = "none";
})


