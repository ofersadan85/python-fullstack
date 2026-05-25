# SQL for Python users

Structured Query Language (***SQL***) is a powerful tool for managing and manipulating databases. It is the de facto standard for relational databases, and is used by many popular database systems, including MySQL, PostgreSQL, Oracle, Microsoft SQL Server, Microsoft Access, SQLite, and MariaDB.

Some of the advantages of using SQL are:

1. It allows you to store data in a *relational* database, which means that objects can be defined to be in some way related to each other (e.g. a user can have many posts, a post can have many comments, etc.)
2. While reading or saving data to text files is easy, editing a single record in a large file is not. SQL allows you to easily update, delete, and query data in a database. When using a relational database, you can also define *constraints* that ensure that the data is always valid.
3. SQL is a standard language, so you can use it with many different database systems. This means that you can easily switch from one database to another without having to learn a new language. This is especially useful when working with large databases that require a lot of maintenance.
4. Separating the data from the code makes it easier to maintain and update your application. For example, if you want to change the way your application stores data, you only need to change the SQL queries, not the code that uses them. At the same time, changing the logic of your application does not harm the data stored in the database.

## Why SQLite?

One of the biggest advantages of using databases, is that they can of "outsourced" to a separate server. This means that you can access the data from anywhere, as long as you have access to the server. So multiple applications can share the same data, read and write to it at the same time, etc. This is important when deploying applications to the web, as we will do in this full-stack course. However, this also means that you need to set up and maintain the server, which can be a lot of work.

SQLite is a database engine that allows you to store data in a database file on your computer. This means that you don't need to set up a server. SQLite is also very fast, and supports most of the features of other SQL databases.

This makes it ideal for learning SQL, as you can focus on the language itself, without having to worry about setting up a server. Later, we will learn how to move on to other databases, such as PostgreSQL, which is a popular choice for web applications.

## Getting Started

If you have Python, SQLite is included in the standard Python distribution. No need to install anything more! We can import the `sqlite3` module to get started.

```python
import sqlite3
```

### Creating a Connection

To use SQLite, you need to create a connection object that represents the database. This "connection" can be thought of as simulating a link between our program and an external database (except here, it's just a file). The connection object allows us to execute SQL queries and manage the database. If the database does not exist, SQLite will create one.

```python
import sqlite3
connection = sqlite3.connect("example.db")
```

### Creating a Cursor

We can't do anything with the database until we create a cursor object. The cursor object allows us to execute SQL queries and manage the database. We can create a cursor object by calling the `cursor()` method on the connection object.

A cursor can be thought of as a pointer to a specific row (or rows) within a table. It allows us to move through the table and access the data stored in each row, without having to read the entire table into memory, and without affecting other rows in the table, which might be in use by other users / processes.

```python
cursor = connection.cursor()
```

## Basic SQL Operations

### Creating a Table

The most basic component of every SQL-relational database is the table. A table is a collection of related data entries, and it consists of columns and rows. Each column represents a different attribute of the data, and each row represents a single data entry.

```python
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE users
                    (id INTEGER,
                     name TEXT,
                     age INTEGER
                     )"""
)
```

Or to break down the general SQL syntax for creating a table:

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

#### Important

- A table name must be unique within a database. If we try to create a table with the same name as an existing table, SQLite will raise an error.
- The `cursor.execute()` method is used to execute SQL queries. It takes a single string as an argument, which is the SQL query to execute.
- The `CREATE TABLE` statement is used to create a new table in the database. It takes two arguments: the name of the table, and a list of columns. Each column is defined by a name and a data type. In this example, we have three columns: `id`, `name`, and `age`. The `id` column is of type `INTEGER`, which means that it can only contain integers. The `name` column is of type `TEXT`, which means that it can contain any text. The `age` column is of type `INTEGER`, which means that it can only contain integers.

### Column Data Types

It's important that we have the correct data type for each column. If we try to insert data of the wrong type, SQLite will raise an error. For example, if we try to insert a string into an integer column, SQLite will raise an error.

The supported data types are:

| Data Type | Description | Example | When to Use | When Not to Use | Python Equivalent |
| --- | --- | --- | --- | --- | --- |
| `INTEGER` | A signed integer (can be positive or negative), stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value. | `42` | For storing numbers. | For storing numbers that are too large to fit in an `INTEGER`. | `int` |
| `REAL` | A floating point value, stored as an 8-byte IEEE floating point number. | `3.141592653589793` | For storing floating point numbers. | For storing numbers that are too large to fit in a `REAL`. | `float` |
| `TEXT` | A text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE). | `'Hello World'` | For storing text. | For storing binary data, or strings that are very small | `str` |
| `BLOB` | A blob of data, stored exactly as it was input. | `b'Hello World'` | For storing binary data. | For storing text. | `bytes` |

