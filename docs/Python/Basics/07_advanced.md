---
title: Python Advanced
description: Learn Advanced Python concepts like classes and objects, formatted strings, handling errors and variable scopes.
keywords: [python advanced, classes and objects, formatted strings, handling errors, variable scopes]
author: Juma Shafara
date: "2023-11"
date-modified: "2024-07-23"
---

![Photo by DATAIDEA](../assets/banner4.png)

In this notebook, we will explore some fundamental concepts in Python that are essential for writing clean, efficient, and maintainable code. These concepts include:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Classes and Objects</li> 
<li><i class="bi bi-cursor"></i> Formatted Strings</li> 
<li><i class="bi bi-cursor"></i> Handling Errors</li> 
<li><i class="bi bi-cursor"></i> Variable Scopes</li> 
</ul>

<!-- Newsletter -->
<div class="newsletter">
<div class="newsletter-heading">
<h3><i class="bi bi-info-circle-fill"></i> Don't Miss Any Updates!</h3>
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

## Classes and Objects


In Python, everything is an object. A class helps us create objects.

### Creating a Class

Use the `class` keyword to create a class

Here is the syntax:
```py
class className:
    statement(s)
```

Below is an example:


```python
class Person:
    first_name = "Betty"
    last_name = "Kawala"
    age = 30
```

### Instantiating a class
Now we can ceate an object from the class by instantiating it.

To instantiate a class, add round brackets to the class name.


```python
person_obj1 = Person()

type(person_obj1)
```




    __main__.Person



After instantiating a class, we can now access the object's properties.


```python
# print attributes
print(person_obj1.first_name)
print(person_obj1.last_name)
print(person_obj1.age)
```

    Betty
    Kawala
    30


## Class Attributes

A class can have attributes. Forexample the Person Class can have attributes like the `name`, `height` and `feet`


```python
class Person:
    def __init__(self, name, height, feet):
        self.name = name
        self.height = height
        self.feet = feet
```

<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>For now, focus on the syntax. Later we will explain the <code>__init__()</code> function and the <code>self</code> parameter.</p></div>

Now that our class is ready, we can now instantiate it and provide values to it's attributes.

This process can also be called "creating an instance of a class".

An instance is simply the object created from a class

In this example, `person_obj1` is a unique instance of the person class. 


```python
# create a class instance
person_obj = Person(
    name='Betty Kawala', 
    height=1.57, 
    feet=4
    )
```

After that, we can now access the properties of the instance (object)


```python
# accessing the properties
print('Name:', person_obj.name)
print('Height:', person_obj.height)
print('Feet:', person_obj.feet)
```

    Name: Betty Kawala
    Height: 1.57
    Feet: 4


The `self` parameter allows us to access the attributes and methods of a class

The `__init__()` function allows us to provide values for the attributes of a class

### Instances are unique

Let's say you have 500 people and you need to manage their data.

It is inefficient to create a variable for each of them, instead, you can create unique instances of a class.

In this example, the student1 and student2 instances are different from each other


```python
class Student:
  def __init__(self, id_number, name, age):
    self.id_number = id_number
    self.name = name
    self.age = age

student1 = Student(5243, "Mary Doe", 18)
student2 = Student(3221, "John Doe", 18)

print("Student 1 ID:", student1.id_number)
print("Student 1 Name:", student1.name)
print("Student 1 Age:", student1.age)

print("---------------------")

print("Student 2 ID:", student2.id_number)
print("Student 2 Name:", student2.name)
print("Student 2 Age:", student2.age)
```

    Student 1 ID: 5243
    Student 1 Name: Mary Doe
    Student 1 Age: 18
    ---------------------
    Student 2 ID: 3221
    Student 2 Name: John Doe
    Student 2 Age: 18


## Methods
Methods are functions that can access the class attributes. 

These methods should be defined (created) inside the class


```python
class Person:
    def __init__(self, name, height, feet):
        self.name = name
        self.height = height
        self.feet = feet
        
    def jump(self):
        return "I'm jumping " + str(self.feet) + " Feet"
```


