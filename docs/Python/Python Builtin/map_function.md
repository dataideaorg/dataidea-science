---
date: 2025-11-12
categories:
  - AI/ML
  - Data Science
author: Juma Shafara
---

# The `map()` function:

The `map()` function in Python is used to apply a function to every item in an iterable—like a list or a tuple—and returns a new map object with the results.

## Syntax:

`map(function, iterable)`

- `function`: This is the function you want to apply to each item.
- `iterable`: This is the list, tuple, or any other iterable whose items you want to process.

## Basic Example:

Imagine we want to square every number in a list.

### Without `map()`:



```python
numbers = [1, 2, 3]
squared = []

for num in numbers:
  square = num ** 2
  squared.append(square)

print(squared)
```

    [1, 4, 9]


### Without `map()`:


```python
squared = map(lambda num: num ** 2, numbers)
print(list(squared))
```

    [1, 4, 9]


The `map`


```python
a = [1, 2, 3]
b = [4, 5, 6]

summs = []

for count in range(len(a)):
  summs.append(a[count] + b[count])

print(summs)
```

    [5, 7, 9]



```python
summs = map(lambda x, y: x + y, a, b)
print(list(summs))
```

    [5, 7, 9]



```python
def add(x, y):
  return x + y

summs = map(add, a, b)
print(list(summs))
```

    [5, 7, 9]



```python

```
