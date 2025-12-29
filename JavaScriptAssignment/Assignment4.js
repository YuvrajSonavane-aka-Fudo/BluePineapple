let arr = [1,2,3,4,5,6,7,8,9,10]

function operations(arr){
    console.log("The maximum values is " + Math.max(...arr))
    console.log("The min value is "+Math.min(...arr))
    let a = arr.reduce((acc , cur) => acc+cur ,0)
    console.log(a/arr.length)
    
}

operations(arr)