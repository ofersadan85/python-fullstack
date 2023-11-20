# Parallel Processing in Python

Up until now, we've been writing code that runs in a single thread. This means that the code is executed in a single sequence, one line at a time. This is fine for some applications, but sometimes we want to run multiple tasks at the same time. This is where parallel processing comes in.

The main methods of parallel processing in Python are:

1. `threading` - Running multiple threads in parallel
2. `multiprocessing` - Running multiple processes in parallel
3. `asyncio` (`async` and `await`) - Running multiple tasks in parallel

We'll discuss the differences between these methods later. Using generator functions, we can simulate parallel processing behavior. Let's look at an example:

```python
from time import sleep
from datetime import datetime, timedelta
import random

def task(name, seconds):
    start_time = datetime.now()
    while start_time + timedelta(seconds=seconds) > datetime.now():
        print(f"Task {name} is working...")
        time.sleep(0.3)  # Simulate work being done
        yield None  # Yield control, indicating the task is not done
    result = random.randint(10000, 20000)
    print(f"Task {name} completed with result: {result}")
    yield result  # Yield the final result

def event_loop(tasks):
    results = {}
    while tasks:
        for task in tasks.copy():
            try:
                result = next(task)
                if result is not None:
                    tasks.remove(task)
                    results[task] = result
            except StopIteration:
                tasks.remove(task)
    return results

# Creating tasks
task1 = task("A", 2)
task2 = task("B", 3)

# Starting the event loop with the tasks
results = event_loop([task1, task2])

# Display the results
print("All tasks completed. Results:", results)
```

In this example, we are using `yield` to repeatedly return control to the event loop. We have seen that when `next` is called on a generator, it stops at every `yield` but remembers where it was so it can continue later. The event loop then checks if the task is done, and if so, removes it from the list of tasks. When all tasks are done, the event loop returns the results. In effect, this is a very simple form of parallel processing, but one that isn't very useful in practice.

## Using threads

Python has a built-in module called `threading` that allows us to run multiple threads in parallel. Let's look at an example:

```python
import threading
from time import sleep

def task(name, seconds):
    print(f"Task {name} started")
    sleep(seconds)
    print(f"Task {name} completed")

# Creating threads
thread1 = threading.Thread(target=task, args=("A", 2))
thread2 = threading.Thread(target=task, args=("B", 3))

print("Starting threads")
thread1.start()
thread2.start()
print("Threads started")
```

In this example, we are creating two threads, each running the `task` function. We then start the threads, and the program continues. The threads will run in parallel, and the program will exit when all threads are done. Notice that the output `Threads started` is printed before the tasks are completed. This is because the threads are running in parallel, and the program (the main thread) continues while the threads are running.

If we wish to wait for the threads to finish, we can use the `join` method:

```python
import threading
from time import sleep

def task(name, seconds):
    print(f"Task {name} started")
    sleep(seconds)
    print(f"Task {name} completed")

# Creating threads
thread1 = threading.Thread(target=task, args=("A", 2))
thread2 = threading.Thread(target=task, args=("B", 3))

print("Starting threads")
thread1.start()
thread2.start()
print("Threads started")
thread1.join()
thread2.join()
print("Threads finished")
```

### Sharing data between threads

When running multiple threads, we often want to share data between them. Naively, we might try to do this by using global variables:

```python
import threading

value = 0

def task():
    global value
    for i in range(1000000):
        plus_one = value + 1
        value = plus_one

threads = []
for i in range(10):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Value: {value}")  # Expected: 10000000, Actual: ?
```

While this code might work, it is not "thread-safe" and unpredictable. This means that the result might be different every time we run the program. This is because the threads are running in parallel, and the order in which they are executed is not guaranteed. This means that one thread might read the value before another thread has written to it, resulting in the value being incremented only once instead of multiple times.

To solve this problem, we can use a `Lock` object:

```python
import threading

value = 0
value_lock = threading.Lock()

def task():
    global value
    for i in range(1000000):
        with value_lock:  # This will block other identical threads from running
            plus_one = value + 1
            value = plus_one
```

The `Lock` object is used to prevent multiple threads from accessing the same resource at the same time. When a thread acquires a lock, other threads that try to acquire the same lock will be blocked (paused) until the lock is released. This ensures that only one thread can access the resource at a time.

### Queues

Another common way to share data between threads is by using a `Queue`. A `Queue` is a data structure that allows us to add items to the end of the queue, and remove items from the front of the queue. This is called a "first in, first out" (FIFO) data structure.  We'll discuss queues in more detail in a later chapter, but for now, let's look at an example:

```python
import threading
import queue

q = queue.Queue()

def task():
    for i in range(10):
        q.put(i)  # Add item to queue

threads = []
for i in range(10):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

while not q.empty():
    print(q.get())  # Remove item from queue and print it
```

A `Queue` is thread-safe, meaning that it can be used by multiple threads at the same time without causing any problems. This is because the `Queue` object uses a `Lock` internally to prevent multiple threads from accessing the queue at the same time. In other words, it is guaranteed that when one thread is adding or removing an item to the queue, no other thread can add or remove items from the queue at the exact same time. Since each thread in our example adds 10 items to the queue, and there are 10 such threads, we know that the queue will contain 100 items when all threads are done (note that we still might not know the exact order of the items in the queue).

## Using multiprocessing

