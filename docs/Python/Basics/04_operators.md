---
title: Python Operators
author: Juma Shafara
date: "2023-11"
date-modified: "2024-09-16"
description: This lesson will give an overview of Python Operators
keywords: [Python Operators]
body-header: This page was developed by Juma Shafara
---

![](../assets/banner4.png)

## What are Python Operators
Operators are symbols that perform operations on operands. Operands can be variables, strings, numbers, booleans etc

### Table of Contents

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> What are Python Operators</li> 
<li><i class="bi bi-cursor"></i> Arithmetic</li> 
<li><i class="bi bi-cursor"></i> Assignment</li> 
<li><i class="bi bi-cursor"></i> Comparison</li> 
<li><i class="bi bi-cursor"></i> The BMI Example</li> 
<li><i class="bi bi-cursor"></i> Identity</li> 
<li><i class="bi bi-cursor"></i> Logical</li> 
<li><i class="bi bi-cursor"></i> Membership</li> 
<li><i class="bi bi-cursor"></i> Exercise</li> 
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

## Arithmetic

Arithemators are symbols that perform mathematical operations on operands

Arithmetic Operator | Description
--------------------|--------------
`+`                 | Addition
`-`                 | Subraction
`/`                 | Division
`*`                 | Multiplication
`**`                | Exponentiates
`% `                | Remainder
`//`                | Floor Division


### Addition Operator
The *addition operator* returns the sum of its numerical operands


```python
# Addition
x = 10 
y = 5

summation = x + y
print(summation)
```

    15


It can also be used to concatenate or join strings together


```python
first_name = 'Juma '
last_name = 'Shafara'

full_name = first_name + last_name
print(full_name)
```

    Juma Shafara


### Subtraction Operator
The *subtraction operator* returns the difference of its numerical operands


```python
# Subraction
x = 10 
y = 5

difference = x - y
print(difference)
```

    5


### Multiplication Operator
The *multiplication operator* returns the product of its numerical operands


```python
# Multiplication
x = 10 
y = 5

product = x * y
print(product)
```

    50


### Division Operator
The *division operator* returns the quotient of its numerical operands.


```python
# Division
x = 10 
y = 5

quotient = x / y
print(quotient)
```

    2.0


### Exponentiation Operator
The *exponentiation operator* raises the left operand to the power of the right operand


```python
# Exponentiation
x = 10 
y = 5

exponent = x ** y
print(exponent)
```

    100000


### Remainder Operators
The *remainder operator*, also knows as the modulus operator returns the remainder after dividing the left operand by the right operand


```python
# Remainder
x = 10 
y = 5

remainder = x % y
print(remainder)
```

    0


### Floor Division Operator
The *floor division* rounds down the quotient of its numerical operands to the nearest whole number.


```python
# Floor Division
x = 10 
y = 5

floor = 10 // 4
print(floor)
```

    2


### Operator Sequence
Operator sequence describes the order of performed operations in an arithmetic expression.


```python
answer = 10 * 3 / 2 + 1
print(answer)
```

    16.0


## Assignment

Assignment operators are used to assign values to variables.

Name             | Operation | Same As
-----------------|------------|---------
Assignment       | `x = y` | `x = y`
Addition Ass     | `x += y`  | `x = x + y`
Subtraction Ass  | `x -= y` |`x = x - y`
Mult Ass         | `x *= y` | `x = x * y`
Division Ass     | `x /= y` | `x = x / y`
Expo Ass         | `x **= y` |`x = x ** y`
Remainder Ass    | `x %= y` | `x = x % y`
Floor Div Ass    | `x //= y` |`x = x // y`


### Assignment 
The *assignment operator* assigns a value to a variable


```python
# Assignment
number = 10
print(number)
```

    10


### Addition Assignment
The *addition assignment operator* adds the left and right operands and assigns the sum to the left operand (the variable)


```python
# Addition Ass
x += 5 # x = x + 5 => x = 10 + 5 => x = 15
print(x)
```

    15


### Subtraction Assignment
The *subtraction assignment operators* deducts the right operand and assigns the difference to the left operand (the variable)


