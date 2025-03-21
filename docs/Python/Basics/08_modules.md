---
title: Python Modules
description: Learn Programming for Data Science
keywords: [python modules, math module, json module, date time module, random module, what is a python module, why use modules]
author: Juma Shafara
date: "2023-11"
---

![Photo by DATAIDEA](../assets/banner4.png)

## Modules
A module in Python is a python file that can contain variables, functions and classes

### Why use Modules?
Modules allow us to split our code into multiple files

Instead of writing all our codes inside a sigle Python file, we can use modules

<div class="alert text-white rounded" style="background: #3a6e68;"><h4>Note!</h4><p>That way, our code will be easier to read, understand and maintain</p></div>

### Creating a Module
There is nothing so special with creating a module, simply write you Python code and save it with the `.py` extension.

In this example, we have a module saved as my_module.py and it contains the following code



```python
# this is my_module.py

first_name = 'Viola'
last_name = 'Akullu'

def add(number1, number2):
    return number1 + number2

def multiply(number1, number2):
    return number1 * number2
```

After that, to use `my_module.py`, we need to import it.

To import, use the `import` statement and the module name.

Then we can use the variables and functions in the module.

In this example, the code below is saved as `main_code.py` and it imports the `module.py`.


```python
# this is main_code.py

import my_module

full_name = my_module.first_name + my_module.last_name
print('Full name:', full_name)

summation = my_module.add(3, 7)
print('Summation:', summation)
```

    Full name: ViolaAkullu
    Summation: 10


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

### Using Aliases
We can use an alias to refer to the module

To use an alias, use the `as` keyword


```python
# this is main_code.py

import my_module as mm

full_name = mm.first_name + mm.last_name
print('Full name:', full_name)

summation = mm.add(3, 7)
print('Summation:', summation)
```

    Full name: ViolaAkullu
    Summation: 10


### Importing Parts of a Module
We can choose to import only some specific parts of a module

>Note! When we import a part of a module, we will be able to use its variables and functions directly

Use the `from` keyword to import a part of a module.

In this example, we will import the `first_name` variable and access it directly


```python
from my_module import first_name

# now we can use it directly as 
print(first_name)
```

    Viola


### The dir() Function

The `dir()` function returns a list of all the variables, functions and classes available in a module


```python
import my_module

dir_ = dir(my_module)

print(dir_)
```

    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'first_name', 'last_name', 'multiply']


### Built in Modules
Python has many useful built-in modules that we can use to make coding easier.

Built-in modules can be imported without having to create them

In this example, we will import the `sysconfig` module and use its `get_python_version()` to return the Python version we're using


```python
import sysconfig

python_version = sysconfig.get_python_version()
print(python_version)
```

    3.10


## Math Module

The math module gives us access to mathematical functions

To use the math module, import it first, then we can start using it.

We can use the math module to find the square root of a number using the `math.sqrt()` method


```python
import math

number = 16
number_sqrt = math.sqrt(number)

print('Number:', number)
print('Square root of number:', number_sqrt)
```

    Number: 16
    Square root of number: 4.0


We can use the math module to get the factorial of a number by using the `math.factorial()` method


```python
import math

number = 5
number_factorial = math.factorial(number)

print('Number:', number)
print('Factorial:', number_factorial)
```

    Number: 5
    Factorial: 120


The math module also contains some constants like `pi` and `e`


```python
import math

print('e:', math.e)
print('pi:', math.pi)
```

    e: 2.718281828459045
    pi: 3.141592653589793


The math module can do those and so much more

## Random Module
The `random` module lets us generate a random number

As usual, to use the `random` module, import it first.

We can generate a random number that falls within a specified range by using the `random.randint()` method


```python
import random

random_integer = random.randint(1,100)
print('Random Integer:', random_integer)
```

    Random Integer: 4


We can generate numbers from a gaussian distribution with mean (`mu`) as 0 and standard deviation (`sigma`) as 1


