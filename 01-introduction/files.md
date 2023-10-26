# Files

Files make it possible to store data on the hard drive. This is useful for storing data between program executions, or for sharing data with other programs.

## Opening a file

To open a file, use the `open()` function. The first argument is the path to the file, and the second argument is the mode. The mode can be either `r` (read), `w` (write), or `a` (append).

We must always close the file when we are done with it. This is done with the `close()` function.

```python
file = open("file.txt", "r")
file.close()
```

## Reading a file

In the previous example, we opened the file in read mode. This means that we can read the contents of the file using the `read()` function.

```python
file = open("file.txt", "r")
contents = file.read()
print(contents)
file.close()
```

**Note:** The `read()` function reads the entire file. If the file is large, this can take a long time.

Reading (and writing) a file can only be done once the file is opened and before it is closed. Trying to read or write to a closed file will result in an error.

```python
file = open("file.txt", "r")
file.close()
contents = file.read() # This will result in an error
```

## Writing to a file

To write to a file, we must open it in write mode. This will overwrite the contents of the file, so be careful. If the file does not exist, it will be created.

```python
file = open("file.txt", "w")
file.write("Hello world!")
file.close()
```

## Appending to a file

To append to a file, we must open it in append mode. This will add the new contents to the end of the file.

```python
file = open("file.txt", "a")
file.write("Hello world!")
file.close()
```

## Reading and writing at the same time

It is possible to read and write to a file at the same time. This is done by opening the file in `r+` mode.

```python
file = open("file.txt", "r+")
contents = file.read()
file.write("Hello world!")
file.close()
```

The order of the read and write operations is important. If we `write` first, the write operation will overwrite the start of the file. If we write to the file after reading it, the write operation will be appended to the end of the file. This is because the read operation moves the cursor to the end of the file.

## File cursor

The file cursor is a pointer that points to a specific position in the file. When we read or write to a file, the cursor is moved to the end of the read or write operation. This means that if we want to read the file again, we must move the cursor back to the start of the file. Some useful methods for using the cursor include:

- `seek(0)` - Move the cursor to the start of the file
- `seek(10)` - Move the cursor to the 10th byte of the file
- `tell()` - Get the current position of the cursor
- `truncate()` - Truncate the file at the current position of the cursor (delete everything after the cursor)
- `result = file.read()` - Read the entire file, and move the cursor to the end of the file. `result` will be a string containing the entire file.
- `result = file.read(10)` - Read 10 bytes from the file, and move the cursor 10 bytes forward. `result` will be a string containing the 10 bytes.
- `result = file.write("Hello world!")` - Write "Hello world!" to the file, and move the cursor 12 bytes forward (the length of the string). `result` will be the number of bytes written.

```python
file = open("file.txt", "r+")
contents = file.read()
file.seek(0)  # Move the cursor to the start of the file
result = file.write("Hello world!")  # Write "Hello world!" to the file, at the start
file.seek(0)  # Move the cursor to the start of the file
contents = file.read()  # Read the entire file again
end_cursor = file.tell()  # Get the current position of the cursor
print(contents)
print(end_cursor)
file.close()
```

## Other file modes

There are other file modes that can be used. Here is a table of the most common ones, and what they do:

| Mode | Read | Write | Append | Create | Cursor at start | Cursor at end |
| ---- | ---- | ----- | ------ | ------ | --------------- | ------------- |
| `r` | Yes | No | No | No | Yes | No |
| `r+` | Yes | Yes | No | No | Yes | No |
| `w` | No | Yes | No | Yes | Yes | No |
| `w+` | Yes | Yes | No | Yes | Yes | No |
| `a` | No | No | Yes | Yes | No | Yes |
| `a+` | Yes | No | Yes | Yes | No | Yes |

There are also modes that allow us to read and write in binary mode. These are `rb`, `rb+`, `wb`, `wb+`, `ab`, and `ab+`. These modes are useful for reading and writing binary files, such as images. We will discuss binary files in a later chapter.

## File paths

When opening a file, we must specify the path to the file. There are two types of paths: absolute paths and relative paths.

An absolute path is a path that starts at the root of the file system. On Windows, this is the `C:\` drive. On Linux and Mac, this is the `/` directory. An absolute path always starts with a `/` on Linux and Mac, and with a drive letter on Windows.

```python
file = open("/home/user/file.txt", "r")  # Linux/Mac
file = open("C:\\Users\\user\\file.txt", "r")  # Windows
```

Notice that for Windows, we must use double backslashes (`\\`) instead of single backslashes (`\`). This is because the backslash is used as an "escape character" in Python. We can also use a "raw string" to avoid this problem.

```python
file = open(r"C:\Users\user\file.txt", "r")  # Windows
```

A relative path is a path that starts at the current working directory. This is the directory that the program is running from.

```python
file = open("file.txt", "r")  # Relative path - file.txt is in the current working directory
another_file = open("folder\\another_file.txt", "r")  # Relative path - another_file.txt is in a folder called "folder" in the current working directory
```

## With statement

When we open a file, we must remember to close it when we are done. If we forget to close the file, it will remain open until the program exits. This can cause problems if we try to open the file again later, or if we try to delete the file. This may also be a problem if the program crashes, or if many files are opened at once.

To avoid this problem, we can use the `with` statement. This will automatically close the file when we are done with it.

```python
with open("file.txt", "r") as file:
    contents = file.read()

print(contents) # The file is closed here, since we are no longer inside the "with" statement
```
