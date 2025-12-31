let button = document.getElementById('txtChanger');

button.addEventListener(
    "click" , function()
    {
        let txt = document.getElementById('txtChange');
        txt.textContent = "You clicked the button !";
        
    }   
);