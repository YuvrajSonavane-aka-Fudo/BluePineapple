const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());
app.use(express.json());

app.use((req,res,next) =>{
    console.log(`This is the method ${req.method} and this is the url ${req.url}`);
    next();
})
    


app.get('/' , (req , res)=>{
    res.send("Welcome to express!!");
})
//data 
app.post('/data',(req, res)=>{
    let data = req.body;
    console.log(data);

    res.status(200).json({
        response : "Data Recieved"
    })
})
//user api
app.get('/users',(req , res)=>{
    res.status(200).json([
        {
            userid : 1 ,
            name : "Yuvi",
            msg : "hello i am under the water",
        },
        {
            userid:2,
            name : "arin",
            msg:"hello i am not under the water"

        }
    ])
})
//custom 404 handler
app.use((req,res,next)=>{
    res.status(404).send("<h1>404 - Page not found</h1>");

})

app.listen(3000 , ()=>{
    console.log("Server is listening");
})