```python
person_obj1 = Person(name='Juma', height=1.59, feet=5)

print(person_obj1.jump())
```

    I'm jumping 5 Feet


As you may notice, we used the `self` parameter to access the `feet` attribute

You can also pass an argument to a method.


```python
class Student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age

    def greet_student(self, greetings):
        print("Hello" + self.name + ", " + greetings)

student1 = Student(43221, "Agaba Calvin", 18)

# the string below will be passed as 
# the value of the greetings parameter
student1.greet_student("Welcome to this Python Tutorial!")
```

    HelloAgaba Calvin, Welcome to this Python Tutorial!


## Python Inheritance

Inheritance is a feature that allows us to create a class that inherits the attributes or properties and methods of another class

### Example
The `Animal` class below can be used to tell that an animal can eat


```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")
```

Let's say we need to create another class called Dog.

Since a dog is also an animal, it's more efficient to have access to all the properties and methods of the `Animal` class than to create another

This example creates a class named `Dog` and inherits from the `Animal` class


```python
class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        print(self.name, "barks")
```

<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>As you may notice, to inherit from a parent, we simply pass the name of that class as a parameter of the child class.</p></div>

Now we can use the properties and methods of both the `Animal` and the `Dog` classes using just one instance


```python
dog1 = Dog(name='Brian', age=8, color='White')
dog1.eat()
dog1.sound()
```

    Brian is eating.
    Brian barks


The `super()` and `__init__` functions found in the `Dog` class allow us to inherit the properties and methods of the `Animal` class.

### Parent and Child Class

The parent class is the class from whick the other class inherits from.

The child class is the the class that inherits from another class

In our example above, the `Animal` is the parent class while the `Dog` class is the child class

## Formatted Strings

<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/yb_1SV_VuD0?si=genqEID1g99GuGMg"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>

In Python, we can format a string by adding substring/s within it.

The `format()` function allows us to format strings.

### Placeholders `{}`
Placeholders help us control which part of the string should be formated.

They are defined using  curly braces `{}`.

In this example, we will concatenate (add) a substring to where the curly braces are placed


```python
text = "I love {} very much!"
formatted_text = text.format("Python")

print(formatted_text)
```

    I love Python very much!


### Multiple placeholders

If you want to format multiple parts of a string, use multiple placeholders.


```python
text = '{} loves to code in {}'
formatted_text = text.format('Juma', 'JavaScript')

print(formatted_text)
```

    Juma loves to code in JavaScript


### Using Indexes

We can use index numbers to specify exactly where the values should be placed. 

The index numbers should be inside the curly braces: `{index_numbers}`


```python
text = 'I love {2}, {1} and {0} very much!'
formatted_text = text.format('Python', 'JavaScript', 'HTML')

print(formatted_text)
```

    I love HTML, JavaScript and Python very much!


<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>0 represents the first value, 1 represents the second value and so on.</p></div>

### Using Named Indexes

We can also use named indexes to specify exactly where the values should be placed.

The arguments of the `format()` function should be in `key/value` pairs ie `key=value`.

The `key/value` pairs should be separated by commas.


```python
text = 'The color of the {fruit} is {color}.'
formatted_text = text.format(fruit='banana', color='yellow')

print(formatted_text)
```

    The color of the banana is yellow.


### Literal String Interpolation

Literal string interpolation allows you to use expression inside your strings. 

Simply add `f` before you opening quote, then surround your expressions with curly braces `{}`.


```python
name = 'Juma'; 
language = 'JavaScript'

statement = f'{name} loves to code in {language}'

print(statement)
```

    Juma loves to code in JavaScript


Here's another example


```python
number1 = 5
number2 = 7
answer = f'The summation of 5 and 7 is {number1 + number2}'

print(answer)
```

    The summation of 5 and 7 is 12


## Errors in Python

When coding in Python, you will encounter errors.

