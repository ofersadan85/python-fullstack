# Decorators - Wrapping Functions

Imagine we have a function that we want to wrap with some additional functionality. Some common examples are:

- Logging the function call and/or its return value or arguments
- Measuring the time it takes to run the function
- Caching the function's return value for future calls
- Checking the function's arguments for validity
- And many more...

## The problem

In our example, let's assume we want to time the function's execution. We could do this by adding a few lines of code to the function itself:

```python
from datetime import datetime
from time import sleep
from random import randint

def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    sleep(randint(1, 5))

def timed_random_sleep():
    """Sleeps for a random number of seconds between 1 and 5, and prints the time it took"""
    start = datetime.now()
    random_sleep()
    end = datetime.now()
    print(f"Function took {end - start} seconds to run")
```

However, this is not ideal. We would have to add this code to every function we want to time, and it would make the function less readable.

## The solution - Wrapping functions

Instead, if our new function takes another function as an argument, we can wrap it with our new functionality:

```python
from datetime import datetime
from time import sleep
from random import randint

def timed(func):
    """Wraps a function and prints the time it took to run"""
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
    return wrapper

def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    sleep(randint(1, 5))

timed_random_sleep = timed(random_sleep)
```

Now, we can call `timed_random_sleep()` and it will print the time it took to run `random_sleep()`. Additionally, we can wrap any other function with the `timed()` decorator, and it will print the time it took to run that function as well.

However, imagine we would like to change the existing function, instead of creating a new one. We could do this by reassigning the function's name to the wrapped function:

```python
random_sleep = timed(random_sleep)
```

This is better because we don't have to search for all the places where the function is called and change them. However, it's still not ideal. We would have to do this for every function we want to wrap, and it would make our code less readable. Instead, we can use the `@` syntax to wrap the function:

```python
@timed  # This is equivalent to: `random_sleep = timed(random_sleep)`
def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    sleep(randint(1, 5))
```

In effect, this is the same as the previous example, but it's much more readable, and can be applied to any function we want to wrap.

## Wrapping functions with arguments

Our previous example will only work for functions that don't take any arguments. What if we want to wrap a function that takes arguments? We can do this by using `*args` and `**kwargs`, to match whatever arguments the original function takes:

```python
from datetime import datetime
from time import sleep
from random import randint

def timed(func):
    """Wraps a function and prints the time it took to run"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
    return wrapper

@timed
def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    sleep(randint(1, 5))
```

## Wrapping functions with return values

Our previous example will only work for functions that don't return any values. What if we want to wrap a function that returns a value? We can do this by returning the value from the wrapper function:

```python
from datetime import datetime
from time import sleep
from random import randint

def timed(func):
    """Wraps a function and prints the time it took to run"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
        return result
    return wrapper

@timed
def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    seconds = randint(1, 5)
    sleep(seconds)
    return seconds

seconds = random_sleep()
print(f"Slept for {seconds} seconds")
```

## Function metadata

When we wrap a function, we lose some of the metadata of the original function. For example, if we try to print the docstring of the wrapped function, we will get the docstring of the wrapper function instead. We may also lose the function's name, the function's arguments types, and other metadata. We can fix this by using the `functools.wraps()` decorator:

```python
from datetime import datetime
from time import sleep
from random import randint
from functools import wraps

def timed(func):
    """Wraps a function and prints the time it took to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
        return result
    return wrapper

@timed
def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    seconds = randint(1, 5)
    sleep(seconds)
    return seconds

seconds = random_sleep()
print(f"Slept for {seconds} seconds")
```

Basically, `functools.wraps()` copies the metadata from the original function to the wrapper function. Of course, we can also do this manually, but it's much more convenient to use `functools.wraps()`. `functools.wraps()` is a decorator and a wrapper, just like the ones we wrote ourselves - it takes a function as an argument, and returns a function, for the purpose of modifying the original function in some way.

## `functools` - A module for working with functions

In this context, `functools` is a module that contains functions for working with functions. It contains the `wraps()` function we used in the previous example, as well as other useful functions, wrappers and decorators. For example, `functools.cache()` is a decorator that caches the return value of a function, so that if the function is called again with the same arguments, it will return the cached value instead of running the function again. This can be useful if the function is expensive to run, and we want to avoid running it multiple times with the same arguments.

```python
from functools import cache
from time import sleep

@cache
def expensive_function(seconds):
    """Sleeps for the given number of seconds, and returns the number of seconds"""
    sleep(seconds)
    return seconds

seconds = expensive_function(5)
print(f"Function took {seconds} seconds to run")
seconds = expensive_function(5)
print(f"Function took {seconds} seconds to run")  # What's printed here is a lie
```

Notice that the second time we call `expensive_function(5)`, it returns immediately, without sleeping for 5 seconds. This is because the return value was cached from the first time we called the function. Despite that, we still get the same return value. This is useful for when the function's return value is deterministic - that is, it always returns the same value for the same arguments.

Since this is difficult to demonstrate, we can use our previous example of `timed` wrapping to wrap the same function twice, once with `timed` and once with `cache`:

```python
from datetime import datetime
from time import sleep
from random import randint
from functools import wraps, cache

def timed(func):
    """Wraps a function and prints the time it took to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
        return result
    return wrapper

@timed
@cache
def random_sleep():
    """Sleeps for a random number of seconds between 1 and 5"""
    seconds = randint(1, 5)
    sleep(seconds)
    return seconds

seconds = random_sleep()  # Prints: Function random_sleep took 0:00:05.00 seconds to run
print(f"Slept for {seconds} seconds")  # Prints: Slept for 5 seconds
seconds = random_sleep()  # Prints: Function random_sleep took 0:00:00.000001 seconds to run
print(f"Slept for {seconds} seconds")  # What's printed here is a lie
```

There are many more useful functions in the `functools` module, and you can read about them in the [official documentation](https://docs.python.org/3/library/functools.html).

## Class decorators

So far, we've only seen function decorators. However, we can also use decorators on classes. This is useful for when we want to wrap all the methods of a class with some functionality. For example, we can use a class decorator to wrap all the methods of a class with the `timed` decorator we wrote earlier:

```python
from datetime import datetime
from time import sleep
from random import randint
from functools import wraps

def timed(func):
    """Wraps a function and prints the time it took to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"Function {func.__name__} took {end - start} seconds to run")
        return result
    return wrapper

def timed_class(cls):
    """Wraps all the methods of a class with the timed decorator"""
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, timed(method))
    return cls

@timed_class
class RandomSleep:
    """A class that sleeps for a random number of seconds between 1 and 5"""
    def __init__(self):
        self.seconds = randint(1, 5)

    def sleep(self):
        """Sleeps for the number of seconds given in the constructor"""
        sleep(self.seconds)

random_sleep = RandomSleep()  # Prints: Function __init__ took 0:00:00 seconds to run
random_sleep.sleep()  # Prints: Function sleep took 0:00:05.00 seconds to run
```

This is just an example, but it can be useful for when we want to wrap all the methods of a class with some functionality. Some more useful examples include wrapping the individual methods with `@property`, `@staticmethod` or `@classmethod`, or wrapping the entire class with `@dataclass`. We can also use class decorators to create "metaclasses", which is a more advanced topic that we won't cover here.

For more information about `@property`, `@staticmethod`, `@classmethod` and `@dataclass`, see the [Advanced classes](./classes-02.md) section.
