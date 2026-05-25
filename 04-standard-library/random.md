# Python `random` module - basic examples

The `random` module helps generate pseudo-random values.

## 1. Random float between 0 and 1

```python
import random

value = random.random()
print(value)  # e.g. 0.734582193
```

## 2. Random integer in a range

```python
import random

number = random.randint(1, 10)
print(number)  # 1..10 (inclusive)
```

## 3. Random choice from a list

```python
import random

colors = ["red", "green", "blue"]
picked = random.choice(colors)
print(picked)
```

> [!NOTE]
> `random.choice()` does not modify the original list, therefore it can repeat the same item multiple times if called in a loop. If you want to pick unique items, consider using `random.sample()` or `random.shuffle()`.

## 4. Shuffle a list in place

```python
import random

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)
```

## 5. Pick multiple unique items

```python
import random

numbers = [1, 2, 3, 4, 5, 6]
picked = random.sample(numbers, 3)
print(picked)  # 3 unique values
```

## 6. Reproducible randomness with seed

Setting a seed allows you to get the same sequence of random numbers each time you run the code, which is useful for testing and debugging.

```python
import random

random.seed(42)
x = random.randint(1, 100)
print(x)
```
