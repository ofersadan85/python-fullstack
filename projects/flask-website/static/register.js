"use strict";

let registerButton = document.querySelector("#register input[type=submit]");

function checkPasswordsMatch() {
  let password = document.getElementById("password");
  let password2 = document.getElementById("password2");
  let error = document.getElementById("password_error");
  if (password.value !== password2.value) {
    password2.style.backgroundColor = "red";
    error.innerHTML = "Passwords do not match";
    registerButton.disabled = true;
  } else {
    password2.removeAttribute("style");
    error.innerHTML = "";
    registerButton.disabled = false;
  }
}

function checkUsername() {
  let username = document.getElementById("username");
  let error = document.getElementById("username_error");
  if (username.value.length < 4) {
    username.style.backgroundColor = "red";
    error.innerHTML = "Username must be at least 4 characters";
    registerButton.disabled = true;
  } else {
    username.removeAttribute("style");
    error.innerHTML = "";
    registerButton.disabled = false;
  }
}

async function checkUsernameExists() {
  let username = document.getElementById("username");
  let error = document.getElementById("username_error");
  fetch("/auth/user_exists?username=" + username.value)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.user_exists) {
        username.style.backgroundColor = "red";
        error.innerHTML = "Username already exists";
        registerButton.disabled = true;
      } else {
        username.removeAttribute("style");
        error.innerHTML = "";
        registerButton.disabled = false;
      }
    });
}

async function checkUsernameExistsAsync() {
  let username = document.getElementById("username");
  let error = document.getElementById("username_error");
  let response = await fetch("/auth/user_exists?username=" + username.value);
  let data = await response.json();
  console.log(data);
  if (data.user_exists) {
    username.style.backgroundColor = "red";
    error.innerHTML = "Username already exists";
    registerButton.disabled = true;
  } else {
    username.removeAttribute("style");
    error.innerHTML = "";
    registerButton.disabled = false;
  }
}

document.getElementById("username").addEventListener("keyup", checkUsername);
document
  .getElementById("username")
  .addEventListener("focusout", checkUsernameExists);
// document
//   .getElementById("username")
//   .addEventListener("focusout", checkUsernameExistsAsync);
document
  .getElementById("password2")
  .addEventListener("keyup", checkPasswordsMatch);
