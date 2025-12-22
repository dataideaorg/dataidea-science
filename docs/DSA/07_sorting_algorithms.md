# Sorting Algorithms

Sorting is the process of arranging elements in a specific order (ascending or descending). Sorting algorithms are fundamental to computer science and are used in many applications.

## Why Learn Sorting?

1. **Foundation for Other Algorithms** - Binary search requires sorted data
2. **Data Organization** - Makes data easier to analyze
3. **Interview Questions** - Commonly asked in technical interviews
4. **Performance Analysis** - Understanding time/space complexity
5. **Real-World Applications** - Databases, file systems, search engines

## Comparison of Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |

**Stable**: Maintains relative order of equal elements

## 1. Bubble Sort

Repeatedly swap adjacent elements if they're in wrong order.

### Algorithm:
1. Compare adjacent elements
2. Swap if in wrong order
3. Repeat until no swaps needed

```python
def bubble_sort(arr):
    """
    Bubble Sort
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # [11, 12, 22, 25, 34, 64, 90]
```

### When to Use:
- Small datasets
- Nearly sorted data
- Educational purposes

## 2. Selection Sort

Find minimum element and place it at beginning.

### Algorithm:
1. Find minimum in unsorted portion
2. Swap with first unsorted element
3. Move boundary of sorted portion

```python
def selection_sort(arr):
    """
    Selection Sort
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)

    for i in range(n):
        min_idx = i

        # Find minimum in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Test
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
```

### When to Use:
- Small datasets
- Memory is limited (in-place)
- When number of swaps matters

## 3. Insertion Sort

Build sorted array one element at a time.

### Algorithm:
1. Start with second element
2. Compare with elements before it
3. Insert in correct position
4. Repeat for all elements

```python
def insertion_sort(arr):
    """
    Insertion Sort
    Time Complexity: O(n²) average, O(n) best
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Test
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # [5, 6, 11, 12, 13]
```

### When to Use:
- Small datasets
- Nearly sorted data
- Online sorting (sort as data arrives)
- Used in hybrid algorithms (Timsort)

## 4. Merge Sort

Divide and conquer algorithm that splits array and merges sorted halves.

### Algorithm:
1. Divide array into two halves
2. Recursively sort each half
3. Merge sorted halves

```python
def merge_sort(arr):
    """
    Merge Sort
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (Merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]
```

### When to Use:
- Need guaranteed O(n log n)
- Stable sort required
- Sorting linked lists
- External sorting (large datasets)

## 5. Quick Sort

Divide and conquer using pivot element.

### Algorithm:
1. Choose pivot element
2. Partition: elements < pivot on left, > pivot on right
3. Recursively sort left and right partitions

```python
def quick_sort(arr):
    """
    Quick Sort
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# In-place version
def quick_sort_inplace(arr, low, high):
    """Quick Sort (in-place)"""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

    return arr

def partition(arr, low, high):
    """Partition array around pivot"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))  # [1, 5, 7, 8, 9, 10]

arr2 = [10, 7, 8, 9, 1, 5]
print(quick_sort_inplace(arr2, 0, len(arr2) - 1))  # [1, 5, 7, 8, 9, 10]
```

### When to Use:
- General purpose sorting
- Average case O(n log n)
- In-place sorting needed
- Used in many standard libraries

## 6. Heap Sort

Uses binary heap data structure.

### Algorithm:
1. Build max heap from array
2. Extract maximum (root) to end
3. Heapify remaining elements
4. Repeat

```python
def heap_sort(arr):
    """
    Heap Sort
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    """Heapify subtree rooted at index i"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Test
arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))  # [5, 6, 7, 11, 12, 13]
```

### When to Use:
- Guaranteed O(n log n)
- In-place sorting
- When auxiliary space is limited

## 7. Counting Sort

Non-comparison based sorting for integers in specific range.

### Algorithm:
1. Count occurrences of each value
2. Calculate cumulative counts
3. Place elements in sorted order

