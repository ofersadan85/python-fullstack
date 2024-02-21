"use strict";

let password = document.getElementById("password");
let password2 = document.getElementById("password2");
let password_error = document.getElementById("password_error");
let username = document.getElementById("username-box");
let username_error = document.getElementById("username_error");
let registerButton = document.querySelector("#register input[type=submit]");

let buttonState = {
    _usernameAvailable: true,
    get usernameAvailable() { return this._usernameAvailable },
    set usernameAvailable(value) {
        this._usernameAvailable = value;
        this.decideAboutButton();
    },

    _passwordsMatch: true,
    get passwordsMatch() { return this._passwordsMatch },
    set passwordsMatch(value) {
        this._passwordsMatch = value;
        this.decideAboutButton();
    },

    decideAboutButton: function() {
        if (buttonState.passwordsMatch && buttonState.usernameAvailable) {
            registerButton.disabled = false;
        } else {
            registerButton.disabled = true;
        }
    }
}


function checkPasswordsMatch() {
  if (password.value !== password2.value) {
    password2.style.backgroundColor = "red";
    password_error.innerHTML = "Passwords do not match";
    buttonState.passwordsMatch = false;
  } else {
    password2.removeAttribute("style");
    password_error.innerHTML = "";
    buttonState.passwordsMatch = true;
  }
}

async function checkUsernameExistsAsync() {
  let response = await fetch("/auth/user_exists?username=" + username.value);
  let data = await response.json();
  if (data.user_exists) {
    username.style.backgroundColor = "red";
    username_error.innerHTML = "Username already exists";
    buttonState.usernameAvailable = false;
  } else {
    username.removeAttribute("style");
    username_error.innerHTML = "";
    buttonState.usernameAvailable = true;
  }
}


password2.addEventListener("input", checkPasswordsMatch);
username.addEventListener("focusout", checkUsernameExistsAsync);
