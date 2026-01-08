import React from 'react';
import {useState} from 'react'

function Counter(){
    let [count , setCount] = useState(0);

    return (
        <div>
            <h4>Count : {count}</h4>
            <button onClick = {()=>{setCount( count += 1)}}>Click me</button>
        </div>
    )
}

export default Counter;