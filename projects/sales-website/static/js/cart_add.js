function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

async function addToUserCart(productID) {
  console.log("User is logged in with user_id:");
  let response = await fetch("/add_to_cart/" + productID);
  if (response.status == 200) {
    console.log("Added to cart " + productID);
  } else {
    console.log("Failed to add to cart " + productID);
  }
}

function addToCookieCart(productID) {
  let cart_string = getCookie("cart") == "" ? "{}" : getCookie("cart");
  let cart = JSON.parse(cart_string);
  cart[productID] = cart[productID] === undefined ? 1 : cart[productID] + 1;
  cart_string = JSON.stringify(cart);
  document.cookie = "cart=" + cart_string;
}

async function addToCart(event) {
  let button = event.target;
  addToCookieCart(button.id);
  addToUserCart(button.id);
}
