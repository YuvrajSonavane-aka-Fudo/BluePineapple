let form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    let isValid = true;
    
    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('mail').value.trim();
    let age = document.getElementById('age').value.trim();

    if (name == ''){
        alert("Please enter valid name");
        isValid = false;
    }

    if (email == '' || !email.includes('@') || !email.includes('.')){
        alert("Please enter a valid email");
        isValid = false;
    }

    if (age < 18){
        alert("Please enter age greater than 18");
        isValid = false;
    }
    
    if (isValid){
        alert("Form submitted successfully");
    }
    
    
});