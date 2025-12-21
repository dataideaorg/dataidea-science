# Stacks and Queues

Stacks and Queues are linear data structures that follow specific ordering principles for adding and removing elements. They are widely used in algorithms and system design.

## Stack

A **Stack** is a Last-In-First-Out (LIFO) data structure where the last element added is the first one to be removed.

### Real-World Analogies:

- Stack of plates (add/remove from top)
- Browser back button (most recent page first)
- Undo operation in text editor
- Function call stack in programming

### Stack Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| **push(item)** | Add item to top | O(1) |
| **pop()** | Remove and return top item | O(1) |
| **peek()** | View top item without removing | O(1) |
| **isEmpty()** | Check if stack is empty | O(1) |
| **size()** | Get number of elements | O(1) |

### Implementing Stack in Python

```python
# Using Python list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """View top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of items"""
        return len(self.items)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())    # 3
print(stack.peek())   # 2
print(stack.size())   # 2
```

### Simple Stack using List

```python
# Stack using built-in list
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Pop
top = stack.pop()  # 3

# Peek
top = stack[-1] if stack else None  # 2

# Check empty
is_empty = len(stack) == 0
```

## Stack Applications

### 1. Balanced Parentheses

```python
def is_balanced(expression):
    """
    Check if parentheses are balanced
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    matching = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in matching:
            stack.append(char)
        elif char in matching.values():
            if not stack or matching[stack.pop()] != char:
                return False

    return len(stack) == 0

# Test
print(is_balanced("()"))           # True
print(is_balanced("()[]{}"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("{[]}"))         # True
```

### 2. Reverse String

```python
def reverse_string(s):
    """
    Reverse a string using stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []

    # Push all characters
    for char in s:
        stack.append(char)

    # Pop all characters
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()

    return reversed_s

# Test
print(reverse_string("hello"))  # "olleh"

# Python way
print("hello"[::-1])  # "olleh"
```

### 3. Evaluate Postfix Expression

```python
def evaluate_postfix(expression):
    """
    Evaluate postfix expression (Reverse Polish Notation)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b

            stack.append(result)

    return stack.pop()

# Test
print(evaluate_postfix("2 3 +"))        # 5
print(evaluate_postfix("2 3 + 4 *"))    # 20
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))  # 14
```

## Queue

A **Queue** is a First-In-First-Out (FIFO) data structure where the first element added is the first one to be removed.

### Real-World Analogies:

- Line at a ticket counter
- Print job queue
- Task scheduling in operating systems
- Breadth-First Search in graphs

### Queue Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| **enqueue(item)** | Add item to rear | O(1) |
| **dequeue()** | Remove and return front item | O(1) |
| **front()** | View front item | O(1) |
| **isEmpty()** | Check if queue is empty | O(1) |
| **size()** | Get number of elements | O(1) |

### Implementing Queue in Python

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        """View front item without removing"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of items"""
        return len(self.items)

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1
print(queue.front())    # 2
print(queue.size())     # 2
```

### Simple Queue using deque

```python
from collections import deque

# Queue using deque
queue = deque()

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue
front = queue.popleft()  # 1

# Front
front = queue[0] if queue else None  # 2

# Check empty
is_empty = len(queue) == 0
```

## Queue Applications

### 1. Hot Potato Simulation

```python
def hot_potato(names, num):
    """
    Simulate hot potato game
    Time Complexity: O(n * num)
    Space Complexity: O(n)
    """
    from collections import deque

    queue = deque(names)

    while len(queue) > 1:
        # Pass the potato num times
        for _ in range(num):
            queue.append(queue.popleft())

        # Remove the person holding potato
        queue.popleft()

    return queue[0]

# Test
players = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(hot_potato(players, 3))  # Winner
```

### 2. Level Order Traversal (BFS)

```python
def level_order_traversal(root):
    """
    Print tree nodes level by level
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not root:
        return

    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

## Deque (Double-Ended Queue)

A **Deque** allows insertion and deletion at both ends.

```python
from collections import deque

# Create deque
dq = deque([1, 2, 3])

# Add to right
dq.append(4)        # [1, 2, 3, 4]

# Add to left
dq.appendleft(0)    # [0, 1, 2, 3, 4]

# Remove from right
dq.pop()            # 4

# Remove from left
dq.popleft()        # 0

# Result: [1, 2, 3]
```

## Priority Queue

A **Priority Queue** where elements are served based on priority, not insertion order.

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Add item with priority (lower number = higher priority)"""
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return highest priority item"""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def is_empty(self):
        return len(self.heap) == 0

# Usage
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)

print(pq.pop())  # Task 2 (priority 1)
print(pq.pop())  # Task 3 (priority 2)
print(pq.pop())  # Task 1 (priority 3)
```

## Stack vs Queue Comparison

| Feature | Stack | Queue |
|---------|-------|-------|
| **Order** | LIFO (Last In First Out) | FIFO (First In First Out) |
| **Primary Ops** | push(), pop() | enqueue(), dequeue() |
| **Use Cases** | Undo/Redo, Recursion, DFS | Task scheduling, BFS |
| **Python** | list with append/pop | deque with append/popleft |

## Common Interview Problems

### Next Greater Element

```python
def next_greater_element(arr):
    """
    Find next greater element for each element
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

# Test
nums = [4, 5, 2, 10, 8]
print(next_greater_element(nums))  # [5, 10, 10, -1, -1]
```

### Implement Queue using Stacks

```python
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, item):
        """O(1)"""
        self.stack1.append(item)

    def dequeue(self):
        """Amortized O(1)"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop() if self.stack2 else None

# Test
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.dequeue())  # 2
```

!!! tip "Practice Problems"
    Try solving these problems:
    - Min Stack (get minimum in O(1))
    - Valid Parentheses
    - Implement Stack using Queues
    - Sliding Window Maximum
    - Largest Rectangle in Histogram

!!! note "When to Use"
    - **Stack**: When you need LIFO behavior (undo operations, parsing, DFS)
    - **Queue**: When you need FIFO behavior (task scheduling, BFS, buffering)
    - **Deque**: When you need operations at both ends
    - **Priority Queue**: When elements have different priorities

---

**Next Tutorial:** [Linked Lists](04_linked_lists.md)