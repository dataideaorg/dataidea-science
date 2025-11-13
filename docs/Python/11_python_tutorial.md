---
title: Python Quick Review
author: Juma Shafara
date: "2024-01"
date-modified: "2024-08-14"
description: This crash course will teach you the basics and advanced concepts of Python Programming
keywords: [python basics, variables, numbers, operators, containers, flow control, advanced, modules, file handling]
---


<!-- ![Photo by DATAIDEA](../../assets/banner4.png) -->

<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/aWbtHS0kMb8?si=6tZR8EXW600ng32J"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen>
  </iframe>
</div>

## Introduction

Python is a great general-purpose programming language on its own, but with the help of a few popular libraries (numpy, scipy, matplotlib) it becomes a powerful environment for scientific computing.

Whether you're a total beginner or seasoned programmer, this lesson will serve as a Python Quick Crash Course to refresh your Python knowledge

In this tutorial, we will cover:

<i class="bi bi-cursor"></i> Basic Python: Basic data types (Containers, Lists, Dictionaries, Sets, Tuples), Functions, Classes

## A Brief Note on Python Versions

We'll be using Python 3.10 for this iteration of the course. You can check your Python version at the command line by running `python --version`.


```python
# checking python version
!python --version
```

    Python 3.12.3


<!-- Newsletter -->
<div class="newsletter">
<h4>Don't Miss Any Updates!</h4>
<div class="newsletter-body">
<p>
Before we continue, we have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
(formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataideaorg"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no">
</iframe>
</div>
</div>

## Basics of Python

Python is a high-level, dynamically typed multiparadigm programming language. Python code is often said to be almost like pseudocode, since it allows you to express very powerful ideas in very few lines of code while being very readable. As an example, here is an implementation of the classic quicksort algorithm in Python:


```python
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [number for number in array if number < pivot]
    middle = [number for number in array if number == pivot]
    right = [number for number in array if number > pivot]
    return quicksort(left) + middle + quicksort(right)

quicksort([3,6,8,10,1,2,1])
```




    [1, 1, 2, 3, 6, 8, 10]




```python
sorted('listen', reverse=True)
```




    ['t', 's', 'n', 'l', 'i', 'e']



### Variables
Variables are stores of value


```python
name = 'Juma'
age = 19
id_number = 190045
```

#### Rules to consider
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Variable names should be meaningful eg `number` instead of `x`</li> 
<li><i class="bi bi-cursor"></i> Variable names should contain only alpha-numberic characters, and maybe under_scores</li> 
<li><i class="bi bi-cursor"></i> Variable names can only start with letters or an underscore</li> 
<li><i class="bi bi-cursor"></i> Variable name cannot contain special characters</li> 
<li><i class="bi bi-cursor"></i> Variables names are case sensitive</li> 
</ul>

## Examples of variables

For this course, we'll use snake case for *quick* variables


```python
name = 'Eva'
list_of_names = ['Eva', 'Shafara', 'Bob'] # snake case
```

we'll use camel case for function variables


```python
def calculateBMI(weight_kg, height_m): # camel case
    bmi = weight_kg / height_m ** 2
    rounded_bmi = round(bmi, 3)
    return rounded_bmi
```

finally, we'll use pascal case for class variables


```python
class MathFunction:    # Pascal Case
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3
```

### Basic data types

#### Numbers

Integers and floats work as you would expect from other languages:


```python
number = 3
print('Number: ', number)
print('Type: ', type(number))
```

    Number:  3
    Type:  <class 'int'>



```python
# Quick number arithmetics

print(number + 1)   # Addition
print(number - 1)   # Subtraction
print(number * 2)   # Multiplication
print(number ** 2)  # Enumberponentiation
```

    4
    2
    6
    9



```python
# Some compound assingment operators

number += 1 # number = number + 1
print(number)
number *= 2
print(number)
number /= 1 # number = number / 1
print(number)
number -= 2
print(number)
```

    4
    8
    8.0
    6.0



```python
number = 2.5
print(type(number))
print(number, number + 1, number * 2, number ** 2)
```

    <class 'float'>
    2.5 3.5 5.0 6.25



```python
# complex numbers
vector = 2 + 6j
type(vector)
```




    complex



#### Booleans

Python implements all of the usual operators for Boolean logic, but uses English words rather than symbols:


```python
t, f = True, False
type(t)
```




    bool



Now we let's look at the operations:


```python
# Logical Operators

print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;
```

    False
    True
    False
    True


#### Strings

A string is a sequence of characters under some quotes. Eg.



```python
hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter
print(hello, len(hello))
```

    hello 5



```python
# We can string in python
full = hello + ' ' + world  # String concatenation
print(full)
```

    hello world



```python
hw12 = '{} {} {}'.format(hello, world, 12)  # string formatting
print(hw12)
```

    hello world 12



```python
statement = 'I love to code in {}'
modified = statement.format('JavaScript')
print(modified)
```

    I love to code in JavaScript



```python
# formatting by indexing
statement = '{0} loves to code in {2} and {1}'
statement.format('Juma', 'Python', 'JavaScript')
```




    'Juma loves to code in JavaScript and Python'




```python
# formatting by name
statement = '{name} loves to code in {language1} and {language2}'
statement.format(language2='Python', name='Juma', language1='JavaScript')
```




    'Juma loves to code in JavaScript and Python'




```python
# String Literal Interpolation
name = 'Juma'
language1 = 'JavaScript'
language2 = 'Python'

statement = f'{name} loves to code in {language1} and {language2}'

print(statement)
```

    Juma loves to code in JavaScript and Python


String objects have a bunch of useful methods; for example:


```python
string_ = "hello"
print(string_.capitalize())  # Capitalize a string
print(string_.upper())       # Convert a string to uppercase; prints "HELLO"
print(string_.rjust(7))      # Right-justify a string, padding with spaces
print(string_.center(7))     # Center a string, padding with spaces
print(string_.replace('l', '(ell)'))  # Replace all instances of one substring with another
print('  world '.strip())  # Strip leading and trailing whitespace
```

    Hello
    HELLO
      hello
     hello 
    he(ell)(ell)o
    world



```python
statement = 'i love to code in Python '

capitalized = statement.capitalize()
upped = statement.upper()
replaced = statement.replace('Python', 'javascript')
statement.strip()
```




    'i love to code in Python'



You can find a list of all string methods in the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true">
</ins>


### Containers

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Python containers (collections) are objects that we use to group other objects</li> 
<li><i class="bi bi-cursor"></i> Python includes several built-in container types: lists, dictionaries, sets, and tuples.</li> 
</ul>

#### Lists

A list is an ordered collection of python objects or elements. A list can contain objects of different data types


```python
list_of_numbers = [3, 1, 2]   # Create a list
print(list_of_numbers)
print(list_of_numbers[2])
print(list_of_numbers[-1])     # Negative indices count from the end of the list; prints "2"
```

    [3, 1, 2]
    2
    2



```python
list_of_numbers[2] = 'foo'    # replacing a specific value in a list
print(list_of_numbers)
```

    [3, 1, 'foo']



```python
list_of_numbers.append('bar') # Add a new element to the end of the list
print(list_of_numbers)  
```

    [3, 1, 'foo', 'bar']



```python
last_item = list_of_numbers.pop()     # Remove and return the last element of the list
print(last_item)    # returns the last item 
print(list_of_numbers) # Modifies the original list
```

    bar
    [3, 1, 'foo']


Research on:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> `del` </li> 
<li><i class="bi bi-cursor"></i> `remove()`</li> 
</ul>

As usual, you can find all the gory details about lists in the [documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

#### Slicing

In addition to accessing list elements one at a time, Python provides concise syntax to access a range of values in a list; this is known as slicing:


```python
list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_of_numbers)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
print(list_of_numbers)         # Prints "[0, 1, 2, 3, 4]"
print(list_of_numbers[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(list_of_numbers[2:])     # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(list_of_numbers[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(list_of_numbers[:])      # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print(list_of_numbers[:-1])    # Slice indices can be negative; prints ["0, 1, 2, 3]"
list_of_numbers[2:4] = [8, 9] # Assign a new sublist to a slice
print(list_of_numbers)         # Prints "[0, 1, 8, 9, 4]"
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 3]
    [2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    [0, 1, 8, 9, 4, 5, 6, 7, 8, 9]


#### Loops

A `for loop` is used to loop through (or iterate) over a sequence of objects (iterable objects). Iterable objects in python include strings, lists, sets etc 

You can loop over the elements of a list like this:


```python
list_of_animals = ['cat', 'dog', 'monkey']

for animal in list_of_animals:
    print(animal)
```

    cat
    dog
    monkey



```python
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_of_squared_numbers = []

for number in list_of_numbers:
    list_of_squared_numbers.append(pow(number, 2))

list_of_squared_numbers
```




    [1, 4, 9, 16, 25, 36, 49, 64, 81, 0]



If you want access to the index of each element within the body of a loop, use the built-in `enumerate` function:


```python
animals = ['cat', 'dog', 'monkey']

for index, animal in enumerate(animals):
    print(f'{index}: {animal}')
```

    0: cat
    1: dog
    2: monkey


#### List comprehensions:


```python
numbers = [0, 1, 2, 3, 4]
squares = []

for number in numbers:
    squares.append(pow(number, 2))

print(squares)
```

    [0, 1, 4, 9, 16]


You can make this code simpler using a list comprehension:


```python
list_of_numbers = [0, 1, 2, 3, 4]

squares = [pow(number, 2) for number in list_of_numbers]

print(squares)
```

    [0, 1, 4, 9, 16]


List comprehensions can also contain conditions:


```python
numbers = [0, 1, 2, 3, 4]

even_squares = [pow(number, 2) for number in numbers if number % 2 == 0]

print(even_squares)
```

    [0, 4, 16]


Research:
<i class="bi bi-cursor"></i> How to combine lists

#### Dictionaries

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A dictionary is an unordered and mutable collection of items</li> 
<li><i class="bi bi-cursor"></i> A dictionary is created using curly brackets</li> 
<li><i class="bi bi-cursor"></i> Each item in a dictionary contains a key/value pair</li> 
</ul>


```python
# creating a dictionary
person = {
    'first_name': 'Juma',
    'last_name': 'Shafara',
    'age': 51,
    'married': True
}
person
```




    {'first_name': 'Juma', 'last_name': 'Shafara', 'age': 51, 'married': True}




```python
# accessing items in a dictionary
first_name = person['first_name']
last_name = person['last_name']
full_name = first_name + ' ' + last_name

# display
full_name
```




    'Juma Shafara'




```python
# add items to a dictionary
person['hobby'] = 'Coding'
person
```




    {'first_name': 'Juma',
     'last_name': 'Shafara',
     'age': 51,
     'married': True,
     'hobby': 'Coding'}




```python
email = person.get('email', 'email not available')
print(email)
```

    email not available



```python
# modifying a value in a dictionay
person['married'] = False
person
```




    {'first_name': 'Juma',
     'last_name': 'Shafara',
     'age': 51,
     'married': False,
     'hobby': 'Coding'}




```python
# remove an item from a dictionary
person.pop('age')
person
```




    {'first_name': 'Juma',
     'last_name': 'Shafara',
     'married': False,
     'hobby': 'Coding'}



Research:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> How to remove an item using the `del` method</li> 
<li><i class="bi bi-cursor"></i> How to iterate over objects in a dictionary</li> 
<li><i class="bi bi-cursor"></i> Imitate list comprehension with dictionaries</li> 
</ul>

You can find all you need to know about dictionaries in the [documentation](https://docs.python.org/3/library/stdtypes.html#dict).

#### Sets

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A set is an unordered, immutable collection of distinct elements. </li> 
<li><i class="bi bi-cursor"></i> A set is created using curly braces</li> 
<li><i class="bi bi-cursor"></i> The objects are placed inside the brackets and are separated by commas</li> 
<li><i class="bi bi-cursor"></i> As a simple example, consider the following:</li> 
</ul>


```python
animals = {'cat', 'dog'}

print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' not in animals)  # prints "True"
```

    True
    True



```python
animals.add('fish')      # Add an element to a set

print('fish' in animals) # Returns "True"

print(len(animals))       # Number of elements in a set;
```

    True
    3



```python
animals.add('cat')       # Adding an element that is already in the set does nothing
print(len(animals)) 
      
animals.remove('cat')    # Remove an element from a set
print(len(animals))       
```

    3
    2


Research:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> How to remove with `discard()`</li> 
<li><i class="bi bi-cursor"></i> How to remove with `pop()`</li> 
<li><i class="bi bi-cursor"></i> How to combine sets/li> 
<li><i class="bi bi-cursor"></i> How to get the difference between 2 sets</li> 
<li><i class="bi bi-cursor"></i> What happens when we have repeated elements in a set</li> 
</ul>

_Loops_: Iterating over a set has the same syntax as iterating over a list; however since sets are unordered, you cannot make assumptions about the order in which you visit the elements of the set:


```python
animals = {'cat', 'dog', 'fish'}

for index, animal in enumerate(animals):
    print(f'{index}: {animal}')
```

    0: fish
    1: cat
    2: dog


Set comprehensions: Like lists and dictionaries, we can easily construct sets using set comprehensions:


```python
from math import sqrt

print({int(sqrt(x)) for x in range(30)})
```

    {0, 1, 2, 3, 4, 5}


#### Tuples

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A tuple is an (immutable) ordered list of values. </li> 
<li><i class="bi bi-cursor"></i> A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:</li> 
</ul>


```python
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print(type(t))
print(d[t])       
print(d[(1, 2)])
```

    <class 'tuple'>
    5
    1



```python
# t[0] = 1
```

Research:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Creating a tuple</li> 
<li><i class="bi bi-cursor"></i> Access items in a tuple</li> 
<li><i class="bi bi-cursor"></i> Negative indexing tuples</li> 
<li><i class="bi bi-cursor"></i> Using range of indexes</li> 
<li><i class="bi bi-cursor"></i> Getting the length of items in a tuple</li> 
<li><i class="bi bi-cursor"></i> Looping through a tuple</li> 
<li><i class="bi bi-cursor"></i> Checking if an item exists in a tuple</li> 
<li><i class="bi bi-cursor"></i> How to combine tuples</li> 
<li><i class="bi bi-cursor"></i> Prove that tuples are immutable</li> 
</ul>

### Functions

<i class="bi bi-cursor"></i> A function is a group of statements that performs a particular task

<i class="bi bi-cursor"></i> Python functions are defined using the `def` keyword. For example:


```python
def overWeightOrUnderweightOrNormal(weight_kg:float, height_m:float) -> str:
    '''
    Tells whether someone is overweight or underweight or normal
    '''
    height_m2 = pow(height_m, 2)
    bmi = weight_kg / height_m2
    rounded_bmi = round(bmi, 3)
    if bmi > 24:
        return 'Overweight'
    elif bmi > 18:
        return 'Normal'
    else:
        return 'Underweight'

overWeightOrUnderweightOrNormal(67, 1.7)
```




    'Normal'



We will often use functions with optional keyword arguments, like this:


```python
bmi = calculateBMI(height_m=1.7, weight_kg=67)

print(bmi)
```

    23.183



```python
def greet(name:str='You')->str:
    """
    This function greets people by name
    Example1:
    >>> greet(name='John Doe')
    >>> 'Hello John Doe'
    Example2:
    >>> greet()
    >>> 'Hello You'
    """
    return f'Hello {name}'

# greet('Eva')
?greet
```

    [0;31mSignature:[0m [0mgreet[0m[0;34m([0m[0mname[0m[0;34m:[0m [0mstr[0m [0;34m=[0m [0;34m'You'[0m[0;34m)[0m [0;34m->[0m [0mstr[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    This function greets people by name
    Example1:
    >>> greet(name='John Doe')
    >>> 'Hello John Doe'
    Example2:
    >>> greet()
    >>> 'Hello You'
    [0;31mFile:[0m      /tmp/ipykernel_25670/2049930273.py
    [0;31mType:[0m      function


<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true">
</ins>

### Classes

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> In python, everything is an object</li> 
<li><i class="bi bi-cursor"></i> We use classes to help us create new object</li> 
<li><i class="bi bi-cursor"></i> The syntax for defining classes in Python is straightforward:</li> 
</ul>


```python
class Person:
    first_name = 'John'
    last_name = 'Tong'
    age = 20
```


```python
# Instantiating a class
object1 = Person()

print(object1.first_name)
print(object1.last_name)
print(object1.age)

print(f'object1 type: {type(object1)}')
```

    John
    Tong
    20
    object1 type: <class '__main__.Person'>



```python
# Instantiating a class
object2 = Person()

print(object2.first_name)
print(object2.last_name)
print(object2.age)
```

    John
    Tong
    20



```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self, name):
        return f'Hello {name}'
```


```python
object1 = Person('Juma', 'Shafara', 24)
print(object1.first_name)
print(object1.last_name)
print(object1.age)
print(type(object1))
```

    Juma
    Shafara
    24
    <class '__main__.Person'>



```python
object2 = Person('Eva', 'Ssozi', 24)
print(object2.first_name)
print(object2.last_name)
print(object2.age)
print(object2.greet('Shafara'))
print(type(object2))
```

    Eva
    Ssozi
    24
    Hello Shafara
    <class '__main__.Person'>



```python
class Student(Person):
    def __init__(self, first_name, last_name, age, id_number, subjects=[]):
        super().__init__(first_name, last_name, age)
        self.id_number = id_number
        self.subjects = subjects

    def addSubject(self, subject):
        self.subjects.append(subject) 
```


```python
student1 = Student('Calvin', 'Masaba', 34, '200045', ['math', 'science'])
```


```python
student1.addSubject('english')
```


```python
student1.subjects
```




    ['math', 'science', 'english']



Research:

<i class="bi bi-cursor"></i> Inheritance: This allows to create classes that inherit the attributes and methods of another class

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
