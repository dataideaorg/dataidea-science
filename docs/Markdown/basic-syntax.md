---
title: Markdown Basic Syntax
author: Juma Shafara
date: "2024-08-14"
description: Learn the fundamental elements of Markdown syntax for creating formatted documents
keywords: [markdown, syntax, headings, lists, formatting, links, images]
---

# Markdown Basic Syntax

This guide covers the most commonly used Markdown syntax elements. Learning these basics will enable you to create well-formatted documents quickly and easily.

## Headings

Headings are created using the hash (`#`) symbol. The number of hash symbols indicates the heading level:

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

Which renders as:

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Alternatively, for Heading 1 and Heading 2, you can use underlining with equals signs or dashes:

```markdown
Heading 1
=========

Heading 2
---------
```

## Paragraphs and Line Breaks

To create paragraphs, use blank lines to separate lines of text:

```markdown
This is the first paragraph.

This is the second paragraph.
```

For line breaks (without creating a new paragraph), end a line with two or more spaces and then press Enter:

```markdown
This is the first line.  
This is the second line.
```

## Emphasis (Bold and Italic)

You can make text bold or italic for emphasis:

### Italic

```markdown
*This text is italic*
_This text is also italic_
```

*This text is italic*  
_This text is also italic_

### Bold

```markdown
**This text is bold**
__This text is also bold__
```

**This text is bold**  
__This text is also bold__

### Combined Bold and Italic

```markdown
***This text is bold and italic***
___This text is also bold and italic___
**_This text is also bold and italic_**
```

***This text is bold and italic***  
___This text is also bold and italic___  
**_This text is also bold and italic_**

## Lists

Markdown supports both ordered (numbered) and unordered (bulleted) lists.

### Unordered Lists

Unordered lists can use asterisks (`*`), plus signs (`+`), or hyphens (`-`) as list markers:

```markdown
* Item 1
* Item 2
  * Subitem 2.1
  * Subitem 2.2
* Item 3

- Item 1
- Item 2
- Item 3

+ Item 1
+ Item 2
+ Item 3
```

Which renders as:

* Item 1
* Item 2
  * Subitem 2.1
  * Subitem 2.2
* Item 3

### Ordered Lists

For ordered lists, use numbers followed by periods:

```markdown
1. First item
2. Second item
3. Third item
   1. Subitem 3.1
   2. Subitem 3.2
4. Fourth item
```

Which renders as:

1. First item
2. Second item
3. Third item
   1. Subitem 3.1
   2. Subitem 3.2
4. Fourth item

**Note**: The actual numbers you use don't matter, as Markdown will always render the list in sequential order. For example, the following:

```markdown
1. First item
1. Second item
1. Third item
```

Will still render as a properly numbered list.

## Links

Markdown provides two ways to create links:

### Inline Links

```markdown
[Visit DataIdea](https://dataidea.org)
```

Which renders as: [Visit DataIdea](https://dataidea.org)

### Reference Links

You can also define links using reference-style syntax:

```markdown
[DataIdea site][1]
[GitHub][github]

[1]: https://dataidea.org
[github]: https://github.com
```

Which renders as:

[DataIdea site][1]  
[GitHub][github]

[1]: https://dataidea.org
[github]: https://github.com

## Images

Images in Markdown work similarly to links but with an exclamation mark (`!`) at the beginning:

### Basic Image Syntax

```markdown
![Alt text](image-url.jpg)
```

### Image with Title

```markdown
![Alt text](image-url.jpg "Image title")
```

### Image Size (Using HTML)

Markdown doesn't directly support image sizing, but you can use HTML:

```markdown
<img src="image-url.jpg" alt="Alt text" width="300" height="200">
```

## Blockquotes

To create a blockquote, use the greater-than symbol (`>`) before your text:

```markdown
> This is a blockquote.
> It can span multiple lines.
>
> It can also contain multiple paragraphs.
```

Which renders as:

> This is a blockquote.
> It can span multiple lines.
>
> It can also contain multiple paragraphs.

### Nested Blockquotes

```markdown
> This is a blockquote
>> This is a nested blockquote
```

Which renders as:

> This is a blockquote
>> This is a nested blockquote

## Horizontal Rules

To create a horizontal rule, use three or more asterisks, dashes, or underscores:

```markdown
***
---
___
```

Each of these will render as a horizontal line:

---

## Escaping Characters

If you want to show characters that are normally used for Markdown formatting, you can escape them with a backslash (`\`):

```markdown
\* This is not italic \*
\# This is not a heading
\[This is not a link](http://example.com)
```

Which renders as:

\* This is not italic \*  
\# This is not a heading  
\[This is not a link](http://example.com)

## Inline Code

To denote a word or phrase as code, enclose it in backticks (`` ` ``):

```markdown
Use the `print()` function in Python.
```

Which renders as:

Use the `print()` function in Python.

## Conclusion

These basic elements of Markdown syntax will help you create well-formatted documents. In the [next section](extended-syntax.md), we'll explore more advanced Markdown features like tables, code blocks, and task lists.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script> 