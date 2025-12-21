# Introduction to Data Structures & Algorithms

Data Structures and Algorithms (DSA) are fundamental concepts in computer science that help you write efficient, scalable, and optimized code. Understanding DSA is essential for problem-solving and technical interviews.

## What are Data Structures?

Data structures are specialized formats for organizing, processing, storing, and retrieving data. They provide a way to manage large amounts of data efficiently.

### Common Data Structures:

- **Arrays & Lists** - Sequential collection of elements
- **Stacks** - Last-In-First-Out (LIFO) structure
- **Queues** - First-In-First-Out (FIFO) structure
- **Linked Lists** - Chain of nodes with data and pointers
- **Trees** - Hierarchical structure with parent-child relationships
- **Graphs** - Network of nodes connected by edges
- **Hash Tables** - Key-value pairs for fast lookup

## What are Algorithms?

Algorithms are step-by-step procedures or formulas for solving problems. They define the logic and operations needed to accomplish a specific task.

### Algorithm Categories:

- **Searching** - Finding elements (Linear Search, Binary Search)
- **Sorting** - Arranging elements (Bubble Sort, Quick Sort, Merge Sort)
- **Traversal** - Visiting all elements (DFS, BFS)
- **Dynamic Programming** - Breaking problems into subproblems
- **Greedy** - Making locally optimal choices
- **Divide and Conquer** - Splitting problems into smaller parts

## Why Learn DSA?

### 1. Write Efficient Code
Understanding DSA helps you choose the right data structure and algorithm for optimal performance.

### 2. Problem-Solving Skills
DSA teaches you how to break down complex problems into manageable parts.

### 3. Technical Interviews
Most tech companies (Google, Amazon, Microsoft, Meta) heavily test DSA knowledge.

### 4. Foundation for Advanced Topics
DSA is essential for machine learning, database design, and system architecture.

## Time and Space Complexity

One of the most important concepts in DSA is analyzing algorithm efficiency using Big O notation.

### Big O Notation

Big O describes the worst-case performance of an algorithm:

| Notation | Name | Example |
|----------|------|---------|
| **O(1)** | Constant | Accessing array element by index |
| **O(log n)** | Logarithmic | Binary search |
| **O(n)** | Linear | Iterating through array |
| **O(n log n)** | Linearithmic | Merge sort, quick sort |
| **O(n²)** | Quadratic | Nested loops, bubble sort |
| **O(2ⁿ)** | Exponential | Recursive fibonacci |

### Example: Analyzing Complexity

```python
# O(1) - Constant time
def get_first_element(arr):
    return arr[0]

# O(n) - Linear time
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## Data Structure Comparison

| Data Structure | Access | Search | Insert | Delete | Use Case |
|----------------|--------|--------|--------|--------|----------|
| **Array** | O(1) | O(n) | O(n) | O(n) | Fixed-size collections |
| **Linked List** | O(n) | O(n) | O(1) | O(1) | Dynamic size, frequent insertions |
| **Stack** | O(n) | O(n) | O(1) | O(1) | Undo operations, recursion |
| **Queue** | O(n) | O(n) | O(1) | O(1) | Task scheduling, BFS |
| **Hash Table** | O(1) | O(1) | O(1) | O(1) | Fast lookups, caching |
| **Binary Tree** | O(log n) | O(log n) | O(log n) | O(log n) | Hierarchical data, BST |

## Python for DSA

Python is an excellent language for learning DSA due to its:

- **Simple syntax** - Easy to focus on concepts
- **Built-in data structures** - Lists, dictionaries, sets
- **Rich libraries** - Collections, heapq, itertools

### Python Built-in Data Structures

```python
# List (Dynamic Array)
numbers = [1, 2, 3, 4, 5]

# Dictionary (Hash Table)
student = {"name": "John", "age": 20, "grade": "A"}

# Set (Unique elements)
unique_numbers = {1, 2, 3, 4, 5}

# Tuple (Immutable list)
coordinates = (10, 20)

# Stack using list
stack = []
stack.append(1)  # push
stack.pop()      # pop

# Queue using collections
from collections import deque
queue = deque()
queue.append(1)      # enqueue
queue.popleft()      # dequeue
```

## Learning Path

This tutorial series will cover:

1. **Arrays and Lists** - Foundation of sequential data
2. **Stacks and Queues** - LIFO and FIFO structures
3. **Linked Lists** - Dynamic data structures
4. **Trees** - Hierarchical structures and BST
5. **Hash Tables** - Fast key-value storage
6. **Sorting Algorithms** - Organizing data efficiently
7. **Searching Algorithms** - Finding elements quickly
8. **Graph Algorithms** - Network and relationship problems

## Practice Resources

To master DSA, practice on these platforms:

1. **LeetCode** - [leetcode.com](https://leetcode.com/)
2. **HackerRank** - [hackerrank.com](https://www.hackerrank.com/)
3. **CodeForces** - [codeforces.com](https://codeforces.com/)
4. **GeeksforGeeks** - [geeksforgeeks.org](https://www.geeksforgeeks.org/)

!!! tip "Consistent Practice"
    Spend 30-60 minutes daily solving DSA problems. Start with easy problems and gradually move to medium and hard ones.

!!! note "Interview Preparation"
    For technical interviews, focus on understanding the problem-solving approach rather than memorizing solutions.

---

**Next Tutorial:** [Arrays and Lists](02_arrays_and_lists.md)