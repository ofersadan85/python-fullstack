# `pytest` - Unit testing in Python

Unit testing is a way of testing your code in small chunks. The idea is to test each function in your code to make sure it works as expected. This is especially useful when you are working on a large project with many functions and classes. If you make a change to one function, you can run the tests to make sure you didn't break anything else. Of course, we are not really limited to testing single functions. We can also test classes, or even entire programs.

## `unittest` vs `pytest`

While Python has a built-in module for unit testing called `unittest`, we will be using a third-party module called `pytest`. The reason for this is that `pytest` is much easier to use and has a lot of useful features. It is also the most popular unit testing module for Python. You can read more about `unittest` [here](https://docs.python.org/3/library/unittest.html) and `pytest` [here](https://docs.pytest.org/en/latest/).

## Installing `pytest`

To install `pytest`, run one the following commands in your terminal (depending on your operating system)

```bash
pip install pytest  # Will work on most systems
pip3 install pytest  # Linux and Mac
python -m pip install pytest  # Windows
py -m pip install pytest  # Windows
```

To make sure `pytest` is installed, run `pytest` in your terminal. You should see something like this:

```bash
==================== test session starts ====================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\youruser\
plugins: anyio-4.0.0
collected 0 items

=================== no tests ran in 0.11s =================== 
```

What `pytest` is doing here is looking for files that start with `test_` or end with `_test` and running them as tests. Since we don't have any tests yet, it doesn't find anything.

## Writing your first test

Let's write a simple function and test it. Create two files called `my_math.py` and `test_my_math.py`. In `my_math.py`, write the following function:

```python
def add(a, b):
    return 4
```

The other file, `test_my_math.py`, will contain our tests. The name of the file is important. It must start with `test_` or end with `_test`. In this file, we will import our function and write a test for it. The test function must also start with `test_`. Here is the code for `test_my_math.py`:

```python
from my_math import add

def test_add():
    assert add(1, 2) == 3
```

The `assert` keyword is used to check if something (the condition that follows it) is true. If it is, the test passes. If it isn't, the test fails. In this case, we are checking if `add(1, 2)` is equal to `3`. If it is, the test passes. If it isn't, the test fails.

`assert` is just a shortcut for an `if` statement that raises an error, in this case, `AssertionError`. The code above is the same as this:

```python
if add(1, 2) != 3:
    raise AssertionError
```

In fact, any error raised inside a test will cause the test to fail, not just `AssertionError`.

## Running the test

To run the test, simply run `pytest` in your terminal. You should see something like this:

```bash
==================== test session starts ====================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\youruser\yourproject
plugins: anyio-4.0.0
collected 1 item

test_my_math.py F                                      [100%]

========================= FAILURES ==========================
_________________________ test_add __________________________

    def test_add():
>       assert add(1, 2) == 3
E       assert 4 == 3
E        +  where 4 = add(1, 2)

test_my_math.py:4: AssertionError
=================== 1 failed in 0.12s =================== 
```

We can see that the test failed. This is because `add(1, 2)` returns `4`, not `3`. In fact, it will always return `4`, no matter what arguments we pass to it. Let's fix that. Change the function to this:

```python
def add(a, b):
    return a + b
```

Now let's run the test again:

```bash
==================== test session starts ====================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\Users\youruser\yourproject
plugins: anyio-4.0.0
collected 1 item

test_my_math.py .                                      [100%]

==================== 1 passed in 0.12s ==================== 
```

Without manually checking the output of `add(1, 2)`, we can be sure that it works as expected. This is especially useful when you are working on a large project with many functions and classes. If you make a change to one function, you can run the tests to make sure you didn't break anything else, without manually checking every function or testing every possible input.

## Fixtures

A fixture is a function that runs before each test. It can be used to set up the environment for the test. For example, if you are testing a function that reads from a file, you can use a fixture to create the file before each test. Here is an example:

```python
import pytest

@pytest.fixture
def my_fixture():
    print("Running fixture")
    return 42

def test_fixture1(my_fixture):
    print("Running test1")

def test_fixture2(my_fixture):
    print("Running test2")
```

The `@pytest.fixture` decorator tells `pytest` that this function is a fixture. The fixture function can take arguments, just like a test function. In this case, we are not using any arguments, but we will see how to use them later. The fixture function can return a value, which will be passed to the test function. In this case, we are returning `42`, which will be passed to the test function as `my_fixture`. The test function can then use this value. In this case, we are checking if `my_fixture` is equal to `42`.

`pytest` usually hides the output of print statements, but if you run the test with the `-s` flag, it will show the output. Try running the test with and without the `-s` flag to see the difference.

Example output:

```bash
test_math.py Running fixture
Running test1
.Running fixture
Running test2
.
```

What we see here is that "Running fixture" is printed twice, once before each test. But what if we want to also run something **after** each test? For that, we can use the `yield` keyword. Here is an example:

```python
import pytest

@pytest.fixture
def my_fixture():
    print("Running fixture start")
    yield 42
    print("Running fixture end")

def test_fixture1(my_fixture):
    print("Running test1")

def test_fixture2(my_fixture):
    print("Running test2")
```

The output of this test is:

```bash
test_math.py Running fixture start
Running test1
.Running fixture end
Running fixture start
Running test2
.Running fixture end
```

So a "fixture" is a way to prepare how "the world" looks like before each test. It can be used to set up the environment for the test, or pass common parameters. For example, if you are testing a function that reads from a file, you can use a fixture to create the file before each test, removing it after the test, and passing the file name to the test function. Such a fixture might look like this:

```python
import os
import pytest

@pytest.fixture
def my_fixture():
    file_name = "test_file.txt"
    with open(file_name, "w") as f:
        f.write("Hello world")
    yield file_name
    os.remove(file_name)
```

## Parametrized tests

Sometimes you want to run the same test with different parameters. You can do it as several test functions, or as several `assert` statements in the same test function.

```python
def add(a, b):
    if a == 0 or b == 0:
        return 0  # This is wrong, but we will use it for the example of locating the error
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(0, 3) == 3  # This will fail
    assert add(2, 3) == 5
    assert add(1.5, 2.5) == 4
    assert add(2.5, 3.5) == 6
```

The case where one of the arguments is `0` fails, but because they are all in the same test function, the other tests running after it aren't executed. We can fix this by putting each test in a separate function, but that is a lot of code duplication.

 But `pytest` has a better way to do it. You can use the `@pytest.mark.parametrize` decorator to run the same test with different parameters. Here is an example:

```python
import pytest

def add(a, b):
    if a == 0 or b == 0:
        return 0  # This is wrong, but we will use it for the example of locating the error
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 3, 3),
    (2, 3, 5),
    (1.5, 2.5, 4),
    (2.5, 3.5, 6),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

We are telling `pytest` here to take the names (`a`, `b`, `expected`) and values (`1`, `2`, `3`) from the list and pass them to the test function. The test function will be called once for each set of values. Even though we have only one test function, the output of this test is:

> 1 failed, 4 passed in 0.12s

So it has correctly located that there are 5 different cases and ran them all. The first case fails, but the other 4 are not prevented from running, and pass.

Let's fix the `add` function so that it passes all the tests:

```python
def add(a, b):
    return a + b
```

Without touching the test function, we can now run the test again and see that it passes. This time,let's run it with `pytest -v` to see the output of each test:

```bash
test_math.py::test_add[1-2-3] PASSED                     [ 20%] 
test_math.py::test_add[0-3-3] PASSED                     [ 40%] 
test_math.py::test_add[2-3-5] PASSED                     [ 60%] 
test_math.py::test_add[1.5-2.5-4] PASSED                 [ 80%]
test_math.py::test_add[2.5-3.5-6] PASSED                 [100%] 
========== 5 passed in 0.12s ==========
```

## Test driven development (TDD)

Test driven development is just a different approach to writing code. It can sometimes be useful to think of the outcome you want first, and then write the code to make it happen. For example, let's say we want to write a function that takes a list of numbers and returns the sum of all the numbers in the list. We can start by writing a test for it:

```python
def test_sum():
    assert sum_function([1, 2, 3]) == 6
```

Even though we haven't written the function yet, we can run the test and see that it fails. Now we can write the function:

```python
def sum_function(numbers):
    return 6
```

Now we can run the test again and see that it passes. But we know that this function is wrong. It will always return `6`, no matter what list we pass to it. So let's fix it:

```python
def sum_function(numbers):
    return sum(numbers)
```

Now we can run the test again and see that it passes. This is of course a very simple example, but it can be useful when you don't want to start working on a function without knowing what it should output.

## Conclusion

There are many more subjects to cover in unit testing, but this should be enough to get you started. You can read more about `pytest` [here](https://docs.pytest.org/en/latest/).

Testing your code is important! It prevents you from breaking applications that are already working, and it makes it easier to find bugs when you do break something. It also makes it easier ans safer to automate processes, since you can be sure that the code works as expected before you are updating it in a real environment.
