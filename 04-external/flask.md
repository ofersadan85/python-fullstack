# Flask

`flask` is a very popular web framework for Python. It is very easy to get started with, and it is very easy to get something up and running. It has some disadvantages, particularly when it comes to scaling (making your app serve thousands of users per second, for example), but it is a great tool for small projects.

## Installing Flask

To install `flask`, we can use `pip`:

```bash
pip install flask
```

## Hello World

Let's start with a simple "Hello World" app. Create a file called `main.py` and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run()
```

Now, run the file:

```bash
python main.py
```

You should see something like this:

```bash
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Congratulations! You have just created your first web app! You have a server running, which means you can go to your browser, enter the provided URL (<http://127.0.0.1:5000/>) and see your app in action!

## Hello World - Explained

It's worth inspecting this simple code line by line to see that it does:

```python
from flask import Flask
```

`Flask` is the main object class for creating a `flask` app. We import it from the `flask` package.

```python
app = Flask(__name__)
```

This line creates a new `flask` app. The `__name__` parameter is the name of the current module. Technically, this can be any string you want, (`app = Flask("my_app")`), but it is usually the name of the current module (which is always `__name__` in Python)

```python
@app.route("/")
```

This is a [decorator](../03-advanced/functions-decorators.md). It tells `flask` that the next function (`hello`) is a handler for the `/` route. In other words, when a user goes to the `/` route, the `hello` function will be called.

In that sense, we can think of the `app.route` we created as having two main goals:

- To map routes (URL paths) to functions, so when a user enters a specific route, a specific function will be called.
- To convert whatever the function returns to a valid [HTTP response](../05-web/http.md).

## Routes

The default route is `/`, which means that if we don't specify a route, the `/` route will be used. When you go to <https://google.com>, what you are really doing is requesting the `/` route from the `google.com` server, using the `https` protocol.

In Flask, routes are the way we map URLs to functions. For example, if we want to map the `/hello` route to a function called `hello`, we can do this:

```python
@app.route("/hello")
def hello():
    return "Hello World!"
```

Now, when a user goes to the `/hello` route, the `hello` function will be called.

## Returning HTML

So far, we have only returned plain text. But we can return HTML as well. For example:

```python
@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"
```

This is because by default, flask will take any string we return and convert it to a valid HTTP response. In this case, it will be a `text/html` response, which will tell our browser to treat it as html. We can also return other types of responses, such as JSON, which we will see later.

## Request methods

So far, we have only seen `GET` requests (which is the default). But there are other types of requests, such as `POST`, `PUT`, `DELETE`, etc. (See [HTTP Basics](../05-web/http.md) for more information). The `route` decorator can take an optional `methods` parameter, which is a list of methods that the route will accept. For example:

```python
@app.route("/hello", methods=["GET", "POST"])
def hello():
    return "<h1>Hello World!</h1>"
```

Now, the `/hello` route will accept both `GET` and `POST` requests. If we try to send a `PUT` request, we will get an error.

We can also declare different methods for the same route, and different functions for each method. For example:

```python
@app.route("/hello", methods=["GET"])
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/hello", methods=["POST"])
def hello_post():
    return "<h1>Hello World! (POST)</h1>"
```

Even though they both map to the same address path, they are different routes, because they have different methods. When an incoming HTTP request arrives, `flask` will check the method and call the appropriate function.

## URL parameters

So far, we have only seen routes without parameters. But we can also define routes with parameters. For example:

```python
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello {name}!</h1>"
```

Now, when a user goes to `/hello/John`, the `hello` function will be called, and the `name` parameter will be set to `John`.

This is the simplest way to define parameters, that will get passed toe the function. Notice that the parameter name in the function definition must match the parameter name in the route for this to work as is.

In the future, we will see more advanced ways to define parameters.

## Flask resources / documentation

- [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/) - The official documentation for `flask`. Contains many useful tutorials and examples about specific topics we will learn in the future, in which case we will link directly to the relevant page.
