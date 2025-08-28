---
title: Python Containers
description: Learn Programming for Data Science
keywords: [python containers, python collections, list, set, object, tuple, dictionary, indexing, negative indexing, range of indexes, adding items, deleting items, Juma Shafara, What is an object?]
author: Juma Shafara
date: "2023-11"
date-modified: "2024-11-25"
---

![Photo by DATAIDEA](../../assets/banner4.png)

### Table of Contents

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> What is an object?</li> 
<li><i class="bi bi-cursor"></i> Containers</li> 
<li><i class="bi bi-cursor"></i> Lists</li> 
<li><i class="bi bi-cursor"></i> Tuple</li> 
<li><i class="bi bi-cursor"></i> Sets</li> 
<li><i class="bi bi-cursor"></i> Dictionaries</li> 
<li><i class="bi bi-cursor"></i> Free Dictionary Tip</li> 
<li><i class="bi bi-cursor"></i> Exercise</li> 
</ul>

Containers in Python are objects that contain other objects

## What is an object?
In python, everything is an object. Even the simplest strings and numbers are considered as objects


```python
x = 'My favorite number is '
y = 21

print(x, y)
```

    My favorite number is  21


## Containers

Containers (also called collections) are objects that contain objects

In the example below, the `fruits` variable contains three strings


```python
fruits = ['bananas', 'apples', 'grapes']

print(fruits)
```

    ['bananas', 'apples', 'grapes']


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

## Lists

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A python list is an ordered container</li> 
<li><i class="bi bi-cursor"></i> A list is created by using square brackets (`[]`)</li> 
<li><i class="bi bi-cursor"></i> Objects are poaced inside those brackets and are separated by commas (`,`)</li> 
</ul>


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
print(pets)
print(type(pets))
```

    ['dog', 'cat', 'rabbit', 'monkey']
    <class 'list'>


A list can contain mixed data types.


```python
x = ['dog', 21, True]
print(x)
```

    ['dog', 21, True]


### Indexing
- Indexing is used to access items of a list
- Indexing uses square brackets and numbers to access individual items of a list
- Where `0` refers to the first item, 1 refers to the second item, and so on


```python
# indexing
pets = ['dog', 'cat', 'rabbit', 'monkey']
print(pets[0])
print(pets[1])
print(pets[2])
```

    dog
    cat
    rabbit


### Negative Indexing
Negative indexing is used to access the items of a list using negative numbers.

Where `-1` refers to the last item, `-2` refers to the second last item, and so on.


```python
# negative indexing
pets = ['dog', 'cat', 'rabbit', 'monkey']
print(pets[-1])
print(pets[-2])
print(pets[-3])
```

    monkey
    rabbit
    cat


### Range of Indexes
By using a colon ie `:`, we can access a range of items at once.

Simply separate two indexes using the colon.

The first index is the start of the range, while the second index is the end of the range (not included)


```python
#range of indexes
pets = ['dog', 'cat', 'rabbit', 'monkey']
print(pets[1:3])
```

    ['cat', 'rabbit']


If you don't specify the last index, the range ends with the last item of the list

In this case, the range includes the last item.


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
print(pets[2:])
```

    ['rabbit', 'monkey']


### Adding items to a list
The `append()` method adds an item to the end of the list.

In this example, we will add `'fish'` to our pets list


```python
pets = ['dog', 'cat']
pets.append('fish')

print(pets)
```

    ['dog', 'cat', 'fish']


The `insert()` method inserts an item at the specified index.

In this case, we will insert `'rabbit'` to the index 0 and `'hamster'` to index 2


```python
pets = ['dog', 'cat', 'monkey']
pets.insert(0, 'rabbit')
pets.insert(2, 'hamster')

print(pets)
```

    ['rabbit', 'dog', 'hamster', 'cat', 'monkey']


### Deleting Items from a list
The `pop()` method removes the last item from a list 


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
pets.pop()

