# Arrays and Lists

Arrays and lists are fundamental data structures that store collections of elements in sequential order. They are the building blocks for many other data structures and algorithms.

## What is an Array?

An array is a collection of elements stored in contiguous memory locations. Each element can be accessed using an index.

### Key Characteristics:

- **Fixed Size** - Size is defined at creation (in traditional arrays)
- **Same Data Type** - All elements are of the same type
- **Index-based Access** - O(1) time to access any element
- **Contiguous Memory** - Elements stored next to each other

### Python Lists vs Arrays

Python's `list` is actually a dynamic array that can:
- Grow and shrink in size
- Store different data types
- Provide built-in methods for manipulation

```python
# Python list (dynamic array)
numbers = [1, 2, 3, 4, 5]

# Access by index
print(numbers[0])  # 1
print(numbers[-1]) # 5 (last element)

# Modify elements
numbers[2] = 10
print(numbers)  # [1, 2, 10, 4, 5]
```

## Common Array Operations

### 1. Accessing Elements

```python
# Direct access - O(1)
arr = [10, 20, 30, 40, 50]
first = arr[0]      # 10
last = arr[-1]      # 50
middle = arr[2]     # 30

# Slicing - O(k) where k is slice size
subset = arr[1:4]   # [20, 30, 40]
reversed_arr = arr[::-1]  # [50, 40, 30, 20, 10]
```

### 2. Insertion

```python
arr = [1, 2, 3, 4, 5]

# Append at end - O(1) amortized
arr.append(6)
print(arr)  # [1, 2, 3, 4, 5, 6]

# Insert at specific position - O(n)
arr.insert(2, 99)
print(arr)  # [1, 2, 99, 3, 4, 5, 6]

# Extend with another list - O(k)
arr.extend([7, 8, 9])
print(arr)  # [1, 2, 99, 3, 4, 5, 6, 7, 8, 9]
```

### 3. Deletion

```python
arr = [10, 20, 30, 40, 50]

# Remove by value - O(n)
arr.remove(30)
print(arr)  # [10, 20, 40, 50]

# Remove by index - O(n)
del arr[1]
print(arr)  # [10, 40, 50]

# Pop last element - O(1)
last = arr.pop()
print(last)  # 50
print(arr)   # [10, 40]

# Pop specific index - O(n)
element = arr.pop(0)
print(element)  # 10
```

### 4. Searching

```python
arr = [5, 2, 8, 1, 9, 3]

# Linear search - O(n)
if 8 in arr:
    print("Found!")

# Find index - O(n)
index = arr.index(8)
print(index)  # 2

# Count occurrences - O(n)
count = arr.count(2)
print(count)  # 1
```

## Time Complexity Summary

| Operation | Time Complexity |
|-----------|----------------|
| Access by index | O(1) |
| Search by value | O(n) |
| Insert at end | O(1) amortized |
| Insert at beginning | O(n) |
| Insert at middle | O(n) |
| Delete from end | O(1) |
| Delete from beginning | O(n) |
| Delete from middle | O(n) |

## Common Array Problems

### Problem 1: Find Maximum Element

```python
def find_max(arr):
    """
    Find the maximum element in an array
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return None

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val

# Test
numbers = [3, 7, 2, 9, 1, 5]
print(find_max(numbers))  # 9

# Using built-in
print(max(numbers))  # 9
```

### Problem 2: Reverse an Array

```python
def reverse_array(arr):
    """
    Reverse an array in-place
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Test
numbers = [1, 2, 3, 4, 5]
print(reverse_array(numbers))  # [5, 4, 3, 2, 1]

# Using slicing (creates new list)
print(numbers[::-1])  # [5, 4, 3, 2, 1]
```

### Problem 3: Remove Duplicates

```python
def remove_duplicates(arr):
    """
    Remove duplicates from sorted array
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0

    write_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index

# Test
sorted_nums = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(sorted_nums)
print(sorted_nums[:length])  # [1, 2, 3, 4, 5]

# Using set (for unsorted arrays)
unique = list(set(sorted_nums))
print(sorted(unique))  # [1, 2, 3, 4, 5]
```

### Problem 4: Two Sum Problem

```python
def two_sum(arr, target):
    """
    Find two numbers that sum to target
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None

# Test
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  # [0, 1] (indices)
```

### Problem 5: Rotate Array

```python
def rotate_array(arr, k):
    """
    Rotate array to the right by k steps
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    k = k % n  # Handle k > n

    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    # Reverse remaining elements
    arr[k:] = arr[k:][::-1]

    return arr

# Test
numbers = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(numbers, k))  # [5, 6, 7, 1, 2, 3, 4]
```

## Multi-dimensional Arrays

Arrays can have multiple dimensions, commonly used for matrices and grids.

```python
# 2D Array (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# Traverse 2D array
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# Create 2D array with list comprehension
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
```

### Matrix Operations

```python
def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns)
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[matrix[r][c] for r in range(rows)]
                  for c in range(cols)]

    return transposed

# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```

## Python List Comprehensions

List comprehensions provide a concise way to create and manipulate lists.

```python
# Basic comprehension
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With transformation
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 0, 0],
#  [0, 1, 2],
#  [0, 2, 4]]
```

## Best Practices

1. **Use Built-in Methods** - Python's list methods are optimized
2. **Avoid Growing Arrays in Loops** - Pre-allocate if size is known
3. **Use Slicing Carefully** - Creates new list (memory overhead)
4. **Consider NumPy** - For numerical operations on large arrays
5. **Use Generators** - For large datasets to save memory

```python
# Good: Pre-allocate
result = [0] * n
for i in range(n):
    result[i] = compute(i)

# Bad: Growing in loop
result = []
for i in range(n):
    result.append(compute(i))

# Better: List comprehension
result = [compute(i) for i in range(n)]
```

!!! tip "Practice Problems"
    Try solving these classic array problems:
    - Find missing number in array (1 to n)
    - Merge two sorted arrays
    - Find majority element
    - Stock buy and sell problem
    - Maximum subarray sum (Kadane's algorithm)

!!! note "NumPy for Numerical Arrays"
    For scientific computing and numerical operations, consider using NumPy arrays which are more efficient than Python lists for mathematical operations.

---

**Next Tutorial:** [Stacks and Queues](03_stacks_and_queues.md)