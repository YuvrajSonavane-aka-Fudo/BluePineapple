import React from 'react';
import {useRef} from 'react';


function FocusInput(){

    let inputRef = useRef(null);

    function handleClick(){
        inputRef.current.focus();
    }

    return(
        <>
            <input ref = {inputRef} placeholder = "Click to button to focus"/>
            <button onClick = {handleClick}> Click Me</button>
        </>
        
    )
}

export default FocusInput;