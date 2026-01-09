import {useEffect , useState} from 'react';

function ApiCall(){
    let [data , setData] = useState([]);

    useEffect(()=>{

         let response = async () => {
            try {

                let res =  await fetch("https://jsonplaceholder.typicode.com/users");
                let jsonData = await res.json();
                return setData(jsonData)

            } 
            catch (error) {
                console.log(error);
            }
            
         } 

         response();
    },[])

    return(
        <p>Name : {data[0]?.name || "Loading"} , Email : {data[0]?.email || "Loading"} </p>
    )

}

export default ApiCall;