print(pets)
```

    ['dog', 'cat', 'rabbit']


The `remove()` method removes the specified item value.


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
pets.remove('rabbit')

print(pets)
```

    ['dog', 'cat', 'monkey']


To delete a specified index, use the `del` keyword


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
del pets [2]

print(pets)
```

    ['dog', 'cat', 'monkey']


### Getting the length of a list

The length of a list refers to the number of items in a list, use the `len()` method

### Changing an item's value
To change an item's value, access the index first and use the assignment operator.


```python
pets = ['dog', 'cat', 'rabbit', 'monkey']
pets[2] = 'fish'

print(pets)
```

    ['dog', 'cat', 'fish', 'monkey']


### Homework
- Check if an item exist

### Extending a list

The `extend()` methods adds all items from one list to another


```python
pets = ['dog', 'cat']
other_pets = ['rabbit', 'monkey']
pets.extend(other_pets)
print(pets)
```

    ['dog', 'cat', 'rabbit', 'monkey']


## Tuple
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Python tuple is an ordered container</li> 
<li><i class="bi bi-cursor"></i> Its the same as a list but the items of tuples cannot be changed</li> 
<li><i class="bi bi-cursor"></i> We create a tuple using round brackets `()`</li> 
</ul>


```python
pets = ('dog', 'cat', 'rabbit')
print(pets)
print(type(pets))
```

    ('dog', 'cat', 'rabbit')
    <class 'tuple'>


## Sets
<!-- Video -->
<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/fwwIn50cQ2c"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> A set is a container/collection that is unordered and immutable</li> 
<li><i class="bi bi-cursor"></i> We create a set using `{}`</li> 
<li><i class="bi bi-cursor"></i> The objects are placed inside those brackets and are separated by commas </li> 
</ul>


```python
pets = {'dog', 'cat', 'rabbit'}
print(pets)
```

    {'rabbit', 'dog', 'cat'}


A set can contain mixed data types, but can NOT contain mutable items like lists, sets and dictionaries


```python
# A set can contain objects of different data types
mixed = {'dog', 21, True}
print(mixed)
print(type(mixed))
```

    {True, 'dog', 21}
    <class 'set'>


### Accessing set elements

- Unlike lists and tuples, you cannot access the items in a set using indexes
- This is because a set is unordered and not indexed
- However, we can use a `for` loop to access all its items one-by-one

***Note: We'll discuss a for loop in the next chapter***


```python
# Accessing
pets = {'dog', 'cat', 'rabbit'}
for pet in pets:
    print(pet)
```

    rabbit
    dog
    cat


### Adding elements to a set
To add items to a set, use the `add()` or `update()` method.

The `add()` method adds one item to a set.


```python
# Adding items to a set
pets = {'dog', 'cat', 'rabbit'}
pets.add('fish')
print(pets)
```

    {'rabbit', 'dog', 'cat', 'fish'}


### Changing an item
The items of a set can NOT be changed because a set is immutable or unchangeable.

### Removing set elements
To remove an item from a set, use the `remove()` method.

You should specify the value of the item you want to remove.


```python
# Removing items from a set
pets = {'dog', 'cat', 'rabbit'}
pets.remove('cat') # remove
print(pets)
```

    {'rabbit', 'dog'}


You can also use the `discard()` method.


```python
pets = {'dog', 'cat', 'rabbit'}
pets.discard('rabbit') #discard
print(pets)
```

    {'dog', 'cat'}


The difference between the `remove()` and `discard()` methods is that the `discard()` method does not raise an error if the specified item is not present.

You can also use the `pop()` method to remove an item.

But we cannot determine which item will be removed because a set is unordered.


```python
pets = {'dog', 'cat', 'rabbit'}
pets.pop() # pop removes the last item from the set
print(pets)
```

    {'dog', 'cat'}


### Homework
- Find the length of a set
- Check if an element exists
- Combine sets

### Getting the difference between sets
To get the difference between two sets, use the subtraction operator (`-`)


```python
# Getting the difference
first_numbers = {1, 2, 3, 4}
second_numbers = {3, 4, 5, 6}