```python
numbers = []

counter = 0
while counter < 100:
    numbers.append(random.gauss(mu=0, sigma=1))
    counter += 1
    
print(numbers)
```

    [0.8310128735410047, 2.402375340413018, -1.2769617295659348, 0.7569506717477539, 1.6026026122392498, 1.4142936594217554, -0.3169917649104485, -0.07305941097531603, -0.7885301448554015, -0.0674611332298377, 0.28288857512573684, 0.08844216926370602, -1.249987094506388, 0.870793290313952, -0.6607737394803138, 0.3780605189691181, 0.20288623881856632, 0.8439702923769746, 1.6500270929422152, -0.5579247768953991, -0.3076290349937902, 0.8927675985413197, -2.3716599434459114, 0.23253728473684382, 0.01698634011714592, -1.506684284668113, -1.516156046117149, -0.7549199652372819, 0.4855840249497611, -1.9426218553454226, -0.5672748318805165, 1.7849639815888045, -0.4223703532919884, -1.4182523392919628, 0.3817982448773813, -1.2151583559744263, 0.21736913499460964, 0.0743448686041854, -0.6217874541247053, -0.05369712902089164, 0.06560332100098984, 0.5791279113149166, 1.5329264216964942, -1.5523813284095307, 0.256018716284597, 1.498941708596562, 0.6484203278916434, 0.956658998431066, -0.7469607705965761, 0.9093585267915438, -0.3301676177291813, -2.1020486475752564, -0.6324768823835674, -0.2621489739923403, 0.36805271395009337, -0.1987104858441708, -0.20226660046300027, -1.0227302328088852, 0.9440428943259802, 1.3499647213634605, 0.28655811659281705, -0.48212404896946465, 1.5732404576352244, 1.7024230857294205, -0.32802550098029193, 2.0808443667109597, 2.2783854541239874, -0.265626754707208, -0.04641950638081212, 0.7941371582079103, -0.36860553191079254, -0.9098450679735101, 1.234946260813307, -2.835066105841072, 1.3883254119625694, 1.2853299658795028, 1.178005875662903, 0.3186472037221876, -1.0006920744966419, -2.3745959188263885, 1.8440465299894964, -0.35610549619690796, 0.5857012223823791, 0.7400382246661824, 0.07225122970263118, -0.5508995490344698, -0.038356750477046286, -0.040997463659922434, 0.6802546773316889, -1.3861271290488735, 0.7275261286416534, 0.3729374034245036, -0.013616473457934613, -0.7620103036607296, 0.15556952852877587, -1.7898533901375224, -1.137248630020012, -1.71518120153122, -0.5817297506694047, -0.4035542913039588]


## Date and Time
The `datetime` module allows us to work with dates

As usual we have to import the `datetime` module to be able to use it.

### Current Date and Time
The `datetime.datetime.now()` method returns the current date and time


```python
import datetime

time_now = datetime.datetime.now()
print(time_now)
```

    2024-05-01 08:18:09.070054


### The `date` Object
The `date` object represents a date (year, month and day)

To create a `date` object, import it from the `datetime` module first.


```python
from datetime import date

today = date.today()
print('Current date:', today)
```

    Current date: 2024-05-01


## JSON
JSON stands for JavaScript Object Notation.

JSON contains data that are sent or received to and from a server

JSON is simply a string, if follows a format similar to a Python [dictionary](06_flow_control.ipynb)

**Example:**


```python
data = "{'first_name': 'Juma','last_name': 'Shafara', 'age': 39}"

print(data)
```

    {'first_name': 'Juma','last_name': 'Shafara', 'age': 39}


### JSON to Dictionary
Before we can individually access the data of a JSON, we need to convert it to a Python dictionary first.

To do that, we need to import the `json` module


```python
import json 

data = '{"first_name": "Juma","last_name": "Shafara", "age": 39}'

# convert to dictionary
data_dict = json.loads(data)

print('Fist name:',data_dict['first_name'])
print('Last name:', data_dict['last_name'])
print('Age:', data_dict['age'])
```

    Fist name: Juma
    Last name: Shafara
    Age: 39


### Dictionary to JSON
To convert a dictionay to JSON, use the `json.dumps()` method.


```python
import json

data_dict = {
    "first_name": "Juma",
    "last_name": "Shafara", 
    "age": 39
    }

data_json = json.dumps(data_dict)


```

## Exercise

Write a program to calculate the factorial of any given positive integer.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