```python
# Subraction Ass
x = 10
x -= 5 # x = x - 5 => x = 10 - 5 => x = 5
print(x)
```

    5


## Comparison

A comparison operator compares its operands and returns
a Boolean value based on whether the comparison is 
True of False

Name             | Operation
-----------------|------------
Equality         | `==`
Inequality       | `!=`
Greater than     | `>`
Less than        | `<`
Greater or equal | `>=`
Less or equal    | `<=`

### Equality
The *equality operator* compares two values and returns `True` if the operands are equal, otherwise returns `False`


```python
# Equality 
print('Voila' == 'Viola') # False
print(5 == 5) # True
```

    False
    True


### Inequality 
The inequality operator compares two values and returns `True` if the operands are **Not equal**, otherwise returns `False`


```python
# Inequality 
print('Voila' != 'Viola')
print(10 != 10)
```

    True
    False


### Greater than
The greater than operator returns `True` if the left operand is greater than the right operand, otherwise returns `False`.


```python
print(8 > 4) # True
print(5 > 10) # False
```

    True
    False


### Less than
The *less than operator* returns `True` if the left operand is less than the right operand, otherwise returns `False`


```python
print(10 < 15) # True
print(20 < 10) # False
```

    True
    False


### Greater than or equal to
The greater than or equal to operator returns `True` if the left operand is greater than or equal to the right operand, otherwise returns `False`


```python
# Greater or Equal
34 >= 43
```




    False



### Less than or equal to 
The **less than or equal to operator** returns `True` if the left operand **is less than or equal to** the right operand, otherwise returns `False`


```python
print(10 <= 15) # True
print(10 <= 10) # True
print(20 <= 10) # False
```

    True
    True
    False


## The Body Mass Index Example
In this example, we use the operators to calculate the body mass index of a person.


```python
weight = 56
height = 1.5

bmi = weight / (height**2)

print('BMI: ', bmi)
```

    BMI:  24.88888888888889


## Identity

Identity operators are used to compare two values to determine
if they point to the same object

Operator     | Name
-------------|------
`is`           | The is operator
`is not`      | The is not operator

### The `is` operator
This operator returns `True` if both operands point to the same object.


```python
# Example 1
x = 5
y = 4

print(x is y)
```

    False



```python
# Example 2
x = 5 
y = 4
z = x

print(x is y) # False
print(x is z) # True

```

    False
    True


### The `is not` operator
This operator return `True` if both operands **do Not** point to the same object in memory


```python
# Example
# is
x = 5
y = 4
z = x 

print(x is not y) # True
print(x is not z) # False

```

    True
    False


## Logical
Logical operators are commonly used with Booleans. In Python, there are 3 logical operators

Operator      |    Description
---------------|---------------
`and`            |   Logical and operator 
`or`              |  Logical or  
`not`              | Logical not 

### Logical `and`
The logical `and` operator returns `True` if both operands are `True`


```python
# Example
# Logical and
x = 4
print(x > 3 and 8 < x)
#               True and False => False
```

    False


### Logical `or`
The logical `or` operator returns `True` if one of the operands is `True`


```python
# Logical or
y = 7
expression_2 = 10 > y or 4 > y
#                   True or False => True
print(expression_2)
```

    True


### Logical `not`
The logical `not` operator returns `True` if the operand is `False`, otherwise returns `False` if the operand is `True`


```python
# Logical not
z = 8
expression_3 = not(10 == z)
#               not False => True
print(expression_3)
```

    True


## Membership

Membership operators are used to check if a sequence
is present in an object like a string, list etc

Operator          |Name
-----------------|------------
`in`               |The in operator
`not in`          |The not in operator

### The `in` operator
The `in` operator returns `True` if a sequence or value is present in an object


```python
# Example
name = 'Tinye Robert'
print('Robert' in name)
```

    True


### The `not in` operator
The `not in` operator returns `True` if a sequence or value is **NOT present** in an object


```python
# Example
name = 'Tinye Robert'
print('Robert' not in name)
```

    False


### Exercise

A car increases it velocity from u ms-1 to v ms-1 within t seconds. Write a program to
calculate the acceleration.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
