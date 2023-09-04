# Built-in Primitive Data Types

There are many data types in Python, some of them we can create, but some are already built in for us in the language. We will start with the most basic ones (also called primitive data types).

## Integers

Integers are whole numbers, positive or negative. For example: 2, 4, 10, 100, -5, -1000. The type of these numbers is `int`.

```python
x = 10
y = -5
print(x)  # 10
print(type(x))  # <class 'int'>
print(y)  # -5
print(type(y))  # <class 'int'>
```

We can do calculations with integers, for example:

```python
print(2 + 2)  # 4
print(10 - 5)  # 5
print(10 * 5)  # 50
print(10 / 5)  # 2.0  NOTE: THIS BECOMES A DIFFERENT TYPE (float)
print(10 // 5)  # 2
print(13 % 4)  # 1
print(2 ** 3)  # 8
```

## Floating point numbers

Floating point numbers are numbers with a decimal point. For example: 2.5, 3.14, 10.0, -5.0, -1000.0. The type of these numbers is `float`.

```python
x = 10.2
y = -5.0
print(x)  # 10.2
print(type(x))  # <class 'float'>
print(y)  # -5.0
print(type(y))  # <class 'float'>
```

We can do calculations with floating point numbers as well, for example:

```python
print(2.5 + 2.5)  # 5.0
print(10.0 - 5.0)  # 5.0
print(10.0 * 5.0)  # 50.0
print(10.0 / 5.0)  # 2.0
print(10.0 // 5.0)  # 2.0
print(13.0 % 4.0)  # 1.0
print(2.0 ** 3.0)  # 8.0
```

But it's worth noting that when we do calculations with a mix of `int` and `float` numbers. In that case the result will **ALWAYS** be a `float` type value. For example:

```python
print(2 + 2.5)  # 4.5
print(10 - 5.0)  # 5.0
print(10 * 5.0)  # 50.0
print(10 / 5.0)  # 2.0
print(10 // 5.0)  # 2.0
print(13 % 4.0)  # 1.0
print(2 ** 3.0)  # 8.0
```

## Strings

Strings are used to store text. They are created by surrounding text with single or double quotes. For example: "Hello World", 'Hello World', "Hello 123", 'Hello 123'. The type of these values is `str`.

```python
x = "Hello World"
y = 'Hello World'
print(x)  # Hello World
print(type(x))  # <class 'str'>
print(y)  # Hello World
print(type(y))  # <class 'str'>
```

We can do some operations with strings, for example:

```python
print("Hello" + "World")  # HelloWorld
print("Hello" + " " + "World")  # Hello World
print("hello".upper())  # HELLO
print("HELLO".lower())  # hello
```

In most cases we can't preform operations between strings and numbers, for example:

```python
print("Hello" + "123")  # Hello123
print("Hello" + 123)  # TypeError: can only concatenate str (not "int") to str
```

But that's not always true, for example:

```python
print("Hello" * 3)  # HelloHelloHello
```

## Booleans

Booleans are used to represent `True` or `False` values. The type of these values is `bool`. They have only two possible values, which is very different from the previous types that can have an infinite number of values. So by definition, a boolean that isn't `True` must be `False`, and a boolean that isn't `False` must be `True`.

```python
x = True
y = False
print(x)  # True
print(type(x))  # <class 'bool'>
print(y)  # False
print(type(y))  # <class 'bool'>
```

Behind the scenes, booleans are actually integers. `True` is equal to `1` and `False` is equal to `0`. We can see this by using the `int()` function to convert them to integers:

```python
print(int(True))  # 1
print(int(False))  # 0
```

We can also convert numbers to booleans. Any integer that isn't `0` will be converted to `True`, and `0` (or `0.0`) will be converted to `False`:

```python
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(1))  # True
print(bool(-2))  # True
print(bool(3.2))  # True
```

We can also convert strings to booleans. Any string that isn't empty will be converted to `True`, and an empty string will be converted to `False`:

```python
print(bool(""))  # False
print(bool("Hello"))  # True
print(bool("False"))  # True
```

## Converting between types

We can convert between types using the following functions (which are the type names), but this is not _always_ possible:

```python
print(int(3.14))  # 3  NOTE: THIS WILL ALWAYS ROUND DOWN
print(int("3"))  # 3
print(int("3.14"))  # ValueError: invalid literal for int() with base 10: '3.14'
print(int("Hello"))  # ValueError: invalid literal for int() with base 10: 'Hello'
print(int(True))  # 1
print(int(False))  # 0
print(float(3))  # 3.0
print(float("3"))  # 3.0
print(float("3.14"))  # 3.14
print(float("Hello"))  # ValueError: could not convert string to float: 'Hello'
print(float(True))  # 1.0
print(float(False))  # 0.0
```

## None

None is a special value that represents **nothing**. It is used to indicate that a variable doesn't have a value. The type of this value is `NoneType`. We will see this value a lot later on. This is unique because this `NoneType` is the only type that has only one value (`None`).

> **Warning**
> `None` is not the same as `False`. `None` is a value that represents nothing, while `False` is a boolean value that represents a false value.

### To be continued

> **Important**
> This chapter about `None` isn't complete. This will be expanded when we learn about it in class.
