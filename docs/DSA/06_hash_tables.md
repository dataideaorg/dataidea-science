# Hash Tables

A **Hash Table** (or Hash Map) is a data structure that stores key-value pairs and provides fast lookup, insertion, and deletion operations using a hash function.

## What is a Hash Table?

Hash tables use a **hash function** to compute an index into an array of buckets, from which the desired value can be found.

### Key Concepts:

- **Hash Function**: Converts key to array index
- **Bucket**: Storage location for key-value pair
- **Collision**: When two keys hash to same index
- **Load Factor**: Ratio of stored elements to table size

```
Key -> Hash Function -> Index -> Value

"apple" -> hash("apple") -> 3 -> {"color": "red", "taste": "sweet"}
```

## How Hash Tables Work

```python
# Conceptual example
hash_table = [None] * 10  # Array of 10 buckets

def hash_function(key):
    """Simple hash function"""
    return sum(ord(c) for c in key) % 10

# Insert
key = "apple"
index = hash_function(key)  # e.g., 3
hash_table[index] = ("apple", "red")

# Retrieve
index = hash_function("apple")
value = hash_table[index]  # ("apple", "red")
```

## Python Dictionary (Built-in Hash Table)

Python's `dict` is an optimized hash table implementation.

```python
# Create dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Access - O(1)
print(student["name"])  # Alice

# Insert/Update - O(1)
student["major"] = "Computer Science"
student["age"] = 21

# Delete - O(1)
del student["grade"]

# Check key existence - O(1)
if "name" in student:
    print("Name exists")

# Get with default - O(1)
major = student.get("major", "Undecided")

# Iterate
for key, value in student.items():
    print(f"{key}: {value}")
```

## Hash Table Operations

### Common Operations

```python
# Create
hash_map = {}

# Insert/Update
hash_map["key1"] = "value1"
hash_map["key2"] = "value2"

# Get
value = hash_map.get("key1")  # "value1"
value = hash_map.get("key3", "default")  # "default"

# Delete
hash_map.pop("key1")  # Returns "value1"
# or
del hash_map["key2"]

# Check existence
exists = "key1" in hash_map  # False

# Get all keys
keys = hash_map.keys()

# Get all values
values = hash_map.values()

# Get all items
items = hash_map.items()

# Clear
hash_map.clear()
```

## Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

*Worst case occurs when all keys hash to same index (many collisions)*

## Implementing a Hash Table

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        """Hash function using built-in hash"""
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert key-value pair
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Insert new key-value pair
        bucket.append((key, value))
        self.count += 1

        # Resize if load factor > 0.7
        if self.count / self.size > 0.7:
            self._resize()

    def get(self, key):
        """
        Get value by key
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def delete(self, key):
        """
        Delete key-value pair
        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return v

        raise KeyError(key)

    def _resize(self):
        """Resize table when load factor is high"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def __contains__(self, key):
        """Check if key exists"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        """Return number of items"""
        return self.count

    def __str__(self):
        """String representation"""
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return str(dict(items))

# Usage
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 3)
ht.insert("orange", 7)

print(ht.get("apple"))  # 5
print("banana" in ht)   # True
ht.delete("orange")
print(len(ht))          # 2
```

## Collision Resolution

### 1. Chaining (Separate Chaining)
Each bucket stores a list of key-value pairs.

```python
# Example: Multiple keys hash to same index
table = [
    [],
    [("key1", "val1"), ("key5", "val5")],  # Collision
    [("key2", "val2")],
    []
]
```

### 2. Open Addressing
Find next available slot when collision occurs.

```python
def linear_probing(self, key):
    """
    Linear probing: try index, index+1, index+2, ...
    """
    index = self._hash(key)
    original_index = index

    while self.table[index] is not None:
        if self.table[index][0] == key:
            return index
        index = (index + 1) % self.size

        # Checked all slots
        if index == original_index:
            return None

    return index
```

## Common Hash Table Problems

### 1. Two Sum

```python
def two_sum(nums, target):
    """
    Find two numbers that sum to target
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None

