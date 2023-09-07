# Conditions

Conditions are our method to run code only based on certain criteria. For that, we use the `if` statement. Inside the `if` statement, we have an expression that will **always** be evaluated to either `True` or `False`. If the expression is `True`, the code inside the `if` statement will run, otherwise it will be skipped.

```python
if True:
    print("This will always run")

if False:
    print("This will never run")
```

We can also use variables inside the `if` statement:

```python
x = True
if x:
    print("This will always run")
```

But it's much more useful to use expressions that are not always `True` or `False`. For example, we can use the `in` keyword to check if a value exists in a collection:

```python
x = 1
if x in (1, 2, 3):
    print("This will run if x is 1, 2 or 3")

if x in (4, 5, 6):
    print("This will run if x is 4, 5 or 6")
```

## `else`

Optionally, we might run some code only if the expression is `False`. For that, we use the `else` keyword.

```python
x = 1
if x in (1, 2, 3):
    print("This will run if x is 1, 2 or 3")
else:
    print("This will run if x is not 1, 2 or 3")

print("This will always run, because it's not part of the if code block or the else code block")
```

## Chaining conditions

We can also chain conditions together using the `and` and `or` keywords. For example:

```python
x = 1
y = 2
my_tuple = (1, 2, 3)
if x in my_tuple and y in my_tuple:
    print("This will run if x and y are both 1, 2 or 3")
else:
    print("This will run if x or y is not 1, 2 or 3")
    print("NOTE: x and y might still be 1, 2 or 3, but we only care if they are ***both*** 1, 2 or 3, because we used the `and` keyword")

if x in my_tuple or y in my_tuple:
    print("This will run if x or y is 1, 2 or 3")
    print("NOTE: because we used `or`, we don't know which of x or y is 1, 2 or 3, or if both are 1, 2 or 3")
else:
    print("This will run if x and y is not 1, 2 or 3")
```

## Nested conditions

Inside code blocks for `if` and `else`, we can use any valid Python code, including other `if` statements. For example:

```python
x = 1
y = 2
my_tuple = (1, 2, 3)
if x in my_tuple:
    print("This will run if x is 1, 2 or 3")
    if y in my_tuple:
        print("This will run if x ***and*** y are both 1, 2 or 3")
    else:
        print("This will run if x is 1, 2 or 3, but y is not 1, 2 or 3")
else:
    print("This will run if x is not 1, 2 or 3, but it doesn't even check what y is")
```

## Comparison operators

We can use the following comparison operators to create expressions that evaluate to `True` or `False`:

```python
x = 1
y = 2
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x < y)  # Less than
print(x <= y)  # Less than or equal to
print(x > y)  # Greater than
print(x >= y)  # Greater than or equal to
```

Because these expressions evaluate to `True` or `False`, we can use them inside `if` statements:

```python
x = 1
y = 2
z = 3
if x < y:
    print("This will run if x is less than y")

if x < y and z == 3:
    print("This will run if x is less than y ***and*** z is equal to 3")
```

## `elif`

We will cover this in more detail later, but we can also use the `elif` keyword to check for more conditions, in that case, the `else` block will run only if none of the conditions are `True`. For example:

```python
x = 1
y = 2
if x < y:
    print("This will run if x is less than y")
elif x > y:
    print("This will run if x is greater than y")
else:
    print("This will run if x is not less than y or greater than y (they are probably equal)")
```
