let paragraph = document.getElementById('paragraph');
let redButton = document.getElementById('redButton');
let blueButton = document.getElementById('blueButton');

redButton.addEventListener('click', function(){

    paragraph.style.color = 'red';    
});

blueButton.addEventListener('click' , function(){

    paragraph.style.color = 'blue';
})

