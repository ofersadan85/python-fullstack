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
