---
title: Python Numbers
author: Juma Shafara
date: "2023-11"
date-modified: '2024-11-25'
description: What are the different types of Python Numbers
keywords: [python numbers, number types, number arithmetics, number methods]
---

![Photo by DATAIDEA](../../assets/banner4.png)

## Numbers

### Table of Contents
In this notebook, you will learn the following

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Number types </li> 
<li><i class="bi bi-cursor"></i> Number arithmetics</li> 
<li><i class="bi bi-cursor"></i> Number methods</li> 
</ul>

In python, there are three types of numbers

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Integer - `int`</li> 
<li><i class="bi bi-cursor"></i> Floating Point - `float`</li> 
<li><i class="bi bi-cursor"></i> Complex - `complex`</li> 
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

## Types

### Integer

An integer is a number without decimals


```python
# Python Numbers: intgers

a = 3
b = 4
number = 5

print('a:', a)
print('b:', b)
print('number:', number)
```

    a: 3
    b: 4
    number: 5


### Floating Point

A floating point number of just a float is a number with decimals


```python
# Python Numbers: floating point
a = 3.0
b = 4.21
number = 5.33

print('a:', a)
print('b:', b)
print('number:', number)
```

    a: 3.0
    b: 4.21
    number: 5.33


### Complex

A comple number is an imaginary number. To yield a complex number, append a `j` o `J` to a numeric value


```python
# Python Numbers: complex

a = 3j
b = 5.21j
number = 4 + 5.33j

print('a:', a)
print('b:', b)
print('number:', number)
```

    a: 3j
    b: 5.21j
    number: (4+5.33j)


## Number Arthmetics

Below are some of the basic arithmetic operations that can be performed with numbers


```python
# Python Numbers: arthmetics

summation = 4 + 2
print('sum:', summation)

difference = 4 - 2
print('difference:', difference)

product = 4 * 2
print('product:', product)

quotient = 4 / 2
print('quotient:', quotient)
```

    sum: 6
    difference: 2
    product: 8
    quotient: 2.0


## Number Methods

Number methods are special inbuilt functions used to work with numbers


```python
# sum() can add many numbers at once
summation = sum([1,2,3,4,5,6,7,8,9,10])
print(summation) # 55
```

    55



```python
# round() rounds a number to a 
# specified number of decimal places
pi = 3.14159265358979
rounded_pi = round(pi, 3)

print('PI: ', pi) # 3.14159265358979
print('Rounded PI: ', rounded_pi) # 3.142
```

    PI:  3.14159265358979
    Rounded PI:  3.142



```python
# abs() returns the absolute value of a number
number = -5
absolute_value = abs(number)
print(absolute_value) # 5
```

    absolute value of -5 is 5



```python
# pow() returns the value of 
# x to the power of y
four_power_two = pow(4, 2)
print(four_power_two) # 16
```

    16



```python
# divmod() returns the quotient and 
# remainder of a division
quotient, remainder = divmod(10, 3)
print(quotient) # 3
print(remainder) # 1
```

    Quotient: 3
    Remainder: 1


## Exercise

Write a program to assign the number 64.8678 to a variable named “number” then
display the number rounded to two decimal places.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
