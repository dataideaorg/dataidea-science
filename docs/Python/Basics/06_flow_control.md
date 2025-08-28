---
title: Python Flow Control
description: Learn Programming for Data Science
keywords: [function, conditional statements, if, if else, if elif, lambda functions, loops, for loop, while loop]
author: Juma Shafara
date: "2023-11"
date-modified: "11-07-2024"
---

![Photo by DATAIDEA](../../assets/banner4.png)

Python control flow tools change the flow of how code is executed by the Python interpreter.

Since the Python interpreter executes code in a line-by-line manner, Python control flow tools help dictate what line(s) of code should run in a Python program. There are different types of control flow tools available to us in Python and we will go through them in detail in this lesson.

### Table of Contents
In this notebook, you'll learn the following

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Functions</li> 
<li><i class="bi bi-cursor"></i> Loops</li> 
<li><i class="bi bi-cursor"></i> Conditional Statements</li>  
</ul>

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

## Functions
A function in python is a group statements that perform a particular task

The function below calculates and returns one's body mass index rounded to 2 decimal places


```python
# This function calculates Body Mass Index
def calculateBodyMassIndex(weight_kg, height_m):

    body_mass_index = weight_kg / pow(height_m, 2)
    rounded_bmi = round(body_mass_index, 2)

    return rounded_bmi
```


```python
# lets try
calculateBodyMassIndex(67, 1.6)
```




    26.17



### Creating a function

To create a function, we need the following:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> The `def` keyword</li> 
<li><i class="bi bi-cursor"></i> A function name</li> 
<li><i class="bi bi-cursor"></i> Round brackets `()` and a colon `:`</li> 
<li><i class="bi bi-cursor"></i> A function body- a group of statements</li> 
</ul>


```python
def greeter():
    message = 'Hello'
    print(message)
```

<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4>A group of statements must have the same indentation level, in the example above, 4 whitespaces were used to indent the function body</div>

### Calling a Function

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> To execute a function, it needs to be called</li> 
<li><i class="bi bi-cursor"></i> To call a function, use its function name with parentheses `()`</li> 
</ul>


```python
greeter()
```

    Hello


### Function Parameters/Arguments

<i class="bi bi-cursor"></i> When calling a function, we can pass data using parameters/arguments

<i class="bi bi-cursor"></i> A *parameter* is a variable declared in the function. In the example below, `number1` and `number2` are parameter

<i class="bi bi-cursor"></i> The *argument* is the value passed to the function when its called. In the example below `3` and `27` are the arguments


```python
# define the function
def addNumbers(number1, number2):
    sum = number1 + number2
    print(sum)

# Call the function
addNumbers(3, 27)
```

    30



```python
# setting a default argument
def greet(name='you'):
    message = 'Hello ' + name
    print(message)

greet('Tinye')
greet()
```

    Hello Tinye
    Hello you


## Default Arguments:
A function can have default arguments.

It can be done using the assignment operator (`=`).

If you don't pass the argument, the default argument will be used instead.


```python
def hello(name = 'Agaba'):
    print('Hello ' + name)

hello('John') # calling with John
hello() # calling with no name
```

    Hello John
    Hello Agaba


###  Return Statement
The `return` statement is used to return a value to a function caller


```python
def addNumbers(number1, number2):
    sum = number1 + number2
    return sum

summation = addNumbers(56, 4)
print(summation)
```

    60


<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>The return statement stops the execution of a function.</p></div>

 ### lambda functions
 <ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Lambda functions (also called anonymous functions) are functions that donot have names</li> 
<li><i class="bi bi-cursor"></i> The body of a lambda function can only have one expression, but can have multiple arguments</li> 
<li><i class="bi bi-cursor"></i> The result of the expression is automatically returned</li> 
</ul>

  **Syntax:**
  ```python
  lambda parameters: expression
  ```


```python
# Example of lambda function
calculateBMI = lambda weight_kg, height_m: round((weight_kg/(height_m ** 2)), 2)

# Calling a labda function
calculateBMI(67, 1.7)
```




    23.18



<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>In the example above, the body mass index is automatically return, even without using the return statement</p></div>

### Practice functions

#### Calculate CGPA


```python
# Assume 4 course units
# 1. Math - A
# 2. Science - B
# 3. SST - B
# 4. English - C


def calculate_CGPA(GPs_list, CUs_list):
    length = len(GPs_list)
    product_sum = 0

    for item in range(length):
        product_sum += GPs_list[item] * CUs_list[item]

    CUs_sum = sum(CUs_list)

    CGPA = product_sum / CUs_sum

    return CGPA

# calculate_CGPA(4, 5)
```

#### Get someones age given birth month and year


```python
def getAge(month, year):
    month_diff = 12 - month
    year_diff = 2023 - year

    return str(year_diff) + ' years ' + str(month_diff) + ' months'  
    
age = getAge(year=2000, month=10) # keyword argument
age2 = getAge(10, 2000) # positional argument

print(age)
```

    23 years 2 months


