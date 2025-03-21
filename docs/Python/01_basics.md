---
title: Python Basics
keywords: [What is Python, What is Python used for?, Python Displaying output]
description: In this notebook, I want to observe any trends related to customers.
author: Juma Shafara
date: "2023-09"
date-modified: "2024-11-25"
--- 

![Photo by DATAIDEA](../assets/banner4.png)

## Overview

This course will teach you the basics and advanced concepts of Python Programming. 

### Table of Contents
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Python Overview</li> 
<li><i class="bi bi-cursor"></i> Introduction</li> 
<li><i class="bi bi-cursor"></i> Installing</li> 
<li><i class="bi bi-cursor"></i> Writing Code</li> 
<li><i class="bi bi-cursor"></i> Displaying Output</li> 
<li><i class="bi bi-cursor"></i> Statements</li> 
<li><i class="bi bi-cursor"></i> Syntax</li> 
<li><i class="bi bi-cursor"></i> Comments</li> 
<li><i class="bi bi-cursor"></i> Exercise</li> 
</ul>

You can watch the full crash course on our YouTube channel [Programming for Data Science](https://www.youtube.com/watch?v=aWbtHS0kMb8) 


### Prerequisites

What do you need before learning Python?

1. Computer Literacy
2. Knowledge of installing a software
3. A compiler

### Python is Easy
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> To learn Python, you don't need any prior knowledge of experience on programming.</li> 
<li><i class="bi bi-cursor"></i> Python is human readable, making it easier to understand.</li> 
<li><i class="bi bi-cursor"></i>  Take alook at this example</li> 
</ul>


```python
x = 4
y = 3
summ = x + y
print(summ)
```

    7


Although we have not taught you how to code in Python yet, you can still easily pick up what the code is doing

<!-- Newsletter -->
<div class="newsletter">
<div class="newsletter-heading">
<h4><i class="bi bi-info-circle-fill"></i> Don't Miss Any Updates!</h4>
</div>
<div class="newsletter-body">
<p>
Before we continue, we have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
(formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no">
</iframe>
</div>
</div>

## What is Python
<i class="bi bi-cursor"></i> Python is a programming language.

<i class="bi bi-cursor"></i> Python is one of the most popular programming languages

### Who created Python?
Python was created by Guido van Rossum and it was first implemented in 1989

### What is Python used for?
Python is used for:
1. Web Development
2. Machine Learning
3. Data Science
4. Scripting
5. And many more

### What is the latest version of Python?
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Python 3 is the latest version of Python</li> 
<li><i class="bi bi-cursor"></i> This tutorial is based on the standards of Python 3</li> 
</ul>

## Installing Python
Before you can run Python on your PC, you need to install it first. 

To install Python in a PC, go to [https://www.python.org/downloads/](https://www.python.org/downloads/) then download the latest version.

After that, install it just like how you install other apps.

Make sure that you check "Add Python to PATH" for easier installation.

## Writing Python Code
In order to learn Python, you need to be able to write and execute code.

### Python Console (Shell)
Python console also known as shell allows you to execute Python code line by line

Assuming that you have already installed Python on your PC, you can access the Python console by opening the command prompt and typing `python`

Let's start using the console

Type the following and hit enter

```
name = 'Juma Shafara'
```
Again, type the following and hit enter
```
print(name)
```
After that, you should see this
```
Juma Shafara
```

![Python Console](python_console.png)

### Python Files 
Python files are saved with `.py` file extension

You can use any text editor (even notepad) to create Python files

Just make sure that you save them with the `.py` extension, forexample `hello.py`.

Copy this code and save it as `hello.py`:
```
print('Hello World!')
```
To run this Python file on a PC, navigate to the folder where is is located using the command prompt.

Then type the following and hit enter
```
python hello.py
```
The console should then output:
```
Hello World!
```

## Integrated Development Enviroment

To continue practicing Python smoothly, I advice using an Integrated Development Environment. This is just a software that has features built in for you to get moving with your coding practice with ease. 

Examples include:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> PyCharm</li> 
<li><i class="bi bi-cursor"></i> Jupyter Notebook</li> 
<li><i class="bi bi-cursor"></i> Thonny</li> 
<li><i class="bi bi-cursor"></i> Visual Studio Code</li> 
</ul>

Watch this video to see how to set up Visual Studio Code for Python Programming



<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/9o4gDQvVkLU"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen>
  </iframe>
</div>

## Python Displaying output

To display an output in Python, use the `print()` function.


```python
print('Hello world!')
```

    Hello world!



```python
print(27)
```

    27



```python
print(3 + 27)
```

    30


## Printing two objects

The `print()` function can be used to print two objects. Eg.


```python
print('Hello', 'Juma')
```

    Hello Juma



```python
x = 3
y = 7
summ = x + y
print('the sum is ', summ)
```

    the sum is  10



```python
x = 4; y = 3; print(x + y)
```

    7


## Python Statements

A python statement is used to write a value, compute a value, assign a value to a variable, call a functino and many more. Eg.


```python
x = 5
y = 3
summ = x + y
print(summ)
```

    8


In the example above, we have 4 lines of code. In python, each line typically contains one statement

### Multiple statements in one line

You can also write multiple statements in a single of code. Simply separate the statements with semicolons `;`


```python
a = 4; b = 3; sum = a + b; print(sum) 
```

    7


## Python Syntax
When coding in Python, we follow a syntax. Syntax is the set of rules followed when writing programs

### Python indentation

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> In python, indentation indicates a block(group) of statements</li> 
<li><i class="bi bi-cursor"></i> Tabs or leading whitespaces are used to compute the indentation level of a line</li> 
<li><i class="bi bi-cursor"></i> It depends on you whether you want to use tabs or whitespaces, in the example below, we use 2 whitespaces</li> 
</ul>


```python
number1 = 4
number2 = 3

if number1 > number2:
  x = 'Hello, world'
  print(x)
```

    Hello, world


## Python Comments

- Comments in Python are used to clarify or explain codes
- Comments are not interpreted by Python, meaning comments will not be executed


```python
# this is a comment
x = 4 
y = 3

# some comment
# second comment
# third comment

print(x + y) # prints out the sum
```

    7


## Excercise

Write a Python program to display the following text on the screen.

```
DATAIDEA
Sir Apollo Kagwa Road,
Kampala,
Uganda
-------------------
www.dataidea.org
```

## End of first module

The nice introduction ends here, in the next section, we will look at variables in Python.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
