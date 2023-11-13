# Advanced Python Function Arguments Guide

Understanding how to use different types of arguments in Python functions can greatly enhance the flexibility and clarity of your code. Here's a brief overview of the various advanced argument types:

## Positional Arguments

Positional arguments are arguments that need to be included in the proper position or order. They are the most common kind of Python function arguments.

**Example:**

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet('John', 'Smith')
```

## Default Arguments

Default arguments are specified in a function definition and assume a default value if no argument value is passed during the function call.

**Example:**

```python
def greet(first_name, last_name, middle_name=""):
    print(f"Hello, {first_name} {middle_name} {last_name}!")

greet('Jane', 'Doe')
greet('John', 'Smith', 'Edward')
```

**Note:** Default arguments must be specified after positional arguments in the function definition.

```python
def greet(first_name, last_name="", middle_name):  # Will cause a SyntaxError
    print(f"Hello, {first_name} {middle_name} {last_name}!")
```

## Keyword Arguments

Keyword arguments are related to the function calls. By using keyword arguments, you can specify which parameter you want to assign a value to in a function call.

**Example:**

```python
def greet(first_name, last_name, middle_name=""):
    print(f"Hello, {first_name} {middle_name} {last_name}!")

greet(first_name="Jane", last_name="Doe")
```

Once again, keyword arguments must be specified after positional arguments in the function call.

```python
greet(last_name="Doe", "Jane")  # SyntaxError, positional argument follows keyword argument
```

## *args

The `*args` parameter allows the function to accept an arbitrary number of positional arguments. It's like a tuple of arguments passed to the function. The word `args` is just a convention (short for "arguments"), and you can use any valid variable name. The important part is the `*` before the variable name, which tells Python to collect all positional arguments into a tuple.

**Example:**

```python
def add_numbers(*args):
    return sum(args)

add_numbers(1, 2, 3, 4, 5)  # Returns 15
add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Returns 55
```

## **kwargs

The **kwargs parameter allows the function to accept an arbitrary number of keyword arguments. This is used when you want to handle named arguments that you have not defined in advance. Like `*args`, the name `kwargs` is just a convention (short for "keyword arguments"), and you can use any valid variable name. The important part is the `**` before the variable name, which tells Python to collect all keyword arguments into a dictionary (`dict`).

**Example:**

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Jane', age=25, title='Engineer')
```

## Combining *args and **kwargs

You can use *args and **kwargs in the same function to handle a flexible number of arguments.

**Example:**

```python
def setup_profile(name, email, *args, **kwargs):
    print(f"Name: {name}, Email: {email}")
    print("Favorite Languages:")
    for language in args:
        print(language)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## Usage Examples

```python
# Using positional arguments
greet('John', 'Smith')

# Using default arguments
greet('John', 'Smith', 'Edward')

# Using keyword arguments
greet(last_name='Doe', first_name='Jane')

# Using *args
add_numbers(1, 2, 3, 4, 5)

# Using **kwargs
print_info(title='Software Engineer', location='New York')

# Combining *args and **kwargs
setup_profile('Jane', 'jane@example.com', 'Python', 'JavaScript', title='Engineer', age=25)
```

## Common Mistakes

In addition to understanding how to use various types of function arguments correctly, it's equally important to be aware of common mistakes that can occur when defining or using Python functions. Below are some counter-examples and explanations of what does not work.

## Positional Arguments After Default Arguments

As mentioned above, you cannot place positional arguments after default arguments in the function definition. Doing so will result in a `SyntaxError`.

**Incorrect Example:**

```python
def greet(first_name, last_name="", middle_name):  # Will cause a SyntaxError
    print(f"Hello, {first_name} {middle_name} {last_name}!")
```

## Mixing Positional and Keyword Arguments

When calling a function, if you begin using keyword arguments, all subsequent arguments must also be keyword arguments.

**Incorrect Call:**

```python
greet(first_name="Jane", "Doe")  # SyntaxError, positional argument follows keyword argument
```

Correct usage would be to maintain the order by not mixing positional arguments after keyword arguments.

**Correct Call:**

```python
greet("Jane", last_name="Doe")  # Correct, as all positional arguments come first
```

## Overriding Default Arguments

Providing a value for a default argument when it is not needed can lead to unexpected behavior, not an error, but it's essential to use them correctly.

**Incorrect Assumption:**

```python
def greet(first_name, last_name, middle_name=""):
    print(f"Hello, {first_name} {middle_name} {last_name}!")

greet('Jane', 'Smith', 'Doe')  # Incorrectly assumes 'Doe' as middle name instead of last name
```

In this case, 'Doe' will be treated as the middle name, not the last name, because of the position it's given in the function call.

## Misusing `*args` and `**kwargs`

Using `*args` or `**kwargs` incorrectly can lead to various errors, from `TypeError` to `SyntaxError`.

**Incorrect Definition:**

```python
def add_numbers(args):  # Missing the * for args
    return sum(args)
```

**Incorrect Call:**

```python
print_info(name='Jane', 'Doe')  # SyntaxError, non-keyword arg after a keyword arg
```

**Mixing up *args and **kwargs:**

```python
def print_info(*kwargs):  # Should be **kwargs to collect keyword arguments as a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

