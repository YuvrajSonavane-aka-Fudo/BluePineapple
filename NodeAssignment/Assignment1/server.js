const http = require('http')
const helper = require('./helper')

const server = http.createServer((req , res)=>{
    if (req.url == "/"){
        res.end("Welcome to Node js!");
    }

    console.log(helper.getMessage());
    
})

server.listen(3000 , ()=>{
    console.log("Server is listening on port 3000");
})

