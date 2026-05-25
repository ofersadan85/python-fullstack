# Getters and Setters

In JavaScript, we can use getters and setters to control access to an object's properties.

## Getters

A getter is a method that gets the value of a specific property.

```javascript
const person = {
  firstName: 'John',
  lastName: 'Doe',
  get fullName() {
    return this.firstName + ' ' + this.lastName;
  }
};

console.log(person.fullName); // John Doe
```

In the example above, we have a `person` object with a `fullName` getter. When we call `person.fullName`, the `get` method is executed and returns the value of `firstName` and `lastName`. The `get` method is called without using parentheses. It looks like we are accessing a property, but in reality, we are calling a method.

## Setters

A setter is a method that sets the value of a specific property.

```javascript
const person = {
  firstName: 'John',
  lastName: 'Doe',
  set fullName(value) {
    const parts = value.split(' ');
    this.firstName = parts[0];
    this.lastName = parts[1];
  }
};

person.fullName = 'Jane Smith';
console.log(person.firstName); // Jane
console.log(person.lastName); // Smith
```

In the example above, we have a `person` object with a `fullName` setter. When we call `person.fullName = 'Jane Smith'`, the `set` method is executed and sets the value of `firstName` and `lastName`. The `set` method is called without using parentheses. It looks like we are assigning a value to a property, but in reality, we are calling a method.

## Getters and Setters in classes

We can also use getters and setters in classes.

```javascript
class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  get fullName() {
    return this.firstName + ' ' + this.lastName;
  }

  set fullName(value) {
    const parts = value.split(' ');
    this.firstName = parts[0];
    this.lastName = parts[1];
  }
}

const person = new Person('John', 'Doe');
console.log(person.fullName); // John Doe
person.fullName = 'Jane Smith';
console.log(person.firstName); // Jane
console.log(person.lastName); // Smith
```

In the example above, we have a `Person` class with a `fullName` getter and setter. We can use them just like we did with the object.

## Comparisons with Python

In Python, we can use the `@property` decorator to define getters and setters. The syntax is different, but the concept is the same.

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, value):
        parts = value.split(' ')
        self.first_name = parts[0]
        self.last_name = parts[1]

person = Person('John', 'Doe')
print(person.full_name) # John Doe
person.full_name = 'Jane Smith'
print(person.first_name) # Jane
print(person.last_name) # Smith
```

In the example above, we have a `Person` class with a `full_name` getter and setter. We can use them just like we did with the JavaScript class.

However, in Python, we can only define getters and setters for class properties. In JavaScript, we can define them for object properties as well. In other words, in Python we don't have the option to create a `dict` with getters and setters. In JavaScript, we can (the equivalent of a `dict` in JavaScript is called an object).
