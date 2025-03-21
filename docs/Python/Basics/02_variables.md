---
title: Python Variables
author: Juma Shafara
date: "2023-11"
date-modified: "2024-08-14"
description: What are variables and how do we use them in Python?
keywords: [python, python programming, python variables]
---

![Photo by DATAIDEA](../assets/banner4.png)

## Variables

### Table of Contents

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Variables</li> 
<li><i class="bi bi-cursor"></i> Data Types</li> 
<li><i class="bi bi-cursor"></i> Numbers</li> 
<li><i class="bi bi-cursor"></i> Number Methods</li> 
<li><i class="bi bi-cursor"></i> Strings</li> 
<li><i class="bi bi-cursor"></i> Type Conversion</li> 
<li><i class="bi bi-cursor"></i> Python Booleans</li> 
<li><i class="bi bi-cursor"></i> Exercise</li> 
</ul>


<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Varibles are used to store values.</li> 
<li><i class="bi bi-cursor"></i> To create a variable, use the equal sign `(=)`.</li> 
</ul>

In the examples below, we create varibales name `fruit` and `name` and we assign them values `'mango'` and `'viola'` respectively


```python
fruit = 'mango'
name = 'voila'

# printing out
print(name, ' likes ', fruit )
```

    voila  likes  mango


### Rules to consider
Before choosing a variable name, consider the following.

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Spaces are not allowed in a variable name eg `my age = 34`</li> 
<li><i class="bi bi-cursor"></i> A variable name can not start with number eg `1name = 'Chris'`</li> 
<li><i class="bi bi-cursor"></i> Variable names can not have special characters eg `n@me = 'Comfort'`</li> 
<li><i class="bi bi-cursor"></i> Are case sensitive. Ie Name and name are not the same!</li> 
</ul>

Examples of good variable names


```python
character = 'Peter Griffin'
my_favorite_character = 'Stewie Griffin' # snake case
myFavoriteCharacter = 'Meg Griffin' # camel case
MyFavoriteCharacter = 'Brian Griffin' # Pascal case
```

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

## Data Types
In this section of the tutorial, you will learn the most basic data types in Python

### Numbers

These are two basic types of numbers and they are called:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> integer(numbers without decimal places)</li> 
<li><i class="bi bi-cursor"></i> floating point numbers(numbers with decimal places)</li> 
</ul>


```python
# python numbers
# Integers
age = 45
population = 45000000
```


```python
# Floating point numbers
height = 1.7
weight = 147.45
```

[Find More on Numbers Here <i class="bi bi-box-arrow-up-right" title="Get Started"></i>](./03_numbers.ipynb)

## Strings

Strings are simply text. A string must be surrounded by single or double quotes


```python
# Strings
name = 'Juma'
other_name = "Masaba Calvin"
statement = 'I love coding'
```

[Find More on Strings Here <i class="bi bi-box-arrow-up-right" title="Get Started"></i>](./03_strings.ipynb)

### Booleans
Boolean data type can only have on fo these values: `True` or `False`

<div class="alert text-white rounded" style="background: #3a6e68;"><h4>Note!</h4><p>The first letter of a Boolean is in upper case.</p></div>

Booleans are often the result of evaluated expressions.

Forexample, when you compare two numbers, Python evaluates the expression and returns either `True` or `False`


```python
print(5 == 5)
print(10 > 5)
print(20 < 10)
```

    True
    True
    False


These are often used in `if` statments.

In this example, if the value of the variable `age` is more than `18`, the program will tell the user that they are allowed to enter


```python
age = 19

if age > 18:
    print('You are allowed to enter.')
```

    You are allowed to enter.


<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>You will learn more about if statements later in the course</p></div>

#### Checking the Type of a Boolean
We can check the data type of a Boolean variable using the `type()` method.


```python
married = True
print(type(married))
```

    <class 'bool'>


### Lists
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A list is an ordered collection of data</li> 
<li><i class="bi bi-cursor"></i> It can contain strings, numbers or even other lists</li> 
<li><i class="bi bi-cursor"></i> Lists are written with square brackets (`[]`)</li> 
<li><i class="bi bi-cursor"></i> The values in lists (also called elements) are separated by commas (`,`)</li> 
</ul>


```python
# Lists
names = ['juma', 'john', 'calvin']
print(names)
```

    ['juma', 'john', 'calvin']


[Find More on Lists Here <i class="bi bi-box-arrow-up-right" title="Get Started"></i>](./05_containers.ipynb)

A list can contain mixed data types


```python
other_stuff = ['mango', True, 38]
print(other_stuff)
```

    ['mango', True, 38]


### Checking data types

To check the data type of an object in python, use `type(object)`, for example, below we get the data type of the object stored in names


```python
# Which data type
print(type(names))
```




    list



## Converting Types

#### Convert to String
The `str()` method returns the string version of a given object


```python
# convert an integer to a string
age = 45
message = 'Peter Griffin is '+ str(age) + ' years old'
print(message)
```

    Peter Griffin is 45 years old


#### Convert to Integer
The `int()` method returns the integer version of the given object.


```python
# Convert floating point to integer
pi = 3.14159
print(int(pi))
```

    3


#### Convert to Float
The `float()` method returns the floating point version of the given object.


```python
side = 4
print(float(side))
```

    4.0


## Exercise

Write a program to assign the number 34.5678 to a variable named “number” then
display the number rounded to the nearest integer value.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
