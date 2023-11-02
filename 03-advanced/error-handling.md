# Error handling - `try...except` in Python

In Python, errors are called "Exceptions". `try...except` is used for exception handling, which allows developers to handle errors (exceptions) gracefully without crashing the entire program.

## Table of Contents

1. [Basic Syntax](#basic-syntax)
2. [Handling Multiple Exceptions](#handling-multiple-exceptions)
3. [The `else` Clause](#the-else-clause)
4. [The `finally` Clause](#the-finally-clause)
5. [Raising Exceptions](#raising-exceptions)
6. [Examples](#examples)
7. [Bare `except`](#bare-except)
8. [Conclusion](#conclusion)

## Basic Syntax

The basic syntax for `try...except` in Python is as follows:

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
```

Example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

In this example, when trying to divide by zero, a `ZeroDivisionError` is raised. The `except` block catches this error and prints a message.

## Handling Multiple Exceptions

You can handle multiple exceptions by using multiple `except` blocks:

```python
try:
    # Some code
except ZeroDivisionError:
    # Handle division by zero
except IndexError:
    # Handle index out of range
```

## The `else` Clause

The `else` clause in a `try...except` statement is executed if no exceptions are raised:

```python
try:
    # Code that might raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("No exceptions were raised!")
```

## The `finally` Clause

The `finally` clause is always executed, whether an exception was raised or not:

```python
try:
    # Some code
except ZeroDivisionError:
    # Handle division by zero
finally:
    print("This code will always run!")
```

## Raising Exceptions

You can raise exceptions using the `raise` keyword:

```python
x = -1

if x < 0:
    raise ValueError("x cannot be negative!")
```

## Examples

### 1. Basic Error Handling

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

This example is useful for checking if a user's input can be converted to an integer. If the user enters a string, the `int()` function will raise a `ValueError`, which is caught by the `except` block. This is somewhat similar to using `if...else` to check if the input is a number, but using `try...except` is more robust and allows you to handle the error more gracefully.

### 2. Multiple Exceptions

```python
list_numbers = [1, 2, 3]

try:
    index = int(input("Enter an index: "))
    print(list_numbers[index])
except ValueError:
    print("Please enter a valid integer!")
except IndexError:
    print("Index out of range!")
```

In this example, the user is asked to enter an index. If the input is not a valid integer, a `ValueError` is raised. If the input is a valid integer, but the index is out of range, an `IndexError` is raised. Both exceptions are handled by separate `except` blocks.

### 3. Using `else` and `finally` together

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered {number}.")
finally:
    print("Execution finished!")
```

## Bare `except`

```python
list_numbers = [1, 2, 3]

try:
    index = int(input("Enter an index: "))
    print(list_numbers[index])
except:
    print("Something went wrong, but we don't know what it was!")
```

While this example is valid Python code, it is not recommended to use bare `except` blocks (i.e `except` without a specific error type). This is because it will catch all exceptions, and you will lose all knowledge of what went wrong. Did the user enter a wrong index or did he enter letters? We'll never know. It is better to catch specific exceptions and handle them accordingly.

## Conclusion

`try...except` in Python provides a robust way to handle exceptions and ensures that your application doesn't crash unexpectedly due to runtime errors. By understanding and effectively using this feature, you can create resilient and user-friendly programs.
