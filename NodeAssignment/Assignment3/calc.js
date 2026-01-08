class Calculator{
    result ;
    
    constructor(result){
        this.result = 0;
    }
    
    add(n){
        this.result = this.result + n;  
        return this;  
    }

    subtract(n){
        this.result -= n;
        return this;
    }

    multiply(n){
        this.result *= n;
        return this;

    }

    divide(n){
        if(n==0){
            console.log("Cannot divide by 0");
            return this
        }
        else{
            this.result  = this.result / n;
            return this;
        }
    }

    getResult(){
        console.log(this.result);
        return this;
    }

}

let c = new Calculator;

c.add(5).subtract(2).multiply(3).divide(0).getResult();

//part 2
const fs = require('fs');
const util = require('util');

readFile = util.promisify(fs.readFile);
function fetchData(){
    setTimeout(()=>{
        readFile('./log.txt' , 'utf-8')
        .then(console.log("Data fetched successfully"))
        .catch((err)=>{
            console.log(err);
        })
    }, 2000);
}

fetchData()