# Generators in Python

Generators are a powerful feature in Python, allowing efficient and concise creation of iterators. They are particularly useful for processing large data sets or for implementing stream-like data flows.

## Comprehensions vs. Generators

### Comprehensions

Comprehensions provide a concise way to create lists, dicts and sets. They are written within square brackets and can include conditions.

- List comprehension Syntax: `[expression for item in iterable]`
- List comprehension with condition: `[expression for item in iterable if condition]`
- Example: `even_squares = [x**2 for x in range(10) if x % 2 == 0]`
- Set comprehension Syntax: `{expression for item in iterable}`
- Set comprehension with condition: `{expression for item in iterable if condition}`
- Example: `even_squares = {x**2 for x in range(10) if x % 2 == 0}`
- Dict comprehension Syntax: `{key_expression: value_expression for item in iterable}`
- Dict comprehension with condition: `{key_expression: value_expression for item in iterable if condition}`
- Example: `even_squares = {x: x**2 for x in range(10) if x % 2 == 0}`

### Generator Expressions

Generator expressions are similar to list comprehensions but use parentheses and can also include conditions. They are more memory-efficient as they generate items on the fly. This means that they do not store the entire list in memory, but rather generate each item as needed.

- Syntax: `(expression for item in iterable)`
- Syntax with condition: `(expression for item in iterable if condition)`
- Example: `even_squares = (x**2 for x in range(10) if x % 2 == 0)`

```python
list_comp = [x**2 for x in range(10) if x % 2 == 0]
print(list_comp) # [0, 4, 16, 36, 64]
gen_exp = (x**2 for x in range(10) if x % 2 == 0)
print(gen_exp) # <generator object <genexpr> at 0x7f9b1c1b3f20>
```

Note: Despite the use of parentheses (`()`), generator expressions are not tuples and do not create tuples. They are simply a way to create generators. The also do not support indexing or slicing.

```python
gen_exp = (x**2 for x in range(10) if x % 2 == 0)
print(gen_exp[0]) # raises TypeError: 'generator' object is not subscriptable
```

### Key Differences

- **Memory Usage**: Generators are more memory-efficient, as they do not store the entire list in memory. In fact, each item is generated on the fly and the previous item is discarded (unless you have saved it elsewhere).
- **Use Case**: Use comprehensions to create a data collection **now**, and store it for future use(s). Use generators for computing one item at a time, **on demand**.

## Using `next()`

You can manually iterate over a generator using the `next()` function. This retrieves the next value from the generator.

- Syntax: `next(generator)`

### Handling `StopIteration`

When a generator exhausts its data, it raises a `StopIteration` exception. This indicates that there are no more values to generate. This also means that the generator can no longer be iterated over, as it has been "exhausted".

- Example:

```python
gen = (x * x for x in range(10, 13))
next(gen) # returns 100
next(gen) # returns 121
next(gen) # returns 144
next(gen) # raises StopIteration exception
```

If we wanted to handle the `StopIteration` exception, we could use a `try...except` block:

```python
gen = (x * x for x in range(10, 13))
try:
    while True:
        print(next(gen))
except StopIteration:
    print("No more values")
```

Which makes it equivalent to this `for` loop:

```python
gen = (x * x for x in range(10, 13))
for item in gen:
    print(item)

print("No more values")
```

In fact, that's exactly what a `for` loop does: it calls `next()` on the generator until it raises `StopIteration`.

### Mitigation Strategies

There will be times when you want to iterate over a generator multiple times. However, once a generator is exhausted, it cannot be iterated over again. There are a few ways to mitigate this:

- **Recreating Generators**: You can create a new generator instance if you need to iterate again.
- **Caching Values**: If the dataset is not too large, you can convert the generator into a list or another iterable structure.
- **itertools.cycle()**: This function creates an infinite iterator that cycles through the values of the given iterable. This can be used to iterate over a generator multiple times.

### Example (Recreating Generators)

```python
def get_data():
    return (x for x in range(5))

# First iteration
for item in get_data():
    print(item)

# Recreate and iterate again
for item in get_data():
    print(item)
```

### Example (Caching Values)

```python
# Convert to list
gen = (x for x in range(5))
data = list(gen)  # [0, 1, 2, 3, 4]

# First iteration
for item in data:
    print(item)

# Iterate again
for item in data:
    print(item)
```

### Example (itertools.cycle())

```python
import itertools
gen = (x for x in range(3))
infinite_gen = itertools.cycle(gen)
print(next(infinite_gen)) # 0
print(next(infinite_gen)) # 1
print(next(infinite_gen)) # 2
print(next(infinite_gen)) # 0
print(next(infinite_gen)) # 1
print(next(infinite_gen)) # 2
```

## Generator Functions and `yield`

A generator function is a function that returns a generator. It uses the `yield` statement instead of `return`.

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```

The return value of this function is **not** `1`, `2` or `3`. Rather, it is a generator object. This object can be iterated over, yielding values one at a time, the same way as a generator expression. It also raises `StopIteration` when it is exhausted.

```python
gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # raises StopIteration
```

### Understanding `yield`

When we call `next` on a generator, produced from a generator function, the function is executed until it reaches a `yield` statement. The yielded value is returned to the caller, and the function's state is preserved. The next time `next` is called, the function resumes execution from the point it left off, until it reaches another `yield` statement. In other words, we can think of `yield` as breakpoints in the function, to be continued from that point later.

```python
def my_generator():
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3
    print("End of function")

gen = my_generator()  # Nothing is printed
result = next(gen)  # Prints "First yield", result = 1
result = next(gen)  # Prints "Second yield", result = 2
result = next(gen)  # Prints "Third yield", result = 3
result = next(gen)  # Prints "End of function", raises StopIteration
```

## Infinite Generators

One of the most common pattern is to use a `while` loop to repeatedly `yield` values. This allows the generator to produce an infinite stream of values.

```python
import random
def create_password_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        yield "".join(random.choices(alphabet, k=8))

password_generator = create_password_generator()
print(next(password_generator))
print(next(password_generator))
```

Again, we must read this function as if it is executed only when `next` is called on its return value (which is a generator), and pauses on each `yield` statement.

## Arguments to generator functions

Since functions the have `yield` are normal functions that return a generator, they can take arguments like any other function. These arguments can be used to control the behavior of the generator. For example, we can try and recreate (some) of the functionality of `range()`:

```python
def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start = start + step

normal_range = range(10, 20, 2)
our_range = my_range(10, 20, 2)
print(list(normal_range)) # [10, 12, 14, 16, 18]
print(list(our_range)) # [10, 12, 14, 16, 18]
```
