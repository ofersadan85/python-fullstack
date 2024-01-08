"use strict";

let password = document.getElementById("password");
let password2 = document.getElementById("password2");
let password_error = document.getElementById("password_error");
let username = document.getElementById("username-box");
let username_error = document.getElementById("username_error");
let registerButton = document.querySelector("#register input[type=submit]");

function checkPasswordsMatch() {
  if (password.value !== password2.value) {
    password2.style.backgroundColor = "red";
    password_error.innerHTML = "Passwords do not match";
    registerButton.disabled = true;
  } else {
    password2.removeAttribute("style");
    password_error.innerHTML = "";
    registerButton.disabled = false;
  }
}

async function checkUsernameExists() {
  fetch("/auth/user_exists?username=" + username.value)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.user_exists) {
        username.style.backgroundColor = "red";
        username_error.innerHTML = "Username already exists";
        registerButton.disabled = true;
      } else {
        username.removeAttribute("style");
        username_error.innerHTML = "";
        registerButton.disabled = false;
      }
    });
}

async function checkUsernameExistsAsync() {
  let response = await fetch("/auth/user_exists?username=" + username.value);
  let data = await response.json();
  if (data.user_exists) {
    username.style.backgroundColor = "red";
    username_error.innerHTML = "Username already exists";
    registerButton.disabled = true;
  } else {
    username.removeAttribute("style");
    username_error.innerHTML = "";
    registerButton.disabled = false;
  }
}

password2.addEventListener("input", checkPasswordsMatch);
username.addEventListener("focusout", checkUsernameExists);
// username.addEventListener("focusout", checkUsernameExistsAsync);
