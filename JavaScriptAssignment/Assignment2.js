let number1 = 5;
let number2 = 2;

function addition(number1 , number2){
    return number1+number2
}
function subtraction(number1 , number2){
    return number1-number2
}
function multiplication(number1 , number2){
    return number1*number2
}
function division(number1 , number2){
    if (number2 === 0){
        console.log("Cannot divide by zero")
    
    }
    else{
        return number1/number2
    }
}

div = division(number1 , number2)
if(div>10){
    console.log("Division is greater than 10")

}
else{
    console.log("Division is less than 10")
}
