## PostgreSQL

While SQLite is a great database for small projects, PostgreSQL is a more powerful database that is used in many large projects. PostgreSQL is a relational database management system that is open-source and has many advanced features.

Additionally, PostgreSQL is the most popular database in the world, with great documentation and a large community. It is also very fast and reliable, and it has many advanced features that are not available in SQLite (such as advanced data types, built-in functions, and more).

See [the official documentation](https://www.postgresql.org/docs/current/index.html) for more information.

### Installing PostgreSQL

To install PostgreSQL, you can download the installer from the [official website](https://www.postgresql.org/download/). Choose the appropriate version for your operating system. For Windows, you can use the [EnterpriseDB installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

After downloading the installer, run it and follow the instructions. You can choose the default settings, but make sure to remember the username, password, and port number that you set during the installation.

In the final step, uncheck the checkbox that says "Launch Stack Builder at exit" and click "Finish" (this is not necessary for most users, and it can be confusing).

### Connecting to PostgreSQL from Python

Unlike SQLite, PostgreSQL is a client-server database, which means that you need to connect to a server in order to interact with the database. This is done using a library called `psycopg2`.

To install `psycopg2`, you can use `pip`:

```bash
pip install psycopg2
```

But if this does not work for you, you can also use the following command:

```bash
pip install psycopg2-binary
```

Which does the same thing, but skips some of the installation steps that can cause issues on some systems.

To connect to a PostgreSQL database from Python, you need to use the following code:

```python
import psycopg2

# Connect to the default database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
```

This code connects to the default database (`postgres`) using the default username (`postgres`) and password. Be sure to replace these values with the ones you set during the installation. Also, make sure to replace `localhost` with the IP address or hostname of the server where PostgreSQL is running (if it's not running on your local machine).

It's also a good idea to not include any of these values directly in your code, but to use environment variables or a configuration file instead.

### Creating a database

This is optional, but one advantage of PostgreSQL over SQLite is that you can create multiple databases on the same server. This can be useful for separating different projects or environments.

To create a new database in PostgreSQL, you can use the following code:

```python
import psycopg2

# Connect to the default database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Create a new database
cur.execute("CREATE DATABASE my_new_database")

# Close communication with the database
cur.close()
conn.close()
```

This code creates a new database called `my_new_database`. You can replace this with any name you like. The next time you connect to the server, you can use this new database instead of the default one:

```python
conn = psycopg2.connect(
    dbname="my_new_database",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
```

We can even create more users and grant them access to specific databases, but this is beyond the scope of this chapter.

### DictCursor / NamedTupleCursor

It's often useful to use a `DictCursor` instead of the default cursor, as it returns rows that can be used as dictionaries instead of "just" tuples. This can make it easier to work with the data in your code.

To use a `DictCursor`, simply add the `cursor_factory=DictCursor` parameter when connecting to the database.

This will enable you to access the rows as dictionaries:

```python
import psycopg2
from psycopg2.extras import DictCursor

# Connect to the default database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    cursor_factory=DictCursor
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")
row = cur.fetchone()
username = row["username"]
```

Alternatively, you can use a `NamedTupleCursor` to access the rows as named tuples:

```python
import psycopg2
from psycopg2.extras import NamedTupleCursor

# Connect to the default database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    cursor_factory=NamedTupleCursor
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")
row = cur.fetchone()
username = row.username
```

In both cases, you can still access the rows as tuples if you prefer (using `row[0]`, `row[1]`, etc.), and it's entirely up to you which method you prefer.

## VSCode and PostgreSQL

It's a good idea to install the `SQLTools` extension for VSCode, which allows you to connect to and interact with databases directly from the editor. This can be very useful for running queries, viewing tables, and more.

See complete instructions in the [official documentation](https://vscode-sqltools.mteixeira.dev/en/home).

You will also need to install the specific driver for PostgreSQL, which you can find in the [drivers section](https://vscode-sqltools.mteixeira.dev/en/drivers) or in the VSCode extensions marketplace search.

After installing the driver, you can connect to your PostgreSQL server by clicking on the "SQLTools" icon in the sidebar, then clicking on the "+" icon to add a new connection. You will need to enter the connection details (host, port, username, password, and database name) and test the connection, then save it.

Once you have a connection, you can run queries, view tables, and more directly from VSCode.

***An important note***: This may create a new file in your project called `.vscode/settings.json` which contains the connection details. Be sure to add this file to your `.gitignore` if you don't want to share your connection details (especially the password) with everyone in the world.
