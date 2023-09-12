# Functions

Functions in Python are logical blocks of code that can be called from other parts of the code. Functions are used to make code more readable and to avoid repeating code.

## Defining a function

A function is defined using the `def` keyword. The function name is followed by a set of parentheses and a colon. The function body is indented.

```python
def my_function():
    print("Hello from my_function")
```

## Calling a function

A function is called by using its name followed by a set of parentheses.

```python
my_function()
```

## Parameters

A function can take parameters. Parameters are defined inside the parentheses when defining the function. When calling the function, the parameters are passed inside the parentheses.

```python
def my_function(name):
    print("Hello " + name)

my_function("John")
```

A function can take multiple parameters. The parameters are separated by commas.

```python
def my_function(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

my_function("John", "Doe")
```

## Return values

A function can return a value. The value is returned using the `return` keyword.

```python
def my_function(name):
    return "Hello " + name

greeting = my_function("John")
print(greeting)
```

> **Note:** A function can return only one value. If you need to return multiple values, you can return a tuple or any other data type that can hold multiple values.

## Function's without a return value

A function can be defined without a return value. In this case, the function body does not contain a `return` statement.

```python
def my_function(name):
    print("Hello " + name)

my_function("John")
```

But if we do try to assign the result of the function to a variable, the variable will be assigned the value `None`.

```python
def my_function(name):
    print("Hello " + name)

greeting = my_function("John")
print(greeting)
```

In other words, these two functions are equivalent:

```python
def my_function1(name):
    print("Hello " + name)

def my_function2(name):
    print("Hello " + name)
    return None 
```