Python has a built-in module called `multiprocessing` that allows us to run multiple processes in parallel. Since we will not be using `multiprocessing` in our course, we will not go into more detail about it. However, if you are interested, you can read more about it in the [official documentation](https://docs.python.org/3/library/multiprocessing.html). Let's just look at a small example:

```python
import multiprocessing
from time import sleep

def task(name, seconds):
    print(f"Task {name} started")
    sleep(seconds)
    print(f"Task {name} completed")

if __name__ == '__main__':
    # Creating processes
    process1 = multiprocessing.Process(target=task, args=("A", 2))
    process2 = multiprocessing.Process(target=task, args=("B", 3))

    print("Starting processes")
    process1.start()
    process2.start()
    print("Processes started")
```

First, it is worth noting that this is almost identical syntax to what we used in threads. However, the differences are important - We are using `if __name__ == '__main__'` to prevent the processes from being started multiple times. This is because processes can't share data, not even the `task` function. This means that the `task` has to be imported by the new process, and this import will create even more processes if their creation is not under the `if __name__ == '__main__'` condition.

## Using asyncio (`async` and `await`)

This is most similar to our example using generator functions. The `asyncio` module allows us to run multiple tasks in parallel, as it defines an event loops that continuously polls between tasks to see if they are completed. We can have more control on where the function pauses and continues, like we did with `yield`, using the `await` keyword. However we can only use `await` inside a function that is explicitly `async`. Let's look at an example:

```python
import asyncio
from time import sleep
from datetime import datetime, timedelta
import random


async def task(name, seconds):
    start_time = datetime.now()
    while start_time + timedelta(seconds=seconds) > datetime.now():
        print(f"Task {name} is working...")
        await asyncio.sleep(0.3)  # Simulate work being done
    result = random.randint(10000, 20000)
    print(f"Task {name} completed with result: {result}")
    return result  # Return the final result


async def main():
    # Run a single task
    single_task_result = await task("A", 2)
    print(f"Single task result: {single_task_result}")

    # Run multiple tasks concurrently
    tasks = [task("B", 2), task("C", 3)]
    results = await asyncio.gather(*tasks)
    print(f"Multiple tasks results: {results}")


# Run the main coroutine
asyncio.run(main())
```

Our `task` function is almost identical to what it was in our generator example, except that we don't need `yield` and we can directly specify `await` where we want to release control (or pause) in favor of other tasks. We can then use `asyncio.gather` to run multiple tasks concurrently. This function will return a list of results, in the same order as the tasks were given to it.

It is important to note that calling an `async` function directly will not run it. Instead, it will return a `coroutine` object. To run the function, we need to pass it to `asyncio.run`, which will run the function and return the result, or `await` for its result if it is called from another `async` function. For example, this will not work:

```python
async def task():
    return 3

result = task()  # This will return a coroutine object
print(result)  # <coroutine object task at 0x0000021E1F6F4C80>
```

But this will:

```python
async def task():
    return 3

result = asyncio.run(task())  # This will run the task and return the result
print(result)  # 3
```

As well as this:

```python
async def task():
    return 3

async def main():
    result = await task()  # This will block until the task is done and has a real result
    print(result)  # 3

asyncio.run(main())
```

## Which method should I use?

This is a very common question, and the answer is not simple. Each method has its own advantages and disadvantages, and the best method depends on the specific use case. Let's look at some of the differences between the methods:

1. `threading` is the simplest method, but it is not very efficient. This is because Python uses a "Global Interpreter Lock" (GIL) to prevent multiple threads from running Python code at the same time. This means that only one thread can run Python code at a time, and the other threads are blocked. This is not a problem if the threads are doing I/O (such as reading from a file or a network), but it is a problem if the threads are doing CPU-intensive work (such as calculating prime numbers). This means that `threading` is best suited for I/O-bound tasks, but not for CPU-bound tasks. (I/O-bound tasks include reading and writing files to disk, waiting on network or web responses, etc. CPU-bound tasks include calculating prime numbers, sorting lists, etc.)
2. `multiprocessing` is similar to `threading`, but it does not use the GIL. This means that it is more efficient for CPU-bound tasks, but it is more complicated to use. It is more expensive to create a new process than a new thread, but is allows us to use multiple CPU cores at the same time. This means that `multiprocessing` is best suited for CPU-bound tasks, but not for I/O-bound tasks.
3. `asyncio` is similar to `threading`, but it does not use threads. Instead, it uses a single thread and a single process, and it uses a single CPU core. This means that it is not suitable for CPU-bound tasks, but it is very efficient for I/O-bound tasks. It is also very efficient for tasks that are waiting for other tasks to complete, such as waiting for a web response before continuing. This is because `asyncio` allows us to pause a task and continue with another task, and then resume the first task when the other task is done. This is called "asynchronous" programming, and it is very useful for I/O-bound tasks. For this reason, `asyncio` is most often used for web servers, where the server needs to wait for a web request before continuing, and it needs to wait for a database response before continuing, etc. This means that `asyncio` is best suited for I/O-bound tasks, but not for CPU-bound tasks. The difference between `asyncio` and `threading` is mostly a matter of syntax, with some use cases being easier to implement in `asyncio` and some being easier to implement in `threading`.
4. Generator functions are similar to `asyncio`, but they are not as efficient. This is because they are not optimized for this use case and served us only for demonstrating what is happening. They are not suitable for any real-world use case of parallel processing.
5. No parallel processing - it's important to remember that parallelizing tasks is not magic, it comes with advantages in certain cases but has its cost. Most simple programs will not benefit from writing code to work in parallel (some will even see a performance decrease). It is also harder to read and write code that runs in parallel, and it is harder to debug. For this reason, it is important to consider if parallel processing is really needed before writing code that runs in parallel.