# Test
nums = [2, 7, 11, 15]
print(two_sum(nums, 9))  # [0, 1]
```

### 2. First Non-Repeating Character

```python
def first_non_repeating(s):
    """
    Find first non-repeating character
    Time Complexity: O(n)
    Space Complexity: O(1) - at most 26 letters
    """
    char_count = {}

    # Count occurrences
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return None

# Test
print(first_non_repeating("leetcode"))  # 'l'
print(first_non_repeating("aabbcc"))    # None
```

### 3. Group Anagrams

```python
def group_anagrams(words):
    """
    Group anagrams together
    Time Complexity: O(n * k log k) where k is max word length
    Space Complexity: O(n * k)
    """
    from collections import defaultdict

    anagram_groups = defaultdict(list)

    for word in words:
        # Sort characters as key
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)

    return list(anagram_groups.values())

# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### 4. Longest Consecutive Sequence

```python
def longest_consecutive(nums):
    """
    Find longest consecutive sequence
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start sequence if num-1 not in set
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

# Test
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # 4 (sequence: 1, 2, 3, 4)
```

### 5. Subarray Sum Equals K

```python
def subarray_sum(nums, k):
    """
    Count subarrays with sum equal to k
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # Initialize with 0 sum

    for num in nums:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        # Update sum count
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count

# Test
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # 2
```

## Python Collections for Hash Tables

### 1. defaultdict

```python
from collections import defaultdict

# Auto-initialize missing keys
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1

print(word_count)  # {'apple': 2, 'banana': 1}

# With lists
groups = defaultdict(list)
groups["fruits"].append("apple")
groups["fruits"].append("banana")
```

### 2. Counter

```python
from collections import Counter

# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

# Operations
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['b', 'c', 'd'])
print(c1 + c2)  # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})
```

### 3. OrderedDict

```python
from collections import OrderedDict

# Maintains insertion order (note: regular dict also maintains order in Python 3.7+)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Move to end
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
```

## Hash Function Design

### Good Hash Function Properties:

1. **Deterministic** - Same input gives same output
2. **Uniform Distribution** - Minimizes collisions
3. **Fast Computation** - O(1) time
4. **Uses all input data** - Avoids clustering

```python
# Simple hash functions
def hash_string(s, table_size):
    """Polynomial rolling hash"""
    hash_value = 0
    for char in s:
        hash_value = (hash_value * 31 + ord(char)) % table_size
    return hash_value

def hash_number(num, table_size):
    """Modulo hash for integers"""
    return num % table_size
```

## Applications of Hash Tables

1. **Caching** - Store computed results (LRU cache)
2. **Databases** - Fast indexing and lookup
3. **Symbol Tables** - Compilers and interpreters
4. **Removing Duplicates** - Using set
5. **Frequency Counting** - Character/word counts
6. **Routing** - IP address lookup
7. **Password Verification** - Storing hashed passwords

## Advantages

1. **Fast Operations** - O(1) average for insert, delete, search
2. **Flexible Keys** - Any hashable type
3. **Dynamic** - Can grow as needed
4. **Easy to Implement** - Simple interface

## Disadvantages

1. **Space Overhead** - Extra memory for hash table
2. **No Order** - Keys are not sorted (use OrderedDict if needed)
3. **Hash Function** - Quality affects performance
4. **Worst Case** - O(n) with many collisions

!!! tip "Practice Problems"
    Try solving these hash table problems:
    - Valid Sudoku
    - Longest substring without repeating characters
    - Top K frequent elements
    - Design LRU Cache
    - Isomorphic strings

!!! note "When to Use Hash Tables"
    Use hash tables when you need:
    - Fast lookup by key (O(1))
    - Counting occurrences
    - Removing duplicates
    - Caching results
    - Mapping relationships

---

**Next Tutorial:** [Sorting Algorithms](07_sorting_algorithms.md)