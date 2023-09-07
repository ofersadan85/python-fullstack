# Built-in Data Types (Collections)

Collections are data types that can hold multiple values. There are 4 built-in collection data types in Python:

- `tuple`
- `list`
- `set`
- `dict` (Which we will cover in the next section)
- `str` (Which is a [primitive data type](./types-primitive.md), but it's also a collection data type)

## Tuple

Tuples are ordered, immutable (unchangeable) collections of data. They are defined by using round brackets `()` and separating the values with a comma `,`. For example:

```python
x = (1, 2, 3)
y = ("a", "b", "c")
z = (1, "a", 2, "b", 3, "c")
```

We can access the values in a `tuple` by using the index of the value (index starts at 0). For example:

```python
x = (1, 2, 3)
print(x[0])  # 1
```

But we can't change the values in a `tuple`, for example:

```python
x = (1, 2, 3)
x[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## List

Lists are ordered, mutable (changeable) collections of data. They are defined by using square brackets `[]` and separating the values with a comma `,`. For example:

```python
x = [1, 2, 3]
y = ["a", "b", "c"]
z = [1, "a", 2, "b", 3, "c"]
```

We can access the values in a `list` by using the index of the value (index starts at 0). For example:

```python
x = [1, 2, 3]
print(x[0])  # 1
```

But unlike `tuple` we can change the values in a `list`, for example:

```python
x = [1, 2, 3]
x[0] = 10
print(x)  # [10, 2, 3]
```

And we can add or remove values from a `list` as well, for example:

```python
x = [1, 2, 3]
x.append(4)  # append always adds the value to the end of the list
print(x)  # [1, 2, 3, 4]
x.remove(2)  # remove removes the first occurrence of the value
print(x)  # [1, 3, 4]
```

## Set

Sets are unordered, mutable (changeable) collections of data. They are defined by using curly brackets `{}` and separating the values with a comma `,`. For example:

```python
x = {1, 2, 3}
y = {"a", "b", "c"}
z = {1, "a", 2, "b", 3, "c"}
```

Unlike `list` or `tuple` (which are ordered) we can't access the values in a `set` by using the index of the value, for example:

```python
x = {1, 2, 3}
x[0]  # TypeError: 'set' object is not subscriptable
```

But we _can_ change the values in a `set`, for example:

```python
x = {1, 2, 3}
x.add(4)
print(x)  # {1, 2, 3, 4}
x.remove(2)
print(x)  # {1, 3, 4}
```

The main feature of `set` as a collection is that it can't contain duplicate values, for example:

```python
x = {1, 2, 3, 3, 3, 3, 3}
print(x)  # {1, 2, 3}
x.add(1)
print(x)  # {1, 2, 3}
```

## String

Strings are considered both primitive and collection data types. They are ordered, immutable (unchangeable) collections of data. They are most similar to `tuple` in that regard, because we can access the values in a `string` by using the index of the value (index starts at 0), but we can't change the values in a `string`, for example:

```python
x = "Hello World"
print(x[0])  # H
x[0] = "h"  # TypeError: 'str' object does not support item assignment
```

## Converting between data types

We can use the keywords `tuple()`, `list()`, `set()` to convert between data types, for example:

```python
x = (1, 2, 3)
print(x)  # (1, 2, 3)
print(type(x))  # <class 'tuple'>
y = list(x)
print(y)  # [1, 2, 3]
print(type(y))  # <class 'list'>
z = set(y)
print(z)  # {1, 2, 3}
print(type(z))  # <class 'set'>
```

But because `str` is also a collection data type, we can convert it to `tuple`, `list` or `set` as well, for example:

```python
x = "Hello World"
print(x)  # Hello World
print(type(x))  # <class 'str'>
y = tuple(x)
print(y)  # ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(type(y))  # <class 'tuple'>
z = list(x)
print(z)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(type(z))  # <class 'list'>
w = set(x)
print(w)  # {'H', 'o', 'r', 'l', ' ', 'W', 'e', 'd'}
print(type(w))  # <class 'set'>
```

Notice that when we convert a `str` to `tuple` or `list` we get a collection of characters, but when we convert it to `set` we get a collection of __unique__ characters (because `set` can't contain duplicate values).

## Common operations

We can use the `len()` function to get the length of a collection, for example:

```python
x = (1, 2, 3)
print(len(x))  # 3
y = [1, 2, 3]
print(len(y))  # 3
z = {1, 2, 3}
print(len(z))  # 3
w = "Hello World"
print(len(w))  # 11
```

We can use the `in` keyword to check if a value exists in a collection, for example:

```python
x = (1, 2, 3)
print(1 in x)  # True
print(4 in x)  # False
y = [1, 2, 3]
print(1 in y)  # True
print(4 in y)  # False
z = {1, 2, 3}
print(1 in z)  # True
print(4 in z)  # False
w = "Hello World"
print("Hello" in w)  # True
print("hello" in w)  # False
```

We can use `max()` and `min()` to get the maximum and minimum values in a collection, for example:

```python
x = (1, 2, 3)
print(max(x))  # 3
print(min(x))  # 1
```

Note that `max()` and `min()` only work with collections that contain values of the same type, for example:

```python
x = (1, "a", 2, "b", 3, "c")
print(max(x))  # TypeError: '>' not supported between instances of 'str' and 'int'
```

But note that when using `max()` and `min()` with `str` it will compare the characters based on their [ASCII](https://en.wikipedia.org/wiki/ASCII) values, for example:

```python
x = "Hello World"
print(max(x))  # r
print(min(x))  #  (space)
```

We can use `sum()` to get the sum of all the values in a collection, for example:

```python
x = (1, 2, 3)
print(sum(x))  # 6
```

But obviously `sum()` only works with collections that contain numbers (`int` or `float`), for example:

```python
x = [1, 2, 3.5]
print(sum(x))  # 6.5
y = {"a", "b", "c"}
print(sum(y))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
