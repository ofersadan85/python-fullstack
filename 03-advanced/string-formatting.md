# Python String Formatting Guide

This guide is meant to teach you various tips and tricks on string formatting in Python! Whether you are preparing a message or displaying output, learning how to format strings is essential in Python. This guide will introduce you to various methods and best practices.

## Using Different Quote Marks for Strings

Strings in Python can be defined in several ways, depending on the need for including certain characters within the string or dealing with multi-line strings.

### Single (`'`) vs Double (`"`) Quotes

```python
# A simple string defined within single quotes.
s1 = 'Hello, world!'
# A simple string defined within double quotes.
s2 = "Hello, world!"
```

There is no difference between single and double quotes in Python. You can use either one to define a string. However, you can use one type of quote inside the other to avoid syntax errors.

```python
# A string with single quotes inside double quotes.
s1 = "It's a lovely day!"
# A string with double quotes inside single quotes.
s2 = 'She said: "Hello!"'
```

### Double Quotes (`"`)

Use double quotes when your string contains single quotes (like apostrophes) to avoid syntax errors.

```python
# A string with an apostrophe inside double quotes.
"It's a lovely day!"
```

### Triple Quotes (`'''`) or (`"""`)

Triple single quotes or triple double quotes are used for strings that span multiple lines, which can include line breaks. This is meant to replace the use of `\n` for line breaks in strings.

```python
# A multi-line string using triple single quotes.
s1 = '''
This string spans
multiple lines
'''
# A multi-line string using triple double quotes.
s2 = """
This string spans
multiple lines
"""
# A string with line breaks using `\n`.
s3 = 'This string\nspans multiple\nlines'
print(s1==s2==s3) # True
```

## The `format` Method

The `format` method is used to insert specified values into a string with placeholder braces `{}`.

### Basic Usage of `format`

Insert values into placeholders in the order they appear.

```python
# A string with placeholders replaced by values passed to `format`.
s1 = '{} {}'.format('Hello', 'World')
print(s1) # 'Hello World'
```

### Positional Formatting with `format`

Specify the order of placeholders using the position of the arguments in the `format` method.

```python
# A string where placeholders are filled based on position provided.
s1 = '{1} {0}'.format('World', 'Hello')
print(s1) # 'Hello World'
```

### Keyword Formatting with `format`

Use keywords in placeholders and provide corresponding values in the `format` method.

```python
# A string formatted using keyword arguments.
s1 = '{greeting} {noun}'.format(greeting='Hello', noun='World')
print(s1) # 'Hello World'
```

### Formatting Numbers with `format`

Control the formatting of numbers, like showing a certain number of decimal places.

```python
# Formatting floating-point numbers to show three decimal places.
s1 = 'Pi is approximately {0:.3f}'.format(3.14159)
print(s1) # 'Pi is approximately 3.142'
```

There are many more ways to format strings using the `format` method. You can learn more about them in the [Python documentation](https://docs.python.org/3/library/string.html#formatstrings).

## f-strings (Formatted String Literals)

F-strings are a more readable and concise way to embed expressions inside string literals using curly braces `{}`.

### Basic f-string

Directly include variables and simple expressions inside string literals.

```python
# Using f-string to include variables directly within the string.
name = 'World'
s1 = f'Hello, {name}!'
print(s1) # 'Hello, World!'
```

### Expression Evaluation in f-strings

Evaluate expressions right inside the string literals.

```python
# An f-string that evaluates an expression within the string.
s1 = f'The sum of 2 and 3 is {2 + 3}.'
print(s1) # 'The sum of 2 and 3 is 5.'
```

We can use any valid Python expression inside the curly braces of an f-string, but we cannot use multi-line statements.

### Formatted Expressions in f-strings

Format numbers or perform operations directly within the curly braces of f-strings.

```python
# Using f-strings to format a floating-point number to three decimal places.
pi = 3.14159
s1 = f'Pi is approximately {pi:.3f}'
print(s1) # 'Pi is approximately 3.142'
```

## Raw Strings

A raw string tells Python to ignore all escape characters (like `\n` for new line) and print the string exactly as it is.

### Using Raw Strings

Useful when dealing with regular expressions or Windows file paths.

```python
# A raw string to maintain actual backslashes in output.
s1 = r'C:\path\to\file'
s2 = "C:\\path\\to\\file"
print(s1==s2) # True
```

A raw string can be combined with other string formatting methods like f-strings.

```python
file = '1.pdf'
s1 = f'C:\\path\\to\\{file}'
s2 = rf'C:\path\to\{file}'
print(s1==s2) # True
```

## f-strings vs `format`

In most cases, choosing between f-strings and `format` is a matter of personal preference. However, there are some cases where one is more suitable than the other.

For example, `format` is separate from the string literal, so it can be used to format strings that are not known when writing the code. Try running the following code:

```python
user_format = input('Enter format: ')  # Try entering: {}*-*{}
user_greeting = user_format.format('Hello', 'World')
print(user_greeting)  # 'Hello*-*World'
```

This is also true if you would like to re-use the same format for multiple strings.

```python
user_format = '{1} {0}'
user_greeting = user_format.format('Hello', 'World')
user_farewell = user_format.format('Goodbye', 'World')
print(user_greeting) # 'World Hello'
print(user_farewell) # 'World Goodbye'
```

On the other hand, f-strings are more readable and concise, so they are preferred when the string is known when writing the code, and there is no need to re-use the format.

```python
name = 'World'
s1 = f'Hello, {name}!'
print(s1) # 'Hello, World!'
```
