# Environment Variables - Production vs. Development

Environment variables play a crucial role in modern software development by allowing developers to manage application configurations separately from the code. This separation is crucial for several reasons, including security, flexibility, and the ability to run the same application in different environments.

## Why we use Environment Variables

1. **Security:** Environment variables help keep sensitive information, such as database passwords or API keys, out of the source code. This prevents sensitive data from being exposed in version control systems.

2. **Flexibility:** They allow configurations to be changed without modifying the code. For instance, changing the database URL between development, staging, and production environments can easily be done through environment variables without any code changes.

3. **Environment-specific settings:** Environment variables enable developers to customize application behavior for different environments. For example, enabling debug mode in development for more verbose logging, while keeping it off in production for performance and security reasons.

## Production vs. Development Environments

### Development Environment (AKA "Dev mode")

- **Purpose:** Used by developers to write and test code.
- **Characteristics:** Features like debug mode are enabled to provide detailed error messages and allow live reloading of code (for example, in `flask`). Security and performance optimizations may be relaxed to ease the development process.
- **Example Uses:** Testing new features, debugging, and performing integration tests.

### Production Environment (AKA "Prod mode")

- **Purpose:** The live environment where the application is accessible to end-users in the real world.
- **Characteristics:** Optimized for security and performance. Debug mode is disabled, error messages are less detailed to avoid exposing sensitive information, and logging is configured for monitoring and alerting.
- **Example Uses:** Hosting the live application, handling real user requests, and data processing in a secure and optimized manner.

#### Other Environments

More rarely (but still often in many organizations), there are other environments such as "staging" or "testing" that are used to test the application in a production-like environment before deploying it to the live production environment. These environments may have their own environment variables and configurations. For simplicity, we'll focus on development and production environments in this explanation, but the same principles apply to other environments.

## Flask

More specifically to our course subject, Flask uses environment variables extensively to manage application configurations. The `FLASK_DEBUG` environment variable is used to distinguish between development and production environments. When `FLASK_DEBUG` is set (to any value), Flask enables debug mode, auto-reloader, and more verbose error pages, which are helpful during development. For production, we won't include `FLASK_DEBUG` as a variable to ensure that these features are disabled for security and performance reasons.

There are many other flask-specific environment variables that can be used to configure the application, all of them are listed in the [official documentation](https://flask.palletsprojects.com/en/3.0.x/config/).

## Working example

Let's consider a simple example of how environment variables can be used in a Flask application. We'll use the `python-dotenv` package to manage environment variables in a `.env` file. This package allows us to define environment variables in a `.env` file and load them into the application using the `os` module.

Read more about `python-dotenv` [here](https://pypi.org/project/python-dotenv/).

First, we need to install the `python-dotenv` package using pip:

```bash
pip install python-dotenv
```

Or added to our `requirements.txt` file along with other packages:

```plaintext
Flask==3.0.2
python-dotenv==1.0.1
```

Next, we create a `.env` file in the root directory of our project and define environment variables in it:

```plaintext
FLASK_DEBUG=True  # Set to any value to enable debug mode
FLASK_SECRET_KEY=supersecret
DATABASE_FILE=data.db
FRONTEND_URL=http://localhost:3000
```

Notice that we've defined environment variables for the Flask environment, secret key, database file, and frontend URL. Any environment variable that starts with `FLASK_` will be loaded into our `app.config` automatically by Flask (but only after we load the `.env` file).

Then, we load these environment variables into our Flask application using the `python-dotenv` package:

```python
# main.py

import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file. Must come before we use any of the variables or create the app object.
app = Flask(__name__) # Create a Flask app
FRONTEND_URL = os.environ["FRONTEND_URL"] # Get the value of the FRONTEND_URL environment variable. We'll get an error if it's not defined.
print(app.config["DEBUG"]) # We won't get an error if it's not defined by us, because Flask will set it to False by default.

@app.route("/")
def index():
    return f"Hello from the Flask backend! The frontend URL is {FRONTEND_URL}"
```

## Best Practices

- **Always** Use environment variables for sensitive information such as API keys, database passwords, and secret keys.
- **Always** Use environment variables for environment-specific configurations such as debug mode, logging level, and database URLs.
- **Never** Hardcode sensitive information directly into the code.
- **Never** Commit `.env` files to version control systems. Make sure to add them to `.gitignore` so you don't accidentally commit them, ever.
- The syntax for `.env` files is `KEY=VALUE`. There are no spaces allowed around the `=` sign. Comments are allowed and start with `#` (Like in Python). Everything is interpreted as a string (`str`), so no quotes are needed around the values (and remember to convert them to the correct type if needed in your code).
