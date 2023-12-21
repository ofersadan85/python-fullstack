# HTML

***HTML*** (HyperText Markup Language) is the standard markup language for creating web pages and web applications. The file format itself is a text file with the extension `.html`, which all browsers can read and render.

## Basic HTML

The basic structure of an HTML document is as follows:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>This is a heading</h1>
        <p>This is a paragraph.<br>And a new line</p>
        <p>This is another paragraph</p>
    </body>
</html>
```

It's worth dissecting this a bit:

- `<!DOCTYPE html>`: This is the document type declaration. It tells the browser that this is an HTML5 document. This is **not** required for all HTML documents, but it's good practice to include it since this is the modern standard.
- `<html>`: This is the root element of the document. All other elements are nested inside this element.
- `<head>`: This is the element that contains metadata about the document. This is not visible to the user, but it contains information that the browser needs to render the page correctly. For example, the `<title>` element is used to set the title of the page, which is displayed in the browser tab.
- `<body>`: This is the element that contains the visible content of the page. This is what the user sees when they visit the page.
- `<h1>`: This is a heading element. There are six heading elements, `<h1>` through `<h6>`. The number indicates the importance of the heading, with `<h1>` being the most important (and by default, the biggest) and `<h6>` being the least important.
- `<p>`: This is a paragraph element. This is used to display text content.
- `<br>`: This is a line break element. This is used to create a new line inside a paragraph. Notice how it breaks the paragraph into two lines, differently than the division between the two `<p>` elements (both of which are paragraphs).

## HTML Tree Structure

HTML documents are structured as a tree. The root element is the `<html>` element, and all other elements are nested inside it. That means that the `<head>` and `<body>` elements are nested inside the `<html>` element, and the `<title>` element is nested inside the `<head>` element, and so on.

That also means that we need to tell the browser when an element ends. For example, if we want to create a paragraph, we need to tell the browser when the paragraph ends. We do that by using a closing tag, like this: `<p>This is a paragraph</p>`. Notice how the closing tag is the same as the opening tag, except it has a `/` in front of it.

In the example above, most elements have opening tags (`<html>`, `<head>`, `<title>`, `<body>`, `<h1>`, `<p>`) and closing tags (`</html>`, `</head>`, `</title>`, `</body>`, `</h1>`, `</p>`). However, some elements don't have closing tags. For example, the `<br>` element doesn't have a closing tag. This is because it doesn't contain any content, so it doesn't need a closing tag. The same goes for the `<img>` element, which is used to display images, the `<input>` element, which is used to create input fields, and a few others.

The example above can be thought of as a tree, like this:

```text
html
├── head
│   └── title
└── body
    ├── h1
    ├── p
    │   └── br
    └── p
```

Where each element can itself contain other tree structures, in more complex documents.

## HTML Attributes

HTML elements can have attributes. Attributes are used to provide additional information about an element. For example, all elements can have a `class` attribute, which is used to give the element a class. Classes are used to style elements using CSS. We'll get to that later.

Here is a partial list of some of the most common attributes:

| Attribute | Applies to | Description | Example |
| --- | --- | --- | --- |
| `class` | All elements | Used to give the element a class (useful for CSS) | `<p class="my-class">This is a paragraph</p>` |
| `id` | All elements | Used to give the element an id (useful for JavaScript) | `<p id="my-id">This is a paragraph</p>` |
| `href` | `<a>` | Used to give the link a URL | `<a href="https://google.com">Google</a>` |
| `src` | `<img>` | Used to give the image a URL | `<img src="https://example.com/image.jpg">` |
| `name` | `<input>` | Used to give the input field a name (useful for forms) | `<input name="my-input">` |
| `type` | `<input>` | Used to give the input field a type (useful for forms) | `<input type="text">` |

These (any many others) can be combined to create more complex elements. For example, here is an input field with a name (to identify it in the form), a placeholder (to give the user a hint about what to enter), a class (so we can later style it using CSS), an id (so we can later access it using JavaScript), and a type (to tell the browser what kind of input it is):

```html
<input name="input-name" placeholder="Enter your name" class="input-class" id="input-id" type="text">
```

## HTML Tables

HTML tables are used to display tabular data. They are created using the `<table>` element, and they contain rows, which are created using the `<tr>` element, and cells, which are created using the `<td>` element. Here is an example:

```html
<table>
    <tr>
        <td>Row 1, Column 1</td>
        <td>Row 1, Column 2</td>
    </tr>
    <tr>
        <td>Row 2, Column 1</td>
        <td>Row 2, Column 2</td>
    </tr>
</table>
```

This will create a table with two rows and two columns, but no headers. To add headers, we can use the `<th>` element instead of `<td>`, like this:

```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>Row 1, Column 1</td>
        <td>Row 1, Column 2</td>
    </tr>
    <tr>
        <td>Row 2, Column 1</td>
        <td>Row 2, Column 2</td>
    </tr>