**Correct Use of `*args:`**

```python
def add_numbers(*args):  # Correct definition with *args
    return sum(args)

add_numbers(1, 2, 3, 4)  # Correct usage
```

**Correct Use of **kwargs:**

```python
def print_info(**kwargs):  # Correct definition with **kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(title='Engineer', department='Software')  # Correct usage
```

Understanding these pitfalls will help you debug your Python code more effectively and write functions that are both robust and versatile.

## Complex Function Example

We can mix and match all of the above argument types to create a function that can handle a wide variety of inputs, as long as we follow the correct order and usage. Let's define a function called `something_complex` to demonstrate the use of mixed argument types. Here's the correct definition and a call that uses all the possibilities:

## Function Definition

```python
def something_complex(a, b, *args, c=1, d=2, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print("args:", args)
    print(f"c: {c}")
    print(f"d: {d}")
    print("kwargs:", kwargs)
```

## Function Call

```python
something(10, 20, 30, 40, 50, c=3, d=4, e=5, f=6)
```

In the above call:

- `10` and `20` are passed as positional arguments to `a` and `b`, respectively.
- `30`, `40`, and `50` are additional positional arguments that get collected into `args` as a tuple.
- `c` and `d` are specified with new values `3` and `4`, overriding their default values of `1` and `2`.
- `e=5` and `f=6` are keyword arguments that are not predefined in the function signature and get collected into `kwargs`.

By the end of the function call, the following will be printed:

> a: 10
> b: 20
> args: (30, 40, 50)
> c: 3
> d: 4
> kwargs: {'e': 5, 'f': 6}

Alternatively, we could call the function fewer arguments, as long as we follow the correct order and usage:

```python
something(10, 20)
```

In this case, the following will be printed:

> a: 10
> b: 20
> args: ()
> c: 1
> d: 2
> kwargs: {}

**Incorrect Call:**

```python
# This will raise an error because after using a keyword argument, all subsequent arguments must also be keyword arguments.
something(10, b=20, 30, c=3, d=4, e=5, f=6)  # Causes an error: SyntaxError: positional argument follows keyword argument
```

## Unpacking Arguments

Outside of function definitions, you can also use `*` and `**` to unpack arguments from a list or dictionary into a function call.

**Example:**

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

names = ['Jane', 'Doe']
greet(*names)  # Unpacks the list into positional arguments
```

In this case, the function call is equivalent to `greet('Jane', 'Doe')`. It is important to note that the number of elements in the list must match the number of positional arguments in the function definition, and they must be in the correct order. For example:

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

names = ['Jane', 'Doe', 'Edward']  # This list has 3 elements, but the function only accepts 2 positional arguments
greet(*names)  # Raises an error: TypeError: greet() takes 2 positional arguments but 3 were given
```

Similarly, you can unpack a dictionary into keyword arguments:

```python
def print_info(name, age, title):
    print(f"Name: {name}, Age: {age}, Title: {title}")

person = {'name': 'Jane', 'age': 25, 'title': 'Engineer'}
print_info(**person)  # Unpacks the dictionary into keyword arguments
```

In this case, the function call is equivalent to `print_info(name='Jane', age=25, title='Engineer')`. It is important to note that the keys in the dictionary must match the keyword arguments in the function definition. For example:

```python
def print_info(name, age, title):
    print(f"Name: {name}, Age: {age}, Title: {title}")

person = {'name': 'Jane', 'age': 25, 'job_title': 'Engineer'}  # This dictionary has a key 'job_title', but the function only accepts 'title'
print_info(**person)  # Raises an error: TypeError: print_info() got an unexpected keyword argument 'job_title'
```

## Common patterns

The most common pattern with `*args` and `**kwargs` is to pass them along to another function. This is useful when you want to create a wrapper function that adds some additional functionality to an existing function.

**Example:**

```python
def add_numbers(*args):
    return sum(args)

def add_numbers_with_message(*args):
    result = add_numbers(*args)
    print(f"The sum of {args} is {result}")
    return result
```

In this case, `add_numbers_with_message` is a wrapper function that calls `add_numbers` and adds some additional functionality. It accepts an arbitrary number of positional arguments, passes them along to `add_numbers`, and then prints a message with the result.

Another very common example is when doing class inheritance. You can use `*args` and `**kwargs` to pass arguments to the parent class.

**Example:**

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, breed, *args, **kwargs):
        super().__init__(*args, **kwargs)  # name and age are passed to the Animal class
        self.breed = breed
```

We can even "inject" additional arguments into the `*args` and `**kwargs` that are passed to the parent class, or remove arguments that are not needed.

**Example:**

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, breed, *args, **kwargs):
        kwargs["name"] = 'Rover'  # Adds a name argument to the kwargs dictionary
        if "age" not in kwargs.keys():  # Checks if age is not already in kwargs
            kwargs["age"] = 0  # Adds an age argument to the kwargs dictionary, essentially setting a default value
        super().__init__(*args, **kwargs)
        self.breed = breed
```