```python
def counting_sort(arr):
    """
    Counting Sort
    Time Complexity: O(n + k) where k is range
    Space Complexity: O(k)
    """
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct sorted array
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i + min_val] * cnt)

    return sorted_arr

# Test
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))  # [1, 2, 2, 3, 3, 4, 8]
```

### When to Use:
- Small range of integers
- Need linear time O(n)
- Stable sort required

## 8. Radix Sort

Sorts by processing digits from least to most significant.

```python
def radix_sort(arr):
    """
    Radix Sort
    Time Complexity: O(nk) where k is number of digits
    Space Complexity: O(n + k)
    """
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def counting_sort_by_digit(arr, exp):
    """Counting sort by specific digit"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy to original
    for i in range(n):
        arr[i] = output[i]

# Test
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # [2, 24, 45, 66, 75, 90, 170, 802]
```

### When to Use:
- Sorting integers or strings
- Need linear time
- Fixed number of digits

## Python's Built-in Sorting

Python uses **Timsort**, a hybrid of Merge Sort and Insertion Sort.

```python
# Sort list in-place
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()
print(arr)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort and return new list
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = sorted(arr)
print(sorted_arr)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sort
arr.sort(reverse=True)
print(arr)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Custom key function
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)
print(words)  # ['pie', 'book', 'banana', 'Washington']

# Sort by multiple criteria
students = [('Alice', 85), ('Bob', 75), ('Charlie', 85)]
students.sort(key=lambda x: (-x[1], x[0]))  # By grade desc, then name asc
print(students)  # [('Alice', 85), ('Charlie', 85), ('Bob', 75)]
```

## Sorting Comparisons

### Stable vs Unstable:
- **Stable**: Maintains relative order of equal elements (Merge, Insertion, Bubble)
- **Unstable**: May change relative order (Quick, Heap, Selection)

### In-place vs Not In-place:
- **In-place**: O(1) extra space (Quick, Heap, Insertion)
- **Not in-place**: O(n) extra space (Merge, Counting, Radix)

## Common Sorting Problems

### 1. Sort Colors (Dutch National Flag)

```python
def sort_colors(nums):
    """
    Sort array with values 0, 1, 2
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

# Test
nums = [2, 0, 2, 1, 1, 0]
print(sort_colors(nums))  # [0, 0, 1, 1, 2, 2]
```

### 2. Merge Intervals

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals
    Time Complexity: O(n log n)
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)

    return merged

# Test
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # [[1, 6], [8, 10], [15, 18]]
```

### 3. Kth Largest Element

```python
def find_kth_largest(nums, k):
    """
    Find kth largest element using Quick Select
    Time Complexity: O(n) average
    """
    def partition(left, right):
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    left, right = 0, len(nums) - 1
    k_index = k - 1

    while left <= right:
        pivot_index = partition(left, right)

        if pivot_index == k_index:
            return nums[pivot_index]
        elif pivot_index < k_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

# Test
nums = [3, 2, 1, 5, 6, 4]
print(find_kth_largest(nums, 2))  # 5

# Using Python's built-in
import heapq
print(heapq.nlargest(2, nums)[-1])  # 5
```

!!! tip "Choosing the Right Algorithm"
    - **Small arrays (< 50)**: Insertion Sort
    - **General purpose**: Quick Sort or Timsort (Python's default)
    - **Guaranteed O(n log n)**: Merge Sort or Heap Sort
    - **Nearly sorted**: Insertion Sort
    - **Integers in small range**: Counting Sort or Radix Sort
    - **Need stability**: Merge Sort or Timsort

!!! note "Practice Problems"
    Try solving these sorting problems:
    - Sort array by parity
    - Largest number
    - Sort characters by frequency
    - Meeting rooms (interval scheduling)
    - Top K frequent elements

---

**Previous Tutorial:** [Hash Tables](06_hash_tables.md)
