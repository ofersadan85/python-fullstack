# Classes - Basic

## What is a class?

A `class` is a blueprint for an object. It defines what attributes and methods an object of that `class` will have. For example, `str` is a `class`. It defines what attributes and methods a string will have, such as `upper()`, `lower()`, `replace()`, `split()` etc. We can define our own classes, and create objects (instances) of that class.

A `class` is Python's way of programming in an object oriented way (i.e Object Oriented Programming - OOP). It is a way of organizing our code, and making it more reusable. It is also a way of thinking about our code and data, and how they relate to the real world. For example, if we are making a game, we can have a `Player` class, and a `Monster` class. Both of these classes can have attributes and methods that are specific to them, and we can create as many instances of these classes as we want. We can also have a `Game` class, that will contain the logic of the game, and can itself contain instances of `Player` and `Monster` classes.

## Creating a class

The most basic class is an empty class. It can be created like this:

```python
class Person:
    pass
```

To create an object instance of this class, we can do this:

```python
person = Person()
```

Note that these two are different. `Person` is the class, the type of the object. `person` is an instance of the class, an object. This is similar to how `str` is a class, and `"Hello"` is an instance of that class. We can create as many instances of a class as we want.

```python
person1 = Person()
person2 = Person()
print(type(person1)) # <class '__main__.Person'>
print(type(person2)) # <class '__main__.Person'>
print(type(person1) == type(person2)) # True
```

## Class attributes

Classes aren't very useful, if they don't contain shared attributes, or shared data. We can add attributes to a class, by defining them inside the class. We can then access these attributes on any instance of the class. These are called "class attributes", because they are shared between all instances of the class.

```python
class Person:
    legs = 2
    hands = 2

person1 = Person()
print(person1.legs) # 2
```

Changing the class attribute will change it for all instances of the class, as long as they haven't overridden the attribute.

```python
class Person:
    legs = 2
    hands = 2

person1 = Person()
person2 = Person()
Person.legs = 3
print(person1.legs) # 3
print(person2.legs) # 3
```

## Instance attributes

When we create an object, we can set it's attributes individually. These are called "instance attributes", because they are unique to that instance. They do not affect other instances of the class.

```python
class Person:
    legs = 2
    hands = 2

person1 = Person()
person1.legs = 3
print(person1.legs) # 3
person2 = Person()
print(person2.legs) # 2
```

In other words, instance attributes override class attributes, and class attributes are shared between all instances of the class only for those instances that haven't overridden the attribute.

## Shared behavior

One of the more useful things that we can do with classes, is have them encapsulate shared behavior. We can define methods inside a class, and all instances of that class will have access to those methods. These methods can be used to manipulate the **instance**, or to return information about the **instance**.

```python
class Person:
    legs = 2
    hands = 2

    def walk(self):
        print("Walking")

    def get_legs(self):
        return self.legs

person1 = Person()
person1.walk() # Walking
print(person1.get_legs()) # 2

person2 = Person()
person2.walk() # Walking
person2.legs = 3
print(person2.get_legs()) # 3
```

## The `self` parameter

When we defined the methods in the previous example, we used a parameter called `self`. This is a special parameter, that is used to refer to the instance of the class that the method is called on. It is not a reserved keyword, and we can use any name we want, but `self` is the convention, and it is recommended to use it. For us, it is a marker that these functions are useful only when called on an instance of the class, and not on the class itself.

```python
class Person:
    def walk(self):
        print("Walking")

person1 = Person()
person1.walk() # Walking
Person.walk() # TypeError: walk() missing 1 required positional argument: 'self'
```

## Inheritance

Inheritance is one of the key attributes of OOP / classes. They allow us to define subtypes, that can still use the attributes and methods of the parent class. This is useful when we want to create a class that is similar to another class, but has some differences. For example, we can have a `Person` class, and a `Student` class. The `Student` class can inherit from the `Person` class, and have all the attributes and methods of the `Person` class, but also have some additional attributes and methods that are specific to students.

Just like in the real world, a specific student name "John" *is* a student, but he is also a person and can do anything that a person does. In the same way, a `Student` object *is* a `Student`, but it is also a `Person`, and can do anything that a `Person` can do.

```python
class Person:
    legs = 2

    def walk(self):
        print("Walking")

class Student(Person):  # Student inherits from Person
    def study(self):
        print("Studying")

person1 = Person()
student1 = Student()
person1.walk() # Walking
student1.walk() # Walking
student1.study() # Studying
person1.study() # AttributeError: 'Person' object has no attribute 'study'
```

Inheritance can have multiple levels, both horizontally (just like brothers and sisters), and vertically (just like parents and grandparents). For example, we can have a `Student` class, that inherits from `Person`, and a `Teacher` class, that also inherits from `Person`. Both `Student` and `Teacher` will have the attributes and methods of `Person`, but they will also have their own attributes and methods. All of these can inherit from an `Mammal` class, that will have attributes and methods that are common to all mammals an so on.

