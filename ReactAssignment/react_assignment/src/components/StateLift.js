import React from 'react';
import {useState} from 'react';



function InputModule({value , onUpdate}){
    return (
    <>
        <input value = {value}  onChange = {(e)=>{onUpdate(e.target.value)}}/>
    </>
    )
}

function OutputModule({value}){
    return (
    <p>The message is :-  {value}</p>
    )
}

function StateLift(){
    let [Msg , setMsg] = useState("");
    return (
    <>
        <InputModule value = {Msg} onUpdate = {setMsg}/>
        <OutputModule value = {Msg}/>
    </>
    )

    
}

export default StateLift;