There's also a special data type called `NULL`, which is used to represent a missing value (like Python's `None`). This is the default value for all columns of any type, unless we specify otherwise.

Other SQL databases support additional data types. For example, PostgreSQL supports `JSON`, `UUID`, `ARRAY`, and more. SQLite does not support these data types.

### `INSERT` - Adding Data to a Table

```python
cursor.execute("""INSERT INTO stocks VALUES
('2023-12-13','BUY','AAPL',100,35.14)
""")
```

Notice values in single quotes (`'`) are always interpreted as strings. The general syntax for inserting data into a table is:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

But if we're inserting data into all columns, we can omit the column names:

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

### Saving (Committing) the Changes

All the actions we've taken so far have been temporary. To save the changes to the database, we need to call the `commit()` method on the connection object.

```python
connection.commit()
```

This is useful, for when we want to make sure several changes are made at the same time, or not at all. If this action will fail, we can be sure that we have not created partial changes to the database.

The opposite of `commit()` is `rollback()`. This method will undo all changes made since the last `commit()`.

### `SELECT` - Retrieving Data from a Table

```sql
SELECT column1, column2, ... FROM table_name;
```

Or to select all columns:

```sql
SELECT * FROM table_name;
```

Will return a list of tuples, where each tuple represents a row in the table, in the exact order of the columns we selected (or in the order they were defined in the table, if we used `*`).

```python
cursor.execute("SELECT * FROM stocks")
```

Notice that `cursor.execute()` never returns anything. Instead, we need to use the `fetchall()` method on the cursor object to retrieve the results of the query.

```python
rows = cursor.fetchall()
```

Or `fetchone()` to retrieve a single row:

```python
row = cursor.fetchone()
```

Cursor objects also have a `description` attribute, which contains information about the columns returned by the query, so we could later match between the values and the columns.

```python
print(cursor.description)
```

### `UPDATE` - Updating Records

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
```

This will update ***all*** rows in the table. To update only specific rows, we can use the `WHERE` clause, followed by a condition.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

For example, to update only the user "John Doe":

```sql
UPDATE users
SET age = 42
WHERE name = 'John Doe';
```

This is very important, as otherwise we might accidentally update all rows in the table, and set all users to be 42 years old!

The `WHERE` clause can also be used with `SELECT` and `DELETE` queries, to select or delete only specific rows.

### `DELETE` - Deleting Records

```sql
DELETE FROM table_name
WHERE condition;
```

Again, it is very important to use the `WHERE` clause, to make sure we don't accidentally delete all rows in the table.

### Closing the Connection

```python
connection.close()
```

## More Advanced SQL Operations

This is just the tip of the iceberg. There are many more SQL operations that we can perform, such as:

- `ORDER BY` - Sort the results by a specific column
- `GROUP BY` - Group the results by a specific column
- `LIMIT` - Limit the number of results returned
- `JOIN` - Join two or more tables together
- `UNION` - Combine the results of two or more `SELECT` queries
- `CREATE INDEX` - Create an index on a column or a group of columns
- `CREATE VIEW` - Create a virtual table based on the result-set of a `SELECT` query
- `ALTER TABLE` - Add, remove, or modify columns in an existing table
- `DROP TABLE` - Delete an existing table
- `DROP INDEX` - Delete an index

And many more. We will learn about some of these operations later in the course. For now, you can read more about them in the [SQLite documentation](https://www.sqlite.org/lang.html).
