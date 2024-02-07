async function addToCart(event) {
    let button = event.target;
    let response = await fetch("/add_to_cart/" + button.id)
    if (response.status == 200) {
        console.log("Added to cart " + button.id);
    } else {
        console.log("Failed to add to cart " + button.id);
    }
}