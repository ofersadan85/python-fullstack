# Hello World

```python
print("Hello World!")
```

Output:
> Hello World!

Words, characters, text are called ***strings***.
They must be surrounded with single quotes ( ' ) or double quotes ( " ). They can be joined together with the + (plus) operator:

```python
print("Hello" + "World!")
```

Output:
> HelloWorld!

Notice: The space between the two words is missing. We did not include it! We can add it like this:

```python
print("Hello" + " " + "World!")
```

Or like this:

```python
print("Hello " + "World!")
#           ^ Here is the space
```

Output:
> Hello World!

We can also print numbers!

```python
print(1)
print(123)
```

But numbers behave differently than strings. This is called a ***data type***. We'll talk more about data types later. For example:

```python
print(1 + 1)
```

Output:
> 2

```python
print("1" + "1")
```

Output:
> 11

Trying to add a number to a string will result in an error:

```python
print(1 + "1")
```

Output:
> TypeError: unsupported operand type(s) for +: 'int' and 'str'

We can view the type of any object using the `type()` function:

```python
print(type(1))
```

Output:
> <class 'int'>

```python
print(type("1"))
```

Output:
> <class 'str'>

As we can see, a data type of "number" in Python is called `int` (short for integer) and a data type of "string" is called `str` (short for string).
