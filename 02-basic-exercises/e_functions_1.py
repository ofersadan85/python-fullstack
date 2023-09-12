## Simple functions exercises

# 1. Define a function named `is_two`.
# It should accept one input and return `True` if the passed input is either the number or the string `2`, `False` otherwise.
def is_two(x):
    ...  # Your solution here
    
# 2. Define a function named that prints a greeting to a user, accepting a name parameter.
# Example: `say_hello("Jane")` prints `"Hello, Jane!"`
def say_hello(name):
    ...  # Your solution here
    
# 3. Define a function that accepts a string argument in this format: 3+4. Your function should return the result (7) as an integer.
def add_numbers(string):
    ...  # Your solution here
    
# 4. What does this function do? What does it return? Rewrite the function with a better name.
def do_something(x):
    return x * x

# 5. What is the difference between the previous function and this one?
def do_something(x):
    print(x * x)

# 6. Write a function that accepts two arguments: a string and a letter.
# The function should count the number of occurrences of that letter in the string.
# Example: `count_letter("banana", "a")` should return `3`.
def count_letter(string, letter):
    ...  # Your solution here

# What does this code do? What is the value of `result`?
def do_something(x):
    x = x + 1

result = do_something(4)    
