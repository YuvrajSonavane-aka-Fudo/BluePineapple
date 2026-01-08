const fs = require('fs');
const util = require('util')

function createFile(logText) {
    let text = logText;
    fs.promises.appendFile("log.txt", text);

}

function blockingFunction(path) {
    let fileContent = fs.readFileSync(path, 'utf-8');
    console.log("Blocking Function " + fileContent);
    return 0;

}

async function nonBlockingFunction(path) {

    try {
        let readFile = util.promisify(fs.readFile);

        let fileContent = await readFile(path, 'utf-8');
        console.log("NonBlocking Function " + fileContent);
        return fileContent;
    } 
    catch (error) {
        console.log("Failed to load file");
    }


}

function timeOut(){

    setTimeout(() => {
        console.log("This is the timeout funtion which executed after 3 secs")
    }, 3000);
}

function interval(){

    setInterval(()=>{
        console.log(" this is setinterval and keeps printing after every 2 secs");
    }, 2000);
}

function nextTick(){

    process.nextTick(
        ()=>{
            console.log("Next tick method that runs on high priority");
        }
    )
}



createFile("\nthis is the log text which is added every time script runs");

nonBlockingFunction('./log.txt');//runs out of sync
blockingFunction('./log.txt');// runs in sync

timeOut()
interval()
nextTick()