difference = first_numbers - second_numbers
# another way
difference2 = first_numbers.difference(second_numbers)
print(difference)
```

    {1, 2}


## Dictionaries

A dictionary is an unordered and mutable colletion of items.

A dictionary is written with curly brackets.

Each item in a dictionary contains a `key/value` pair.

<!-- Video -->
<div class="video-wrapper">
  <iframe
    class="video-iframe"
    src="https://www.youtube.com/embed/UatrQb3tQTw?si=u2LX_giR2kJ_VqwO"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
    allowfullscreen
  >
  </iframe>
</div>


```python
# Creating 
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }

print(person)
```

    {'first_name': 'Voila', 'last_name': 'Akullu', 'age': 16}


In the above example we have 3 items:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> The first item has a key name of `'first_name'`, and its value is `'Viola'`.</li> 
<li><i class="bi bi-cursor"></i> The second item has a key name of `'last_name'`, and its value is `'Akullu'`</li> 
<li><i class="bi bi-cursor"></i> The third item has a key name of `'age'`, and its value is `30`</li> 
</ul>

### Accessing items
To access an item, specify the key name of an item inside square brackets.


```python
# Accessing items
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }

print(person['last_name'])
```

    Akullu


If you try to access an item using a key name that does not exist, an error will be raised 

### Adding items
To add new items, specify a new index key name inside the square brackets and assign a  value using the assignment operator.


```python
# Adding items 
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }
person['middle_name'] = 'Vee'

print(person)
```

    {'first_name': 'Voila', 'last_name': 'Akullu', 'age': 16, 'middle_name': 'Vee'}


### Changing an item's value
To change an item, refer to its key name using square brackets and use the assignment operator.


```python
# Changing items 
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }
person['last_name'] = 'Kibekityo'

print(person)
```

    {'first_name': 'Voila', 'last_name': 'Kibekityo', 'age': 16}


### Removing an Item's value
To remove an item, use the pop() method.

The `pop()` method removes an item with the specified key name.


```python
# Remove items
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }

person.pop('age')
print(person)
```

    {'first_name': 'Voila', 'last_name': 'Akullu'}


Another way to remove an item is to use the `del` keyword.


```python
# del keyword
person = {
    'first_name': 'Voila', 
    'last_name': 'Akullu',
    'age': 16
    }

del person['age']
print(person)
```

    {'first_name': 'Voila', 'last_name': 'Akullu'}


### Homework
- Check if an element exists
- Find the length of a dictionary

### Nested Dictionary
A dictionary can contain another dictionary.


```python
# Nesting dictionaries
employees = {
    'manager': {
        'name': 'Akullu Viola',
        'age': 29
    },
    'programmer': {
        'name': 'Juma Shafara',
        'age': 30
    }
}

print(employees)
```

    {'manager': {'name': 'Akullu Viola', 'age': 29}, 'programmer': {'name': 'Juma Shafara', 'age': 30}}


To access an item in a nested dictionary, access the key name of the dictionary then the key name of the item


```python
# Accessing nested dictionary
employees = {
    'manager': {
        'name': 'Akullu Viola',
        'age': 29
    },
    'programmer': {
        'name': 'Juma Shafara',
        'age': 30
    }
}

programmer = employees['programmer']
print(programmer['name'])
```

    Juma Shafara


## Free Dictionary Tip 


```python
# Using a dictionary constructer
names = ('a1', 'b2', 'c3')
dictionary = dict(names)
print(dictionary)
```

    {'a': '1', 'b': '2', 'c': '3'}


### Exercise

Write a program to store marks of 5 students for 5 subjects given through the keyboard.
Calculate the average of each students marks and the average of marks taken by all the students

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
