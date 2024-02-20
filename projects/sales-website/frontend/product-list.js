"use strict";

function addProduct(id, title, description, price, image) {
    let table = document.getElementById('productTable');
    let row = table.insertRow();
    row.insertCell(0).innerHTML = title;
    row.insertCell(1).innerHTML = description;
    row.insertCell(2).innerHTML = price;
    let img = new Image();
    img.src = image;
    row.insertCell(3).appendChild(img);
    let button = document.createElement('button');
    button.innerHTML = 'Add to Cart';
    button.id = id;
    row.insertCell(4).appendChild(button);
    // button.addEventListener('click', addToCart);  // We'll add this later
    button = document.createElement('button');
    button.innerHTML = 'Delete';
    button.id = id;
    button.className = 'deleteButton'
    row.insertCell(5).appendChild(button);
    // button.addEventListener('click', deleteProduct);  // We'll add this later
}

async function fillProductTable() {
    let response = await fetch('http://127.0.0.1:5000/products');
    let products = await response.json();
    for (let product of products) { addProduct(...product) }
}

window.addEventListener('load', fillProductTable);
