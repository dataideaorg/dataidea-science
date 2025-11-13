---
date: 2025-11-12
categories:
  - AI/ML
  - Data Science
author: Juma Shafara
---

# Python `reduce()` Function Explained



## Syntax

```python
from functools import reduce

reduce(function, iterable, initializer)
```


```python

```


```python
numbers = [1, 2, 3, 4]
total = 0

for num in numbers:
  total += num

print(total)
```

    10



```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
```

    10



```python
numbers = [1, 2, 3, 4]

def add(a, b):
  return a * b

result = reduce(add, numbers)
print(result)
```

    24



```python
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers, 10)
print(result)
```

    20



```python
numbers = [4, 8, 1, 6, 10, 3]

result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)
```

    10



```python

```
