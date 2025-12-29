let arr  = [];
for(let i = 0 ; i<10 ; i++){
    a = Math.random()
    arr.push(a)
}

console.log(arr)

function operations(arr){
    console.log("The maximum values is " + Math.max(...arr))
    console.log("The min value is "+Math.min(...arr))
    let a = arr.reduce((acc , cur) => acc+cur ,0)
    console.log(a/arr.length)
    
}

operations(arr)