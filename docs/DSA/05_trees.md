# Trees and Binary Search Trees

A **Tree** is a hierarchical data structure consisting of nodes connected by edges. Unlike linear data structures, trees represent hierarchical relationships.

## Tree Terminology

```
         1         <- Root
       /   \
      2     3      <- Children of 1 (Siblings)
     / \     \
    4   5     6    <- Leaf nodes (4, 5, 6)
```

- **Root**: Top node (1)
- **Parent**: Node with children (1, 2, 3)
- **Child**: Node descended from another (2, 3 are children of 1)
- **Leaf**: Node with no children (4, 5, 6)
- **Sibling**: Nodes with same parent (2 and 3)
- **Edge**: Connection between nodes
- **Path**: Sequence of nodes and edges
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to node
- **Level**: All nodes at same depth

## Types of Trees

### 1. Binary Tree
Each node has at most 2 children (left and right).

### 2. Binary Search Tree (BST)
Binary tree where left child < parent < right child.

### 3. AVL Tree
Self-balancing BST.

### 4. Red-Black Tree
Self-balancing BST with color properties.

### 5. B-Tree
Self-balancing tree for databases.

### 6. Heap
Complete binary tree with heap property.

## Binary Tree Implementation

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert node (level-order insertion)"""
        new_node = TreeNode(data)

        if not self.root:
            self.root = new_node
            return

        from collections import deque
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)
```

## Binary Search Tree (BST)

A BST maintains the property: **left child < parent < right child**

```python
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert value into BST
        Time Complexity: O(log n) average, O(n) worst
        """
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return BSTNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)

        return node

    def search(self, data):
        """
        Search for value in BST
        Time Complexity: O(log n) average, O(n) worst
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self._search_recursive(node.left, data)

        return self._search_recursive(node.right, data)

    def delete(self, data):
        """
        Delete value from BST
        Time Complexity: O(log n) average, O(n) worst
        """
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data)

        return node

    def _find_min(self, node):
        """Find minimum value node"""
        current = node
        while current.left:
            current = current.left
        return current

    def find_min(self):
        """Find minimum value in tree"""
        if not self.root:
            return None
        node = self._find_min(self.root)
        return node.data

    def find_max(self):
        """Find maximum value in tree"""
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

# Usage
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    bst.insert(val)

print(bst.search(40))  # Returns node with data 40
print(bst.find_min())  # 20
print(bst.find_max())  # 80
```

## Tree Traversals

### 1. Inorder Traversal (Left, Root, Right)
For BST, gives sorted order.

```python
def inorder_traversal(root):
    """
    Left -> Root -> Right
    Time Complexity: O(n)
    """
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.data)
            traverse(node.right)

    traverse(root)
    return result

# For BST with values [50, 30, 70, 20, 40, 60, 80]
# Output: [20, 30, 40, 50, 60, 70, 80]
```

### 2. Preorder Traversal (Root, Left, Right)
Used for creating copy of tree.

```python
def preorder_traversal(root):
    """
    Root -> Left -> Right
    Time Complexity: O(n)
    """
    result = []

    def traverse(node):
        if node:
            result.append(node.data)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return result

# Output: [50, 30, 20, 40, 70, 60, 80]
```

### 3. Postorder Traversal (Left, Right, Root)
Used for deleting tree.

```python
def postorder_traversal(root):
    """
    Left -> Right -> Root
    Time Complexity: O(n)
    """
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.data)

    traverse(root)
    return result

# Output: [20, 40, 30, 60, 80, 70, 50]
```

### 4. Level Order Traversal (BFS)
Visit nodes level by level.

```python
def level_order_traversal(root):
    """
    Level by level (BFS)
    Time Complexity: O(n)
    """
    if not root:
        return []

    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Output: [50, 30, 70, 20, 40, 60, 80]
```

## Tree Properties

### Height of Tree

```python
def height(root):
    """
    Calculate height of tree
    Time Complexity: O(n)
    """
    if not root:
        return -1  # or 0, depending on definition

    return 1 + max(height(root.left), height(root.right))
```

### Count Nodes

```python
def count_nodes(root):
    """
    Count total nodes
    Time Complexity: O(n)
    """
    if not root:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### Check if Balanced

```python
def is_balanced(root):
    """
    Check if tree is height-balanced
    Time Complexity: O(n)
    """
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1
```

## Common Tree Problems

### 1. Validate BST

```python
def is_valid_bst(root):
    """
    Check if tree is valid BST
    Time Complexity: O(n)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.data <= min_val or node.data >= max_val:
            return False

        return (validate(node.left, min_val, node.data) and
                validate(node.right, node.data, max_val))

    return validate(root, float('-inf'), float('inf'))
```

### 2. Lowest Common Ancestor (BST)

```python
def lowest_common_ancestor(root, p, q):
    """
    Find LCA in BST
    Time Complexity: O(log n) average
    """
    if not root:
        return None

    if p.data < root.data and q.data < root.data:
        return lowest_common_ancestor(root.left, p, q)
    elif p.data > root.data and q.data > root.data:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root
```

### 3. Maximum Path Sum

```python
def max_path_sum(root):
    """
    Find maximum path sum
    Time Complexity: O(n)
    """
    max_sum = float('-inf')

    def helper(node):
        nonlocal max_sum

        if not node:
            return 0

        left = max(0, helper(node.left))
        right = max(0, helper(node.right))

        max_sum = max(max_sum, left + right + node.data)

        return max(left, right) + node.data

    helper(root)
    return max_sum
```

### 4. Serialize and Deserialize

```python
def serialize(root):
    """
    Serialize tree to string
    Time Complexity: O(n)
    """
    def helper(node):
        if not node:
            return "None,"

        return str(node.data) + "," + helper(node.left) + helper(node.right)

    return helper(root)

def deserialize(data):
    """
    Deserialize string to tree
    Time Complexity: O(n)
    """
    def helper():
        val = next(values)

        if val == "None":
            return None

        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()

        return node

    values = iter(data.split(','))
    return helper()
```

### 5. Mirror Tree

```python
def mirror_tree(root):
    """
    Create mirror of tree
    Time Complexity: O(n)
    """
    if not root:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    # Recursively mirror subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root
```

## BST Operations Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Find Min/Max | O(log n) | O(n) |

*Worst case occurs with unbalanced tree (like linked list)*

## Balanced Trees

To ensure O(log n) operations, use self-balancing trees:

- **AVL Tree**: Strictly balanced, faster lookups
- **Red-Black Tree**: Less strict, faster insertions
- **B-Tree**: Multi-way tree for databases

## Applications of Trees

1. **File Systems** - Directory structure
2. **Databases** - Indexing (B-trees)
3. **Compilers** - Abstract Syntax Trees
4. **Routing** - Decision trees
5. **HTML DOM** - Document structure
6. **AI** - Game trees, decision trees
7. **Networking** - Routing tables

!!! tip "Practice Problems"
    Try solving these tree problems:
    - Diameter of binary tree
    - Vertical order traversal
    - Right view of binary tree
    - Construct tree from inorder and preorder
    - Binary tree to doubly linked list

!!! note "When to Use BST"
    Use BST when you need:
    - Dynamic sorted data
    - Fast search, insert, delete (O(log n))
    - Range queries
    - Finding min/max efficiently

---

**Next Tutorial:** [Hash Tables](06_hash_tables.md)