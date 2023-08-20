# Variables

Variables are like boxes that can hold values. We can give them a name and then use that name to access the value inside the box. We can also change the value inside the box.

```python
name = "John"
print("Hello " + name)
```

Output:
> Hello John

Again, we have to remember what type that variable has!

```python
name = 123
print("Hello " + name)
```

Output:
> TypeError: can only concatenate str (not "int") to str

As we can see, the plus (`+`) operator behaves differently depending on the type of the operands. If both operands are strings, it will concatenate them. If one of the operands is a string and the other is a number, it will give us an error.

**READ THE ERROR MESSAGE!** It tells us exactly what the problem is. In this case, it says that we can only concatenate strings to strings, not integers.

With some operations, mixing types is actually acceptable. For example, the multiply operand (`*`):

```python
name = "John" * 3
print("Hello " + name)
```

Output:
> Hello JohnJohnJohn
