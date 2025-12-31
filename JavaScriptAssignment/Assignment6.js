let button = document.getElementById('addItem');
let ulList = document.getElementById('ulList');

button.addEventListener('click' , function(){

    let itemCount = ulList.children.length;
    
    let newItem = document.createElement('li');

    newItem.textContent = "Item " + (itemCount+1);

    ulList.append(newItem);



    
});
