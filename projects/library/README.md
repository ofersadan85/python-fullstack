# Library Management System Project

This project involves creating a Python application for managing a library's book loans, returns, and orders. The program should provide functionalities for customers to loan and return books, as well as order new books that are out of stock. The program will be object-oriented, with classes for Libraries, Books, and Customers.

## Object Classes

- **Library**: A class that encapsulates all the information and functionalities of a library including books, customers, address, employees, etc.
- **Book**: A class representing a book with all required information fields (title, author, genre, language, year, etc.).
- **Customer**: A class for handling customer information and interactions with the library (loaned books, ordered books, history, etc.).

## Program Features

1. **Start Menu**: When the main program runs, present the user with three options:
    - Loan a book
    - Return a book
    - Order an out-of-stock book

2. **Book Loaning Restrictions**:
    - A customer can have a maximum of 2 loaned books at any given time.
    - If a customer already has 2 loaned books, they should not be able to loan more but can still place orders.

3. **Book Ordering Restrictions**:
    - A customer can order a maximum of 2 out-of-stock books.
    - Customers with 2 ordered books cannot order more but can loan books available in stock.

4. **Customer History**:
    - Each customer should have a history record of all loaned and ordered books, including dates and times.

5. **Book Information**:
    - Title, author, genre, language, and year of publication.
    - Loan history and maximum allowed loan duration.

6. **Library Information**:
    - Address, total number of books, most popular book, best customer, and number of employees.

## Requirements

### Classes and Methods

- Implement a `Library` class to manage the operations within the library.
- Implement a `Book` class with attributes for title, author, genre, language, year, loan history, and max loan days.
- Implement a `Customer` class with attributes for tracking loaned books, ordered books, and customer history.

### Functionalities

- **Loan a Book**: Check if the customer has less than 2 loaned books. If so, proceed with the loan process.
- **Return a Book**: Update the library and customer records when a book is returned.
- **Order a Book**: Allow customers to order a book that is out of stock if they haven't already ordered two books.

### Error Handling

- Proper error handling for scenarios like requesting a book that doesn't exist, exceeding loan limits, etc.

### User Interface

- Implement a simple command-line interface for interaction with the program.
- Ensure the interface is user-friendly and prompts appropriate messages during operations.
- Ensure error messages are displayed in a user-friendly manner.

## Future requirements

The following requirements will only be added in the future to this project:

### Features

- **Employee Management**: Implement a feature for managing employees and their roles in the library.
- **Book Management**: Implement a feature for managing books, including adding new books, removing books, and updating book information.
- **Customer Management**: Implement a feature for managing customers, including adding new customers, removing customers, and updating customer information.
- **Login System**: Implement a login system for employees and customers to access the library's features.

### Technical

- **Data Persistence**: Store data in files or implement a database to store all the library's information and customer history.
- **Documentation**: Document the code and provide a user manual for the program.
- **Version Control**: Use Git to manage the project's source code and version control.
- **Unit Testing**: Implement unit tests for the program's classes and methods.
- **GUI / Web**: Implement a graphical user interface for the program using a GUI framework or web framework.