## Loops 

<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/BqPsPkh5U4k?si=pwk_izEAXijmZbWI"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>


<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Loops are used to repetitively execute a group of statements</li> 
<li><i class="bi bi-cursor"></i> we have 2 types, `for` and `while` loop</li> 
</ul>

#### For Loop
A `for` loop is used to loop through or iterate over a sequence or iterable objects

**Syntax:**
```python
for variable in sequence:
    statements
```

### Looping through a list
The for loop is commonly used with lists.


```python
pets = ['cat', 'dog', 'rabbit']
# iterate through pets
for pet in pets:
    print(pet)
```

    cat
    dog
    rabbit


Here's another example to convert many weights from kilograms(kgs) to pounds(pds)


```python
# convert all weights in list from kg to pounds
weights_kg = [145, 100, 76, 80]
weights_pds = []

for weight in weights_kg:
    pounds = weight * 2.2
    rounded_pds = round(pounds, 2)
    weights_pds.append(rounded_pds)

print(weights_pds)
```

This example displays all letters in my name.


```python
# Display all letters in a name
name = 'Shafara'

for letter in name:
    print(letter)
```

    S
    h
    a
    f
    a
    r
    a


### While loop

The `while` loop executes a given group of statements as long as the given expression is `True`

**Syntax:**
```python
while expression:
    statements
```

In the example below, `Hello you` will be printed 5 times, that is for each time counter is still less than 5.


```python
counter = 0

while counter < 5:
    print('Hello you')
    counter += 1
```

    Hello you
    Hello you
    Hello you
    Hello you
    Hello you



```python
# Convert the weights in the list from kgs to pounds
weights_kg = [145, 100, 76, 80]
weights_pds = []

counter = 0
end = len(weights_kg)

while counter < end:

    pound = weights_kg[counter] * 2.2
    rounded_pds = round(pound, 3)
    weights_pds.append(rounded_pds)

    counter += 1

print(weights_pds)
```

    [319.0, 220.0, 167.2, 176.0]


## Conditional Statements
<!-- Video -->
<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/VJXESXuv9FU?si=ocfa6U9xaAmyBoEO"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>

Conditional statements in Python are fundamental building blocks for controlling the flow of a program based on certain conditions. They enable the execution of specific blocks of code when certain conditions are met. The primary conditional statements in Python include `if`, `elif`, and `else`.

### Basic Syntax

#### If Statement
The `if` statement is used to test a condition. If the condition evaluates to `True`, the block of code inside the `if` statement is executed.

```python
if condition:
    # block of code
```

Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

#### Else Statement
The `else` statement is used to execute a block of code if the condition in the `if` statement evaluates to `False`.

```python
if condition:
    # block of code if condition is True
else:
    # block of code if condition is False
```

Example:
```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

#### Elif Statement
The `elif` (short for else if) statement allows you to check multiple conditions. If the first condition is `False`, it checks the next `elif` condition, and so on. If all conditions are `False`, the `else` block is executed.

```python
if condition1:
    # block of code if condition1 is True
elif condition2:
    # block of code if condition2 is True
else:
    # block of code if none of the above conditions are True
```

Example:
```python
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")
```

### Nested Conditional Statements
Conditional statements can be nested within each other to handle more complex decision-making processes.

Example:
```python
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is greater than 10 but not greater than 20")
else:
    print("x is 10 or less")
```

### Conditional Expressions (Ternary Operator)
Python also supports conditional expressions, which allow for a more concise way to write simple `if-else` statements.

```python
variable = value_if_true if condition else value_if_false
```

Example:
```python
x = 10
result = "greater than 5" if x > 5 else "5 or less"
print(result)  # Output: greater than 5
```

### Combining Conditions
Multiple conditions can be combined using logical operators (`and`, `or`, `not`).

Example:
```python
x = 8
if x > 5 and x < 10:
    print("x is between 5 and 10")
```

### Practical Usage
Conditional statements are used in a wide variety of scenarios, such as:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Validating user input.</li> 
<li><i class="bi bi-cursor"></i> Controlling the flow of loops.</li> 
<li><i class="bi bi-cursor"></i> Implementing different behaviors in functions or methods.</li> 
<li><i class="bi bi-cursor"></i> Handling exceptions or special cases in data processing.</li> 
</ul>

Understanding and effectively using conditional statements are crucial for writing efficient and readable code in Python. They enable developers to build programs that can make decisions and respond dynamically to different inputs and situations.

### Exercise

Write a program which accepts a number (an amount of money to be paid by a
customer in rupees) entered from the keyboard. If the amount is greater than or equal to 1000 rupees, a
5% discount is given to the customer. Then display the final amount that the customer has to pay.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
