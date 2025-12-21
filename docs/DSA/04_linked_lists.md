# Linked Lists

A **Linked List** is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't require contiguous memory.

## What is a Linked List?

### Structure:
- **Node**: Contains data and reference(s) to other node(s)
- **Head**: First node in the list
- **Tail**: Last node (points to None)

```
[Data|Next] -> [Data|Next] -> [Data|Next] -> None
   HEAD                          TAIL
```

### Key Characteristics:

- **Dynamic Size** - Can grow/shrink at runtime
- **No Random Access** - Must traverse from head
- **Efficient Insertion/Deletion** - No shifting required
- **Extra Memory** - For storing pointers

## Types of Linked Lists

### 1. Singly Linked List
Each node points to the next node.

```
1 -> 2 -> 3 -> 4 -> None
```

### 2. Doubly Linked List
Each node points to both next and previous nodes.

```
None <- 1 <-> 2 <-> 3 <-> 4 -> None
```

### 3. Circular Linked List
Last node points back to the first node.

```
1 -> 2 -> 3 -> 4 -|
^__________________|
```

## Singly Linked List Implementation

### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### LinkedList Class

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if list is empty"""
        return self.head is None

    def insert_at_beginning(self, data):
        """
        Insert node at the beginning
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert node at the end
        Time Complexity: O(n)
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, position):
        """
        Insert node at specific position
        Time Complexity: O(n)
        """
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current:
            new_node.next = current.next
            current.next = new_node

    def delete_at_beginning(self):
        """
        Delete first node
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None

        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def delete_at_end(self):
        """
        Delete last node
        Time Complexity: O(n)
        """
        if self.is_empty():
            return None

        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data

        current = self.head
        while current.next.next:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        return deleted_data

    def delete_by_value(self, value):
        """
        Delete first occurrence of value
        Time Complexity: O(n)
        """
        if self.is_empty():
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, value):
        """
        Search for a value
        Time Complexity: O(n)
        """
        current = self.head
        position = 0

        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1

    def display(self):
        """Print all elements"""
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")

    def get_length(self):
        """
        Get number of nodes
        Time Complexity: O(n)
        """
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

# Usage Example
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
ll.display()  # 0 -> 1 -> 2 -> 3 -> None

print(f"Length: {ll.get_length()}")  # 4
print(f"Search 2: {ll.search(2)}")   # 2

ll.delete_by_value(2)
ll.display()  # 0 -> 1 -> 3 -> None
```

## Time Complexity Comparison

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(n) | O(1) |
| Insert at end | O(1) | O(n) |
| Insert at position | O(n) | O(n) |
| Delete at beginning | O(n) | O(1) |
| Delete at end | O(1) | O(n) |

## Doubly Linked List

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert at beginning
        Time Complexity: O(1)
        """
        new_node = DNode(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert at end
        Time Complexity: O(n)
        """
        new_node = DNode(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        """Display from head to tail"""
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" <-> ".join(elements))

    def display_backward(self):
        """Display from tail to head"""
        if not self.head:
            return

        current = self.head
        while current.next:
            current = current.next

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev

        print(" <-> ".join(elements))

# Usage
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display_forward()   # 1 <-> 2 <-> 3
dll.display_backward()  # 3 <-> 2 <-> 1
```

## Common Linked List Problems

### 1. Reverse a Linked List

```python
def reverse_linked_list(head):
    """
    Reverse a singly linked list
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Method for LinkedList class
def reverse(self):
    """Reverse the linked list in place"""
    self.head = reverse_linked_list(self.head)
```

### 2. Detect Cycle (Floyd's Algorithm)

```python
def has_cycle(head):
    """
    Detect if linked list has a cycle
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

### 3. Find Middle Element

```python
def find_middle(head):
    """
    Find middle node using slow/fast pointers
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### 4. Merge Two Sorted Lists

```python
def merge_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists
    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next
```

### 5. Remove Nth Node from End

```python
def remove_nth_from_end(head, n):
    """
    Remove nth node from end of list
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both until fast reaches end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next
```

### 6. Check if Palindrome

```python
def is_palindrome(head):
    """
    Check if linked list is palindrome
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare both halves
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True
```

### 7. Remove Duplicates from Sorted List

```python
def remove_duplicates(head):
    """
    Remove duplicates from sorted linked list
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
```

## Advantages of Linked Lists

1. **Dynamic Size** - Can grow/shrink at runtime
2. **Efficient Insertion/Deletion** - O(1) at beginning
3. **No Memory Waste** - Allocate only what's needed
4. **Easy Implementation** - Of stacks and queues

## Disadvantages of Linked Lists

1. **No Random Access** - Must traverse sequentially
2. **Extra Memory** - For storing pointers
3. **Not Cache Friendly** - Non-contiguous memory
4. **Reverse Traversal** - Difficult in singly linked lists

## When to Use Linked Lists

Use Linked Lists when:
- Frequent insertions/deletions at beginning
- Unknown size of data
- Don't need random access
- Implementing stacks, queues, or graphs

Use Arrays when:
- Need random access
- Mostly reading data
- Size is known or stable
- Memory locality is important

!!! tip "Practice Problems"
    Try solving these classic problems:
    - Add two numbers represented as linked lists
    - Find intersection point of two lists
    - Rotate linked list
    - Clone linked list with random pointer
    - Sort linked list (Merge Sort)

!!! note "Implementation Note"
    Python doesn't have built-in linked lists. For production code, consider using:
    - `collections.deque` for double-ended operations
    - `list` for most general-purpose needs
    - Only implement custom linked lists when specifically needed

---

**Next Tutorial:** [Trees and Binary Search Trees](05_trees.md)