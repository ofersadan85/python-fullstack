# CSS - Cascading Style Sheets

***CSS*** is the standard language for styling web pages. It is used to define colors, fonts, layout, and much more. It is used together with HTML and can be generated with JavaScript or server-side languages such as Python.

## Styling HTML Elements

For simple one-time styling of a specific element, we can use the `style` attribute, always in the form of `style="property: value;"`. For example:

```html
<p style="color: red;">This is a red paragraph</p>
<p style="color: blue;">This is a blue paragraph</p>
```

To combine several styles, we can use the `;` separator. For example:

```html
<p style="color: red; font-size: 20px;">This is a red paragraph with a font size of 20px</p>
```

That style will be applied to that specific element, but also to every element inside it. For example:

```html
<p style="color: red;">This is a red paragraph
    <span>This is a span inside the paragraph</span>
</p>

Both the paragraph and the span will be red. If we apply a different style to an internal tree element, it will override the parent style. In other words, the most specific style will be applied.

```html
<p style="color: red;">This is a red paragraph
    <span style="color: blue;">But this is blue</span>
</p>
```

Styles will not be "removed" if a property has not been specifically overridden. For example:

```html
<p style="color: red; font-size: 40px">This is a red paragraph
    <span style="font-size: 20px;">Smaller, but still red</span>
</p>
```

## The `<style>` tag

Applying styles to individual elements is not very practical in most cases. We can use the `<style>` tag (inside the `<head>` section) to define styles for the entire page. For example:

```html
<head>
    <style>
        p {
            color: red;
        }
    </style>
</head>
```

This will cause every `<p>` element to be red. We can "select" elements by other ways, more on that later. This is also very convenient for defining multiple styles to the same elements, without inserting all those styles in the element itself. For example:

```html
<head>
    <style>
        p {
            color: red;
            font-size: 20px;
        }
    </style>
</head>
```

## CSS files

We can also define styles in a separate file, and then link to it from the HTML file. This is usually the best practice, because it allows us to separate the content from the style, replace the style easily, and reuse the style in multiple pages without writing it again.

To link to a CSS file, we use the `<link>` tag, inside the `<head>` section. For example:

```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

Now, we can define the styles in the `style.css` file:

```css
p {
    color: red;
}
```

## Selectors

### Element name

We can select elements in several ways. The most common way is by the element name. For example, to select all `<p>` elements, we use `p`:

```css
p {
    color: red;
}
```

We can also select several types of elements at once, by separating them with a comma. For example, to select all `<p>` and `<span>` elements, we use `p, span`:

```css
p, span {
    color: red;
}
```

### Class name

We can also select by class name. For example, to select all elements with the class `red`, we use `.red`:

```css
.red {
    color: red;
}
```

This will select elements that have that class name, so it will "catch" both `<p class="red">` and `<span class="red">` even if they are not the same element type, but will not catch `<p>` elements that do not have that class.

### Element ID

We can also select by element ID. For example, to select the element with the ID `main`, we use `#main`:

```css
#main {
    color: red;
}
```

This style will only apply to any element, of any type, of any class, but only if it has the ID `main`, for example `<p id="main">`.

### Complex selectors

We can combine selectors to create more complex selectors. For example, to select all `<p>` elements with the class `red`, we use `p.red`:

```css
p.red {
    color: red;
}
```

To select all `<p>` elements with the class `red` or `blue`, we use `p.red, p.blue`:

```css
p.red, p.blue {
    color: red;
}
```

We can even select elements that are inside other elements. For example, to select all `<span>` elements that are inside `<p>` elements, we use `p span` (note the space between the selectors):

```css
p span {
    color: red;
}
```

Which will apply like this:

```html
<p>This is not red <span>This is red</span></p>
```

But will not apply to any `<span>` that is not inside a `<p>`:

```html
<p>This is not red</p>
<span>This is not red</span>
```

There are many more ways to select elements, but these are the most common ones. There are even ways to select elements based on their position in the page, but we will not cover that here.

## Properties

There are many properties that we can use to style elements. Here is a partial list of the most common ones:

| Property | Description | Example |
| --- | --- | --- |
| `color` | The color of the text | `color: red;` |
| `background-color` | The background color of the element | `background-color: red;` |
| `font-size` | The size of the font | `font-size: 20px;` |
| `font-family` | The font family | `font-family: Arial;` |
| `font-weight` | The font weight (bold, normal, etc.) | `font-weight: bold;` |
| `text-align` | The text alignment (left, right, center, justify) | `text-align: center;` |
| `text-decoration` | The text decoration (underline, overline, line-through) | `text-decoration: underline;` |
| `border` | The border of the element | `border: 1px solid black;` |
| `border-radius` | The border radius (rounded corners) | `border-radius: 5px;` |
| `padding` | The padding of the element | `padding: 5px;` |
| `margin` | The margin of the element | `margin: 5px;` |
| `width` | The width of the element | `width: 100px;` |
| `height` | The height of the element | `height: 100px;` |
| `display` | The display type of the element (block, inline, inline-block, none) | `display: block;` |

### Padding and margin

As a side note, it's worth mentioning that padding and margin are not the same thing. Padding is the space inside the element, while margin is the space outside the element. In other words:

- Padding is the space between the borders of the element and its content, whatever that content is.
- Margin is the space between the borders of the element and the borders of the next element.

It's recommended to play around with your browser's developer tools to see how these properties work, and where each one is applied.

## CSS Units

There are several units that we can use to define sizes in CSS. The most common ones are:

| Unit | Description | Example |
| --- | --- | --- |
| `px` | Pixels. The most common unit. | `width: 100px;` |
| `em` | Relative to the font size of the element. | `width: 2em;` |
| `rem` | Relative to the font size of the root element (usually the `<html>` element). | `width: 2rem;` |
| `%` | Relative to the size of the parent element. | `width: 50%;` |

## CSS Colors

There are several ways to define colors in CSS. The most common ones are:

| Color | Description | Example |
| --- | --- | --- |
| `red` | The name of the color. There are many colors that can be used by name. | `color: red;` |
| `#ff0000` | The hexadecimal representation of the color. The first 2 digits are the red component, the next 2 are the green component, and the last 2 are the blue component. Each pair is in the (hex) range of `00-ff` | `color: #ff0000;` |
| `rgb(255, 0, 0)` | The RGB representation of the color. The first number is the red component, the second is the green component, and the last is the blue component. Each component is in the range of `0-255` | `color: rgb(255, 0, 0);` |
| `rgba(255, 0, 0, 0.5)` | The RGBA representation of the color. The first 3 numbers are the red, green and blue components, and the last is the alpha component (transparency). Each component is in the range of `0-255`, and the alpha component is in the range of `0-1` | `color: rgba(255, 0, 0, 0.5);` |

## Complete example

In this repository, you can find a complete example of a [simple HTML page](./example.html) which includes a [CSS styling example](./example.css). These files will be updated as we learn more about HTML and CSS.

## CSS Resources

CSS is very easy to start with, but is very complex to master. We won't cover all the details here, but here are some resources that you can use to learn more:

- [CSS MDN](https://developer.mozilla.org/en-US/docs/Web/CSS) - The official documentation for CSS
- [Bootstrap](https://getbootstrap.com/) - A popular (free) CSS & JavaScript framework
- [HTML Cheat Sheet](https://htmlcheatsheet.com/css/) - A cheat sheet for CSS, with interactive examples
