# JavaScript - Basics

This is a very short introduction to JavaScript. It is not meant to be a complete guide, but rather a quick overview of the basics, mainly for Python developers.

## Variables

Variables in JavaScript are declared using the `let` keyword. The syntax is very similar to Python, but there are some differences.

```javascript
let x = 5;
let y = 10;
let z = x + y;
```

JavaScript is a dynamically typed language, so you don't need to specify the type of the variable. The type is inferred from the value.

```javascript
let x = 5; // x is a number
let y = "10"; // y is a string
let z = x + y; // z is a string
```

## If-else

The syntax for if-else statements is very similar to Python, but there are some differences.

```javascript
let x = 5;
if (x > 10) {
    console.log("x is greater than 10");
} else if (x > 5) {
    console.log("x is greater than 5");
} else {
    console.log("x is less than or equal to 5");
}
```

The main difference is the use of parentheses `()` around the condition, and the curly braces `{}` around the code block. Unlike Python, JavaScript does not use indentation to define code blocks.

## Functions

Functions in JavaScript are declared using the `function` keyword. The syntax is very similar to Python, but again, code blocks are defined using curly braces `{}`.

```javascript
function add(x, y) {
    return x + y;
}
```

## Arguments in functions

Differently from Python, JavaScript will allow you to call a function with any number of arguments, regardless of the number of arguments defined in the function.

```javascript
function print(a, b) {
    console.log(a);
    console.log(b);
}

print(); // undefined, undefined
print(1); // 1, undefined
print(1, 2); // 1, 2
print(1, 2, 3); // 1, 2
```

## Undefined vs. null

In JavaScript, `undefined` is a value that means "no value". It is different from `null`, which is a value that means "nothing". This can be confusing, because in Python, `None` is used for both cases. Another way to think of the difference is that `undefined` means "not defined", while `null` means "defined, but empty".

```javascript
let x; // x was "declared" but its value is yet undefined
let y = null; // y's IS defined, it's value is null
```

## Arrays

Arrays are very similar to Python lists:

```javascript
let x = [1, 2, 3];
console.log(x[0]); // 1
console.log(x[1]); // 2
console.log(x[2]); // 3
```

Getting the length of an array is done using the `length` property:

```javascript
let x = [1, 2, 3];
console.log(x.length); // 3
```

## Objects

Objects are very similar to Python dictionaries (`dict`):

```javascript
let x = {
    "name": "John",
    "age": 30
};
console.log(x["name"]); // John
console.log(x["age"]); // 30
```

However, JavaScript allows you to access the values using the dot notation:

```javascript
let x = {
    "name": "John",
    "age": 30
};
console.log(x.name); // John
console.log(x.age); // 30
```

## Loops

### While loop

The syntax for while loops is very similar to Python (but again, code blocks are defined using curly braces `{}`, and conditions are wrapped in `()`).

```javascript
let x = 0;
while (x < 10) {
    console.log(x);
    x++;
}
```

`x++` is a shorthand for `x = x + 1`. This can also be written as `x += 1`.

### For loop

A for loop is just a shorthand for a while loop. The following two code snippets are equivalent:

```javascript
let x = 0;
while (x < 10) {
    console.log(x);
    x++;
}
```

```javascript
for (let x = 0; x < 10; x++) {
    console.log(x);
}
```

Notice that in both, we create an index variable `x` with a starting value of `0`, and increment it by `1` in each iteration, while the condition is `x < 10`.

### For...of loop

A for...of loop is used to iterate over the values of an array. It is similar to Python's `for item in item_list` loop.

```javascript
let x = [1, 2, 3];
for (let item of x) {
    console.log(item);
}
```

This is basically the same as:

```javascript
let x = [1, 2, 3];
for (let i = 0; i < x.length; i++) {
    console.log(x[i]);
}
```

Except usually shorter and easier to read and write. This is the preferred way of iterating over or generators in JavaScript.

## Resources

This guide is very short and incomplete. For a more complete guide, check out the [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide). It's also recommended to check out the [MDN JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) for a complete reference of all JavaScript features.

[W3Schools](https://www.w3schools.com/js/default.asp) also has a good JavaScript tutorial, but it's not as complete as the MDN guide. This is also recommended for a quick overview of the basics, or as a quick "cheat sheet" for the syntax or different features and operations.
