# Dictionary (dict) collection

Dictionaries are unordered, mutable (changeable) collections of data. They are defined by using curly brackets `{}` and separating the key-value pairs with a comma `,`. The type in Python is called `dict`. For example:

```python
x = {"name": "John", "age": 36}
print(x)  # {'name': 'John', 'age': 36}
print(type(x))  # <class 'dict'>
```

We can access the values in a `dict` by using the key of the value, for example:

```python
x = {"name": "John", "age": 36}
print(x["name"])  # John
```

We can change the values in a `dict`, for example:

```python
x = {"name": "John", "age": 36}
x["age"] = 40
print(x)  # {'name': 'John', 'age': 40}
```

But we can't add or remove values from a `dict` by using the index of the value, for example:

```python
x = {"name": "John", "age": 36}
x[0] = 40  # TypeError: 'dict' object does not support item assignment
```

We can add or remove values from a `dict` by using the key of the value, for example:

```python
x = {"name": "John", "age": 36}
x["city"] = "Oslo"
print(x)  # {'name': 'John', 'age': 36, 'city': 'Oslo'}
x.pop("age")
print(x)  # {'name': 'John', 'city': 'Oslo'}
```

## Keys

The keys in a `dict` must be unique, somewhat similar to a `set`. If we try to add a key that already exists, the value will be overwritten, for example:

```python
x = {"name": "John", "age": 36}
x["age"] = 40
print(x)  # {'name': 'John', 'age': 40}
```

Trying to access a key that doesn't exist will result in a `KeyError`, for example:

```python
x = {"name": "John", "age": 36}
print(x["city"])  # KeyError: 'city'
```

We can use the `in` keyword to check if a key exists in a `dict`, for example:

```python
x = {"name": "John", "age": 36}
print("name" in x)  # True
print("city" in x)  # False
```

And we can get all the keys in a `dict` by using the `keys()` method, for example:

```python
x = {"name": "John", "age": 36}
print(x.keys())  # dict_keys(['name', 'age'])
```

But when iterating (looping) over a `dict` we will get the keys by default, for example:

```python
x = {"name": "John", "age": 36}
for key in x:
    print(key)
# name
# age
```

> Note: The keys in a `dict` are unordered, so the order of the keys may change when iterating over a `dict`.

### Types of keys

The keys in a `dict` can be any **immutable** data type, for example, `str`, `int`, `tuple`, but not `list` or `set`, for example:

```python
x = {"name": "John", "age": 36}
print(x)  # {'name': 'John', 'age': 36}
x[1] = "Hello"
print(x)  # {'name': 'John', 'age': 36, 1: 'Hello'}
x[(1, 2, 3)] = "World"
print(x)  # {'name': 'John', 'age': 36, 1: 'Hello', (1, 2, 3): 'World'}
x[[1, 2, 3]] = "World"  # TypeError: unhashable type: 'list'
```

## Values

The values in a `dict` can be **any** data type, for example, even another `dict`, for example:

```python
x = {"name": "John", "age": 36, "info": {"city": "Oslo", "country": "Norway"}}
print(x)  # {'name': 'John', 'age': 36, 'info': {'city': 'Oslo', 'country': 'Norway'}}
```

We can access the values in a `dict` by using the key of the value, for example:

```python
x = {"name": "John", "age": 36}
print(x["name"])  # John
```

But we can't do the reverse, we can't access the key of a value, for example:

```python
x = {"name": "John", "age": 36}
print(x["John"])  # KeyError: 'John'
```

We can get all the values in a `dict` by using the `values()` method, for example:

```python
x = {"name": "John", "age": 36}
print(x.values())  # dict_values(['John', 36])
```

## Items

We can get all the key-value pairs in a `dict` by using the `items()` method, for example:

```python
x = {"name": "John", "age": 36}
print(x.items())  # dict_items([('name', 'John'), ('age', 36)])
```

Sometimes, it will be useful to iterate (loop) over the key-value pairs in a `dict`, for example:

```python
x = {"name": "John", "age": 36}
for key, value in x.items():
    print(key, value)
# name John
# age 36
```

## Useful methods

| Method | Description | Example |
| --- | --- | --- |
| `clear()` | Removes all the elements from the dictionary | `x.clear()` |
| `copy()` | Returns a copy of the dictionary | `x.copy()` |
| `get()` | Returns the value of the specified key, if it exists, otherwise `None` or another default value | `x.get("name", "anonymous")` |
| `pop()` | Removes the element with the specified key (and returns its value) |  `name = x.pop("name")` |
| `update()` | Updates the dictionary with the specified key-value pairs | `x.update({"name": "John", "age": 36})` |
