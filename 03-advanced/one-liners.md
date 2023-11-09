# One-liners

Python is known for its conciseness and readability. One-liners are a great way to write concise code that is easy to read. In this section, we'll look at some examples of one-liners and how they can be used to make your code shorter and more readable.

Primarily, we'll look at:

1. [List Comprehensions](#list-comprehension)
2. [Ternary If Statements](#ternary-if)
3. Lambda Functions (will be added later)
4. Generator Expressions (will be added later)

## List Comprehension

Here is a common pattern in Python:

```python
squares = []
for x in range(10):
    squares.append(x**2)
```

The above code can be read as a series of steps:

> 1. Create an empty list
> 2. Loop through a range of numbers
> 3. Square each number
> 4. Append the squared number to the list

But just like in English, it's also true to say:

> Create a list of squared numbers from 0 to 9

This is exactly what list comprehensions do. They allow you to create a list from a range of values in a single line of code.

```python
squares = [x**2 for x in range(10)]
```

### Filtering list comprehensions

It is also quite common to filter a list based on some condition. For example, if we wanted to create a list of even numbers from 0 to 9, we could do the following:

```python
odds = []
for x in range(10):
    if x % 2 != 0:
        odds.append(x)
```

One-liner "list comprehensions" can also be used to filter a list based on some condition. The syntax is similar to a for loop, but with an additional if statement at the end.

```python
odds = [x for x in range(10) if x % 2 != 0]
```

## Ternary If

Ternary if statements are a way to write if-else statements in a single line of code. They are useful for simple conditions with clear outcomes. For example, if we wanted to check if a number is even or odd, we could do the following:

```python
if x % 2 == 0:
    result = "Even"
else:
    result = "Odd"
```

The above code can be read as a series of steps:

> 1. Check if the number is even
> 2. If it is, assign the string "Even" to a variable named `result`
> 3. If it isn't, assign the string "Odd" to a variable named `result`

Note that in both cases, we are assigning a value to a variable, so no matter what `x` is, `result` will always be assigned a value. This is a good use case for ternary if statements. We can rewrite this task in one English sentence:
> If x is an even number, result should be "Even", otherwise result should be "Odd".

This is exactly what "ternary if statements" do. They allow you to write if-else statements in a single line of code.

```python
result = "Even" if x % 2 == 0 else "Odd"
```

Once again, `result` will always be assigned a value.

### Nested Ternary If

Is also possible to nest ternary if statements in one line. For example, if we wanted to check if a number is zero, positive, or negative, we could do the following:

```python
result = "zero" if x == 0 else "positive" if x > 0 else "negative"
```

This is equivalent to the following code:

```python
if x == 0:
    result = "zero"
else:
    if x > 0:
        result = "positive"
    else:
        result = "negative"
```

## When to Use One-liners

While one-liners can make your code shorter, they can sometimes make your code harder to read, especially for those not familiar with the syntax. It's essential to strike a balance between conciseness and readability. Use list comprehensions for simple operations or filtering and map operations. For more complex operations, such as those involving nested loops or multiple conditions, a regular for loop might be more readable.

For ternary if statements, they are best used when you have a simple condition with clear outcomes. When dealing with multiple conditions that require nested ternary operators, it can become less clear and should be replaced with normal if-else statements for the sake of readability.

Ultimately, it's up to you to decide when to use one-liners. The most important thing is to write code that is easy to read and understand (for others, and for yourself in the future!)
