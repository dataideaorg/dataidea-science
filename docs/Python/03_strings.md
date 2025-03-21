---
title: Python Strings
author: Juma Shafara
date: "2023-11"
date-modified: "2024-11-25"
description: What are strings and how do we use them in Python?
keywords: [python, python programming, python variables, strings]
---

![Photo by DATAIDEA](../assets/banner4.png)

## Strings

Strings are simply text. A string must be surrounded by single or double quotes

In this notebook, you will learn the following about strings

### Table of Contents

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> How to create strings</li> 
<li><i class="bi bi-cursor"></i> String methods</li> 
<li><i class="bi bi-cursor"></i> Exercise</li> 
</ul>

### House to create strings

We can create a string by writing any text and we enclose it in quotes. An example is as below


```python
# Strings
name = 'Juma'
other_name = "Masaba Calvin"
statement = 'I love coding'
```

## Single or double quotes?

Use single quotes when your string contains double quotes, or the vice versa.


```python
# when to use which quotes
report = 'He said, "I will not go home"'
```

<!-- Newsletter -->
<div class="newsletter">
<div class="newsletter-heading">
<h4><i class="bi bi-info-circle-fill"></i> Don't Miss Any Updates!</h4>
</div>
<div class="newsletter-body">
<p>
Before we continue, I have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
(formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no">
</iframe>
</div>
</div>

## String Methods
In this lesson, we will study some methods(functions) that can be used to work with strings.

### Capitalize String
The `capitalize()` function returns the string where the first letter is in upper case. 

Note that it doesn't modify the original string. 


```python
text = 'shafara loves coding'
capitalized_text = text.capitalize()
print(capitalized_text)
```

    Shafara loves coding


### Convert to Upper Case
The `upper()` function returns a copy of the given string but all the letters are in upper case.

Note that this does not modify the original string.


```python
text = 'JavaScript'
upper_text = text.upper()
print(upper_text)
```

    JAVASCRIPT


### Convert to Lower Case
The `lower()` function returns a copy of the given string but all the letter are in lower case.

Note that it does not modify the original text/string


```python
text = 'JavaScript'
lower_text = text.lower()
print(lower_text)
```

    javascript


### Get the lenght of a String
The length of a  string is the number of characters it contains

The `len()` function returns the length of a string. It takes on paramter, the string.


```python
text = 'JavaScript'
text_length = len(text)
print(text_length)
```

    10


### Replace Parts of a String.
The `replace()` method/function replaces the occurrences of a specified substring with another substring.

It doesn't modify the original string.


```python
text = 'shafara is a good girl'
corrected_text = text.replace('shafara', 'viola')
print(corrected_text)
```

    viola is a good girl


### Check if a Value is Present in a String
To check if a substring is present in a string, use the `in` keyword.

It returns `True` if the substring is found, otherwise `False`.


```python
text = 'shafara loves coding'
print('shafara' not in text)
```

    False


### Exercise

Write a program to convert a given character from uppercase to lowercase and vice
versa.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
