import React from 'react';

function TodoList(){

    let todoLst = [
        {
            id : 1,
            task : "Drink coffee"
        },
        {
            id:2,
            task : "write code"
        }

    ];

    let itemList = todoLst.map((item)=>{
        return(
        <li key = {item.id}>
            {item.task}
        </li>
        )   
    })

    return (
        <>
            <ol>
                {itemList}
            </ol>
        </>
    )
}

export default TodoList;