</table>
```

## HTML Forms

HTML forms are used to collect user input. They are created using the `<form>` element, and they contain input fields, which are created using the `<input>` element. Here is an example:

```html
<form>
    <input type="text" name="name" placeholder="Enter your name">
    <input type="email" name="email" placeholder="Enter your email">
    <input type="password" name="password" placeholder="Enter your password">
    <input type="submit" value="Submit">
</form>
```

By default, the form will be submitted to the same URL as the page it's on. Using the [HTTP](./http.md) "GET" method, the data will be sent as part of the URL. In other words, the address bar will change to something like this: `example.html?name=John&email=john@example&password=123456` using the data from the form, or just `example.html?name=&email=&password=` if you left the fields empty when clicking submit.

Using the "POST" method, the data will be sent as part of the request body, and the address bar will not change. This is the preferred method for sending data to the server, since it's more secure (the data is not visible in the address bar) and it can contain more data (the URL has a length limit). To do that, we need to specify the method in the form element, like this:

```html
<form method="POST">
```

If we want to send the form data to another location that is not the current page, we need to specify the URL in the form element, like this:

```html
<form action="https://example.com/submit">
```

And of course, it is usually preferred to use a relative path (`/submit`) instead of an absolute path (`https://example.com/submit`). This is because the absolute path will not work if the website is moved to another domain, or during development when the website is running on a local server. Here is a common example using all of the above:

```html
<form method="POST" action="/submit">
    <input type="text" name="name" placeholder="Enter your name">
    <input type="email" name="email" placeholder="Enter your email">
    <input type="password" name="password" placeholder="Enter your password">
    <input type="submit" value="Submit">
</form>
```

## Input types

There are many different input types, and they all have different purposes. Here are some of the most common ones:

| Type | Description | Example |
| --- | --- | --- |
| `text` | A single line of text | `<input type="text">` |
| `email` | A single line of text, but the browser will validate that it's a valid email address (submit will not be possible otherwise) | `<input type="email">` |
| `password` | A single line of text, but the browser will hide the input (usually as dots) | `<input type="password">` |
| `number` | A single line of text, but the browser will validate that it's a valid number | `<input type="number">` |
| `checkbox` | A checkbox that can be checked or unchecked | `<input type="checkbox">` |
| `radio` | A radio button that can be selected or unselected. Radio buttons are usually grouped together, and only one can be selected at a time | `<input type="radio">` |
| `file` | A file upload field | `<input type="file">` |
| `button` | A button | `<input type="button">` |
| `submit` | A submit button | `<input type="submit">` |
| `reset` | A reset button | `<input type="reset">` |

Here is an example of a form with all of the above, it's recommeded to copy this into a file and open it in a browser to see how it looks and how each elements behaves:

```html
<form method="POST" action="/submit">
    <input type="text" name="text" placeholder="Enter text">
    <input type="email" name="email" placeholder="Enter email">
    <input type="password" name="password" placeholder="Enter password">
    <input type="number" name="number" placeholder="Enter number">
    <input type="checkbox" name="checkbox" value="1"> Checkbox
    <input type="radio" name="radio" value="1"> Radio 1
    <input type="radio" name="radio" value="2"> Radio 2
    <input type="file" name="file">
    <input type="button" name="button" value="Button">
    <input type="submit" name="submit" value="Submit">
    <input type="reset" name="reset" value="Reset">
</form>
```

## Other common HTML elements

There are many other common HTML elements, but we won't go over all of them here. Here are some of the most common ones:

| Element | Description | Example | Needs closing tag? |
| --- | --- | --- | --- |
| `<a>` | A link | `<a href="https://google.com">Google</a>` | Yes |
| `<img>` | An image | `<img src="https://example.com/image.jpg">` | No |
| `<div>` | A generic container, usually to apply some style to it | `<div>This is a div</div>` | Yes |
| `<span>` | A generic *inline* container, usually to apply some style to it | `<p>Hello <span>World</span> ! </p>` | Yes |
| `<ul>` | An unordered list | `<ul><li>Item 1</li><li>Item 2</li></ul>` | Yes |
| `<ol>` | An ordered list | `<ol><li>Item 1</li><li>Item 2</li></ol>` | Yes |
| `<li>` | A list item, must be contained inside a list | `<li>Item 1</li>` | Yes |
| `<br>` | A line break | `<p>This is a paragraph.<br>And a new line</p>` | No |

## Complete example

In this repository, you can find a complete example of a [simple HTML page](./example.html) that contains most of the elements we've discussed so far. You can open it in your browser to see how it looks. It also includes a [CSS styling example](./example.css), which we will discuss in the [CSS](./css.md) section.

## HTML Resources

- [HTML MDN](https://developer.mozilla.org/en-US/docs/Web/HTML) - The official HTML documentation from Mozilla, contains useful examples and explanations about each element.
- [HTML Cheat Sheet](https://htmlcheatsheet.com/) - A useful cheat sheet with all the most common HTML elements, you can use it to  test colors, attributes, and more.
