# Flask "clone"

It can be sometimes useful to have to rewrite a library from scratch. It helps to understand how it works and to be able to modify it to fit your needs. The following is a very simplified version of the Flask web framework. It is not meant to be used in production, but it is a good exercise to understand how Flask works.

## The complete code

Let's start from the end with the complete code. We will then go through it step by step.

```python
import socket

http_response = """HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

{html}"""

not_found_response = """HTTP/1.1 404 NOT FOUND
Content-Type: text/html; charset=UTF-8

<h1>PAGE NOT FOUND 404</h1>"""


class Flask:
    def __init__(self, app_name, host="127.0.0.1", port=5000):
        self.app_name = app_name
        self.host = host
        self.port = port
        self.routes = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print(f"Listening on address {host}:{port}")

    def get_input(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Accepted client connection from {client_address}")
        data = client_socket.recv(4096)  # BLOCKS! Works like `data = input()`
        print(f"Received data from client: {data}")
        return (data, client_socket)

    def send_output(self, data, client_socket):
        client_socket.sendall(data)
        client_socket.close()

    def route(self, path, methods=("GET",)):
        def wrapper(normal_function):
            for method in methods:
                self.routes[(path, method)] = normal_function
            return normal_function
        return wrapper

    def run(self):  # app.run() in flask
        while True:
            data, client_socket = self.get_input()
            data = data.decode()  # bytes to str
            parts = data.split()  # ("GET", "/", "HTTP/1.1")
            method = parts[0]
            path = parts[1]

            if (path, method) in self.routes.keys():
                path_function = self.routes[(path, method)]
                path_response = path_function()
                response = http_response.format(html=path_response)
            else:
                response = not_found_response
            
            self.send_output(response.encode(), client_socket)
```

## Responses

We discussed HTTP responses in the [HTTP Basics](../05-web/http.md) chapter. We will use the same format here. We will have two responses: one for a successful request and one for a 404 error.

```python
http_response = """HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

{html}"""
```

This is our successful response. It contains the HTTP status code `200 OK` and the content type `text/html`. The `{html}` part will be replaced with the actual HTML content of the page.

```python
not_found_response = """HTTP/1.1 404 NOT FOUND
Content-Type: text/html; charset=UTF-8

<h1>PAGE NOT FOUND 404</h1>"""
```

This is our 404 response. It contains the HTTP status code `404 NOT FOUND` and the content type `text/html`. The HTML content is a simple `h1` tag with the text "PAGE NOT FOUND 404".

## The `Flask` class

We'll initialize with very basic parameters: the name of the app, the host and the port. The host and the port are by default the same as Flask's (and the name doesn't really matter in our case).

To be able to handle multiple routes, we will need to store them somewhere. We will use a dictionary with the key being a tuple of the path and the method, and the value being the function that handles the request.

The routes dictionary will look like this:

```python
{
    ("/", "GET"): index,
    ("/contact", "GET"): contact,
    ("/contact", "POST"): contact_post,
}
```

Note that `index`, `contact`, `contact_post` should be functions that are already defined. We don't call them here! We just pass them by name so we can get to them later, based on the path and method of the incoming request.

The `server_socket` is the socket that will listen for incoming connections. We will use it to accept connections, we won't dive to deep into sockets here, but you can think about it as if we're asking the operating system to update us if any message comes in on the address and port we specified.

## The `run` method

This is the heart of our example web framework. This is basically an infinite loop that will wait for requests (`self.get_input()`) and handle them by their route (`self.routes[(path, method)]`). To do this, we first need to parse the request, so we know what path and method it is requesting.

We also handle the case when the path and method are not found in our routes dictionary. In this case, we return a 404 response.

Note that we are using a very simple way to parse the request. We are just splitting the request by spaces and taking the first two parts. This is not a good way to parse requests, but it is good enough for our example.

We also assume that the route functions will always return strings that can be converted to HTML. So we're limited, compared to Flask, but it is good enough for now.

## The `route` decorator

This is the most complicated part of our example. We will use a decorator to register routes. The decorator will take the path and the methods as parameters. It will then return a function that will take the actual function as a parameter. This is a bit complicated, but it will make sense when we see it in action.

```python
def wrapper(normal_function):
    for method in methods:
        self.routes[(path, method)] = normal_function
    return normal_function
```

This inner part takes a "normal function" and registers it inside of our `routes` dictionary. By default, this includes only the `GET` method, but we allow the user to specify more methods if they want to. This function can now be used in any of the following ways:

```python
app = Flask("My App")

@app.route("/")
def index():
    return "<h1>INDEX</h1>"
```

OR

```python
app = Flask("My App")

def index():
    return "<h1>INDEX</h1>"

app.route("/")(index)
```

The first one is just a shortcut for the second one. Both of them mean the same thing, we just register the `index` function to the `/` path with the `GET` method.

Note: Unlike `flask` we do not alter the original function in any way. We just register it in our `routes` dictionary. This means that the function can be used normally, without any special requirements. We don't do any special checks about the arguments to the function, the return type, or anything else. `flask` does a lot of these checks, and it allows it to add more functionality, but it also makes it more complicated.

## Using our framework

Now that we have our framework, we can use it to create a simple website. Let's create a file called `main.py` and add the following code:

```python
from flask_clone import Flask

app = Flask("My App")

@app.route("/")
def index():
    return "<h1>INDEX</h1>"

@app.route("/contact", methods=("GET", "POST"))
def contact():
    return "<h1>CONTACT</h1>"
```

The complete code is available in the [flask_clone.py](./flask_clone.py) file.

## Limitations

You might have noticed that our framework is very limited. Primarily, it's a simple loop that "blocks" whenever it's waiting for a request. This means that it can only handle one request at a time. This is not a problem for a simple website (creating our simple text responses is very fast), but it is a big problem for a more complex website.

Additionally, we'll start having problems if we want to do anything interesting inside of our functions. For example, the `contact()` function can't really tell if the request is a `GET` or a `POST` request. It can't access the request body, the headers, or anything else. It can only return a string that will be sent back to the client.

These limitations are the reason why we use a framework like `flask` instead of writing our own. Someone has already solved these very common problems for us, and we can focus on writing our website instead of writing the framework.

## Real `flask`

It's very much worth looking at the actual [source code](https://github.com/pallets/flask) of `Flask`. It's a bit more complicated than our example, but it's still very readable. This is also a good time to have a look at the Flask [documentation](https://flask.palletsprojects.com/en/3.0.x/). It's very well written and contains a lot of examples we'll end up using.
