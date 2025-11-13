---
date: 2025-11-12
categories:
  - AI/ML
  - Data Science
author: Juma Shafara
---

# The `filter()` function in Python

The filter() function is used to filter elements from an iterable based on a condition.

## Syntax

```python
filter(function, iterable)
```

`function`: A function that returns True or False.

`iterable`: The list (or tuple, etc.) to filter.

It returns a filter object, which you can convert to a list, set, or tuple.

## Example

Let’s say we want to filter out only even numbers from a list.

### Without `filter()`:


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []

for num in numbers:
  if num % 2 == 0:
    even_numbers.append(num)

print(even_numbers)
```

    [2, 4, 6, 8]


### With `filter()`:


```python
even_numbers = filter(lambda num: num % 2 == 0, numbers)
print(list(even_numbers))
```

    [2, 4, 6, 8]


## Using named functions:
We can also use named functions instead of lambda functions, as of the example below


```python
def is_even(num):
  return num % 2 == 0

even_numbers = filter(is_even, numbers)

print(list(even_numbers))
```

    [2, 4, 6, 8]


## Using `filter()` with strings:

In the example below, we filter out the "short" words from the list of words


```python
words = ['data', 'ai', 'machine', 'learning']

long_words = filter(lambda word: len(word) > 4, words)

print(list(long_words))
```

    ['machine', 'learning']


## Using `filter()` to clean data:

In the example below, we remove all the None values from the list


```python
data = [10, None, 25, None, 40, 0]

cleaned = filter(lambda value: value is not None, data)
print(list(cleaned))
```

    [10, 25, 40, 0]



```python

```
