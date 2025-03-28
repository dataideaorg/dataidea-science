---
title: Markdown Extended Syntax
author: Juma Shafara
date: "2024-08-14"
description: Learn advanced Markdown syntax including tables, code blocks, footnotes, and more
keywords: [markdown, extended syntax, tables, code blocks, footnotes, task lists]
---

# Markdown Extended Syntax

While basic Markdown syntax provides the essential tools for document formatting, extended syntax offers additional features that enhance your documents. This guide covers the most useful extended Markdown syntax elements.

## Tables

Tables are created using pipes (`|`) and hyphens (`-`). Hyphens create the header row, while pipes separate the columns:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

Which renders as:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Column Alignment

You can align text in columns by adding colons (`:`) to the header separators:

```markdown
| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|---------------:|
| Left         | Center         | Right          |
| Left         | Center         | Right          |
```

Which renders as:

| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|---------------:|
| Left         | Center         | Right          |
| Left         | Center         | Right          |

## Fenced Code Blocks

While basic Markdown allows for code blocks using indentation (4 spaces or 1 tab), fenced code blocks provide a cleaner syntax and enable language-specific syntax highlighting.

To create a fenced code block, use three backticks (```) before and after the code block:

````markdown
```
function helloWorld() {
  console.log("Hello, world!");
}
```
````

Which renders as:

```
function helloWorld() {
  console.log("Hello, world!");
}
```

### Syntax Highlighting

You can specify a language after the opening backticks to enable syntax highlighting:

````markdown
```python
def hello_world():
    print("Hello, world!")
```
````

Which renders with Python syntax highlighting:

```python
def hello_world():
    print("Hello, world!")
```

Here are some common language identifiers:

- `python` for Python
- `javascript` or `js` for JavaScript
- `html` for HTML
- `css` for CSS
- `bash` or `shell` for shell scripts
- `sql` for SQL
- `r` for R
- `json` for JSON
- `yaml` or `yml` for YAML

## Footnotes

Footnotes allow you to add notes and references without cluttering the main content:

```markdown
Here's a sentence with a footnote reference.[^1]

[^1]: This is the footnote content.
```

Which renders as:

Here's a sentence with a footnote reference.[^1]

[^1]: This is the footnote content.

Footnotes can also have multiple paragraphs:

```markdown
Here's another sentence with a more complex footnote.[^2]

[^2]: This is the first paragraph of the footnote.
    
    This is the second paragraph of the footnote.
```

## Task Lists

Task lists (or checklists) are useful for tracking progress on a list of items:

```markdown
- [x] Complete task 1
- [x] Complete task 2
- [ ] Incomplete task 3
- [ ] Incomplete task 4
```

Which renders as:

- [x] Complete task 1
- [x] Complete task 2
- [ ] Incomplete task 3
- [ ] Incomplete task 4

## Definition Lists

Some Markdown processors support definition lists:

```markdown
term
: definition

another term
: definition 1
: definition 2
```

Which may render as:

<dl>
  <dt>term</dt>
  <dd>definition</dd>
  
  <dt>another term</dt>
  <dd>definition 1</dd>
  <dd>definition 2</dd>
</dl>

## Strikethrough

To cross out text, use double tildes:

```markdown
~~This text is crossed out~~
```

Which renders as:

~~This text is crossed out~~

## Automatic Links

URLs and email addresses can be turned into links automatically by enclosing them in angle brackets:

```markdown
<https://www.dataidea.org>
<email@example.com>
```

Which renders as:

<https://www.dataidea.org>  
<email@example.com>

## Emoji

Many Markdown applications support emoji shortcodes:

```markdown
:smile: :heart: :thumbsup:
```

Which might render as: 😄 ❤️ 👍

## HTML in Markdown

Most Markdown processors allow you to use HTML tags directly in your Markdown documents:

```markdown
<div style="color: red;">
  This text will be red.
</div>
```

<div style="color: red;">
  This text will be red.
</div>

## Highlight

Some Markdown implementations support highlighting text using double equals signs:

```markdown
==This text is highlighted==
```

Which may render as: <mark>This text is highlighted</mark>

## Superscript and Subscript

Some Markdown processors support superscript and subscript:

```markdown
X^2^ (superscript)
H~2~O (subscript)
```

Which may render as: X<sup>2</sup> (superscript)  
H<sub>2</sub>O (subscript)

## Disabling Automatic URL Linking

To prevent a URL from being automatically linked, you can wrap it in backticks:

```markdown
`https://www.example.com`
```

Which renders as: `https://www.example.com`

## Comments

You can add comments that won't appear in the rendered Markdown using HTML comment syntax:

```markdown
<!-- This comment won't appear in the rendered Markdown -->
```

## Conclusion

These extended Markdown features provide powerful tools for creating more complex and visually appealing documents. In the [next section](data-science.md), we'll focus on Markdown features specific to data science documentation, including math equations and diagrams.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script> 