```python
class Animal:
    can_move = True

class Mammal(Animal):
    has_hair = True

class Person(Mammal):
    legs = 2

    def walk(self):
        print("Walking")

class Student(Person):
    def study(self):
        print("Studying")

class Teacher(Person):
    def teach(self):
        print("Teaching")

john = Student()
print(john.can_move) # True
john.walk() # Walking
john.study() # Studying
jane = Teacher()
print(jane.legs) # 2
jane.walk() # Walking
jane.teach() # Teaching
```

## `__init__` method

When initializing an object (i.e creating an instance of a class), Python internally calls a special method called `__init__`. This method is called with the arguments that we pass to the class constructor. We can define this method in our class, and use it to initialize the instance. This is useful when we want to set some instance attributes when the object is created.

```python
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("John")
print(person1.name) # John
```

Arguments do not have to match to internal attributes. We can use any name we want, and set any attributes we want when initializing the object.

```python
import random

class Person:
    def __init__(self, first_name, last_name):
        self.full_name = first_name + " " + last_name
        self.unique_id = random.randint(0, 1000)

person1 = Person("John", "Doe")
print(person1.full_name) # John Doe
print(person1.unique_id) # 123
```

## Overriding methods

When we inherit from a class, we can override any of the methods of the parent class. This is useful when we want to change the behavior of a method, or add some additional functionality.

```python
class Car:
    def drive(self):
        print("Driving")

class SportsCar(Car):
    def drive(self):
        print("Driving fast")
```

## Calling parent methods (`super`)

When we override a method, we can still call the parent method, if we want to. This is useful when we want to add some additional functionality, but still keep the original functionality.

```python
class Car:
    def drive(self):
        print("Driving")

class SportsCar(Car):
    def drive(self):
        super().drive() # Calling parent method
        print("Fast")

car1 = Car()
car1.drive() # Driving
car2 = SportsCar()
car2.drive() # Driving \n Fast
```

## Magic methods

Like `__init__`, there are many other special methods that we can define in our classes. These are called "magic methods", and they are used by Python internally. We can override these methods, and change the behavior of our classes. For example, we can override the `__str__` method, and change how our class is represented as a string.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "A person named " + self.name

person1 = Person("John")
print(person1) # A person named John
```

The list of all magic methods is too long to describe here, but for convenience, here is a table of some of the more common and useful methods:

| Method | Usage example | Description | Parameters | Return value |
| --- | --- | --- | --- | --- |
| `__init__` | `john = Person()` | Called when initializing an object | `self` and any other arguments | `None` |
| `__str__` | `print(john)` | Called when converting an object to a string | `self` | `str` |
| `__int__` | `int(john)` | Called when converting an object to an integer | `self` | `int` |
| `__add__` | `john + jane` | Called when adding two objects | `self` and only one other argument | Anything |
| `__sub__` | `john - jane` | Called when subtracting two objects | `self` and only one other argument | Anything |
| `__mul__` | `john * jane` | Called when multiplying two objects | `self` and only one other argument | Anything |
| `__div__` | `john / jane` | Called when dividing two objects | `self` and only one other argument | Anything |
| `__eq__` | `john == jane` | Called when comparing two objects for equality | `self` and only one other argument | `bool` |
| `__lt__` | `john < jane` | Called when comparing two objects for less than | `self` and only one other argument | `bool` |
| `__gt__` | `john > jane` | Called when comparing two objects for greater than | `self` and only one other argument | `bool` |
| `__le__` | `john <= jane` | Called when comparing two objects for less than or equal | `self` and only one other argument | `bool` |
| `__ge__` | `john >= jane` | Called when comparing two objects for greater than or equal | `self` and only one other argument | `bool` |
| `__len__` | `len(john)` | Called when getting the length of an object | `self` | `int` |
| `__getitem__` | `john[0]` | Called when getting an item from an object | `self` and the item name | Anything |
| `__setitem__` | `john[0] = "John"` | Called when setting an item in an object | `self`, item name, item value | `None` |
| `__contains__` | `"John" in john` | Called when checking if an item is in an object | `self` and the item name | `bool` |

The full list and documentation can be found [here](https://docs.python.org/3/reference/datamodel.html#special-method-names).

In effect, using one of these magic methods is just a shortcut for calling a method on an object, for example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def make_baby(self, other):
        return "A baby for " + self.name + " and " + other.name

    def __add__(self, other):
        return "A baby for " + self.name + " and " + other.name

john = Person("John")
jane = Person("Jane")
result1 = john.make_baby(jane) # A baby for John and Jane
result2 = john.__add__(jane) # A baby for John and Jane
result3 = john + jane # A baby for John and Jane
print(result1 == result2 == result3) # True (all three are the same)
```
