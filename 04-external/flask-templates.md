# Flask templates

Flask templates are HTML files that are rendered by the Flask app. They can be used to create dynamic web pages. This is made possible by the Jinja2 engine, which is built into Flask, but is also used by other frameworks, such as `Django` and `fastapi`, so it applies to them as well.

## Basic template

Let's start with a basic template. Create a file called `templates/index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My App</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

Now, let's render this template from our Flask app. Create a file called `main.py` with the following content:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

app.run()
```

This template does nothing very interesting, but it shows the basic structure of using a template:

- We import `render_template` from `flask`
- We use `render_template` to render the template, which is, to open the html file, and send it to the browser
- The file must be in a folder called `templates` (this is the default, but can be changed)

## Passing data to the template

Let's create a more interesting template. Replace the `<h1>` element in the previous example with the following:

```jinja
<h1>Hello {{ name }}!</h1>
```

Now, let's render the template with some data. Replace the `hello` function in `main.py` with the following:

```python
@app.route("/")
def hello():
    user_name = "John"
    return render_template("index.html", name=user_name)
```

Now, when we run the app, we should see "Hello John!" in the browser. The data contained in `user_name` is passed to the template, and is available in the template as `name`. The template replaces `{{ name }}` with the value of `name`, which is "John".

We can pass any data we want to the template, and use it in the template. For example, we can pass a list of names, and use it to create a list of names in the template. Replace the `hello` function in `main.py` with the following:

```python
@app.route("/")
def hello():
    user_names = ["John", "Jane", "Jack"]
    return render_template("index.html", name=user_names)
```

Although, this is not very useful, because by default the object (a `list` in this case) is just converted to a string, in order to be added to the page. We can do better than that. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello {{ name[0] }}!</h1>
```

Now, we should see "Hello John!" in the browser. So we can access a `list` by index just like we did in Python. Accessing a `dict` is also very similar. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello {{ user.name }}!</h1>
```

By doing that, we can now give the template a `dict` instead of a `list`. Replace the `hello` function in `main.py` with the following:

```python
@app.route("/")
def hello():
    user = {"name": "John"}
    return render_template("index.html", user=user)
```

Now, we should see "Hello John!" in the browser. So we can access a `dict` by key just like we did in Python, but the syntax of accessing the value is a bit different (`user.name` instead of `user["name"]`).

The `dict` itself can have too many keys, or missing keys, in comparing to what the template expects. This is fine! Unlike `str.format` in Python, will not fail / error / crash - it will just ignore the missing keys, and use the ones that are available. Missing keys will be replaced with an empty string.

## Loops in templates

We can also use loops in templates. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello {% for name in names %}{{ name }}{% endfor %}!</h1>
```

Now, we should see "Hello JohnJaneJack!" in the browser. Note that this is different from a simple `for` loop in Python, because we have to tell the template where the loop starts (`{% for name in names %}`) and where it ends (`{% endfor %}`), because spacing, newlines, and indentation are not significant in HTML.

This can also be user to render entire HTML blocks. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello everyone:</h1>
<ul>
    {% for name in names %}
        <li>{{ name }}</li>
    {% endfor %}
</ul>
```

Whatever is inside the loop, is "printed" on to the page for each iteration of the loop. So, in this case, the `<li>` element is printed for each name in the list, and the `<ul>` element is printed once, because it is outside the loop.

## Conditionals (if) in templates

We can also use conditionals in templates. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello {% if name == "John" %}John{% else %}everyone{% endif %}!</h1>
```

Now, we should see "Hello John!" in the browser. Like our loop we have to tell the template where the condition starts (`{% if name == "John" %}`) and where it ends (`{% endif %}`), because spacing, newlines, and indentation are not significant in HTML.

Again, this can be used to "print" entire HTML blocks. Replace the `<h1>` element in the template with the following:

```jinja
<h1>Hello Everyone:</h1>
<ul>
    {% for name in names %}
        {% if name == "John" %}
            <li>{{ name }}</li>
        {% else %}
            <li>{{ name }} (not John)</li>
        {% endif %}
    {% endfor %}
</ul>
```

Remember, you can use an `if` without an `else`, an `if` with several `elif` for other conditions, or an `if` with both `elif` and `else`. But at the end, you **must** have an `endif` in a template.

## Including other templates

We can also include other templates in a template. This is useful for reusing parts of a template in multiple places. Create a file called `templates/header.html` with the following content:

```jinja
<h1>Current user: {{ name }}</h1>
```

Now, replace the `<h1>` element in the template with the following:

```jinja
<p>Before</p>
{% include "header.html" %}
<p>After</p>
```

The `include` tag will include the content of the template in the current template. So, in this case, the `<h1>` element will be included in the template, and the result will be:

```html
<p>Before</p>
<h1>Current user: John</h1>
<p>After</p>
```

Notice that this also includes any data that was passed to the template. The variable `name` is available in the included template, because it was passed to the template that includes it.

## Extending other templates

The opposite of including a template, is extending a template. This is useful for creating a base template, and then extending it in other templates. Create a file called `templates/base.html` with the following content:

```jinja
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My App</title>
  </head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>
```

And replace the contents of `templates/index.html` with the following:

```jinja
{% extends "base.html" %}

{% block content %}
    <h1>Hello World!</h1>
{% endblock %}
```

The `extends` tag tells the renderer (flask) that this template extends another template. The `block` tag tells the renderer that this block can be overridden in the template that extends this template. In other words, anything from `index.html` that is inside the `content` block, will replace the `content` block in `base.html`. The result will be complete HTML page.

This is very useful when you have a basic template that you want to extend in multiple other templates. For example, you can have a `base.html` that contains the header and footer of your website, common CSS styles, JavaScript files, and then extend it in other templates that contain the content of each page.

This makes each template simpler, smaller, and easier to maintain.

## Complete example

Will be added soon

## Resources

- [Jinja2 documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Flask documentation - Templates tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/)
- [Flask documentation - Templates](https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates)