When errors occur, the program crashes or stops executing.

Fortunately, errors can be handled in Python

### The `try...except` statment

The `try...except` statement is used to handle exceptions(errors)

The `try` statement takes a block of code to test for errors

The `except` statement handles the exceptions.


```python
try:
    # age = input('Enter your age: ')
    age = '32'

    if age >= 18:
        print('Your vote has been cast')
    else:
        print('You are not eligible to vote')
except:
    print('A problem occured while picking your age \n'
          'You did not enter a number')

text = "\nHello world!"
print(text)
```

    A problem occured while picking your age 
    You did not enter a number
    
    Hello world!


<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>Even when the exception was thrown, the codes after the try...except were still executed</p></div>

### The `else` statement

The else statement is executed if there are no exceptions thrown.


```python
try:
    text = "Hello World!"
    print(text)
except:
    print("An error occurred.")
else:
    print("No exception was thrown!")
```

    Hello World!
    No exception was thrown!


### The `finally` statement

The `finally` statement is executed whether or not an exception is thrown.


```python
try: 
    text = "hello world"
    print(text)
except:
    print("An error occured.")
finally:
    print("Hello, I am still printed.")

print("----------------------")

# an exception will be thrown here
try: 
    print(undefined_variable)
except:
    print("An error occured.")
finally:
    print("Hello, I am still printed.")
```

    hello world
    Hello, I am still printed.
    ----------------------
    An error occured.
    Hello, I am still printed.


### Throw Exceptions
We can intentionally throw and exception to stop the execution of a program.

The `raise` keyword throws an excrption.


```python
# Creating your own errors
try: 
    age = 14
    if age < 18:
        raise Exception('Not an adult')
except Exception as error:
    print('A problem occurred \n'
          f'Error: {error}')
```

    A problem occurred 
    Error: Not an adult


### Kinds of Exceptions

In Python, there are different kinds of exceptions and we can handle them individually with the `try...except` statement.

```python
try:
    # statements
except ExceptionKind:
    #statments
```

One of the most common kind of exceptions is the `NameError`. This is thrown when you use a variable that is not defined


```python
try:
    print(rand_var)
except NameError:
    print('You used a variable that is not defined!')
```

    You used a variable that is not defined!


## Variable Scope
<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/VMmR86ghCyc?si=jkxeuEJntvdnTtZL"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>

## Python Variable Scopes

The accessibility of variable depends on its scope. In Python, there are two variable scopes:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Global Scope</li> 
<li><i class="bi bi-cursor"></i> Local Scope</li> 
</ul>

### Global Scope
A variable that is defined (created) outside a function has a global scope

A global variable can be accessed anywhere in a program


```python
name = 'Viola'
# name can be accessed here
print(name)

def greet():
    # name can be accessed here
    print('Hello ' + name)

greet()
```

    Viola
    Hello Viola


## Local Scope

A variable that is defined (created) inside a function has a local scope. A local scope variable can only be accessed and used inside the function.


```python
def greet():
    local_name = 'Viola'
    print('Hello ' + local_name)

greet()

try:
    # local_name cannot be accessed here
    print(local_name)
except Exception as e:
    print(e)
```

    Hello Viola
    name 'local_name' is not defined


### The `global` Keyword

We can force a local variable to be a global variable by using the `global` keyword.


```python
# Global Keyword

def add():
    global summ
    number1 = 5
    number2 = 7
    summ = number1 + number2
    return summ

add()

# summ is accessible even outside the function
print(summ)
```

    12


## Exercise

Develop a simple calculator to accept two floating point numbers from the keyboard.
Then display a menu to the user and let him/her select a mathematical operation to be performed on
those two numbers. Then display the answer. A sample run of you program should be similar to the
following:

```
Enter number 1: 20
Enter number 2: 12
Mathematical Operation
-----------------------------------
1 - Add
2 - Subtract
3 - Multiply
4 - Divide
-----------------------------------
Enter your preference: 2
Answer : 8.00
```

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
