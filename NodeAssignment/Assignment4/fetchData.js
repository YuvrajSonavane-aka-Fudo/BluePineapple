const fs = require('fs')
const util = require('util')
const axios = require('axios')

fs.promises.appendFile("log.txt" , "Data to be fetched");

//*local data fetch

async function fetchData() {
    try {
        
        let readFile = util.promisify(fs.readFile);
        let data = await readFile('./log.txt', 'utf-8');
        console.log(data);

    } catch (error) {
        console.log(error);
    }

}

//*public url fetch

async function getPosts(url){
    try {
        
        let res = await axios.get(url);

        let filteredData = res.data.map(item =>({
            title: item.title,
            body : item.body

    }))
        for(i = 0 ; i<5 ; i++){

            console.log(filteredData[i]);
        }
        
    } 
    catch (error) {
        console.log(error);
    }
    

}

//simulate multiple api calls
async function multipleCalls(){
    try {
        let [postRes , commentsRes] = await Promise.all([
            axios.get('/posts'),
            axios.get('/comments')
        ])
        console.log([postRes , commentsRes]);
    } 
    catch (error) {
        console.log("Wont work because the api endpoints dont exist");
    }
    
}

getPosts("https://jsonplaceholder.typicode.com/posts");
multipleCalls();
fetchData();
