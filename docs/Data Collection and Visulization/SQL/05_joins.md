# SQL Joins

Learn how to combine data from multiple tables using different types of joins.

## What are Joins?

Joins are used to combine rows from two or more tables based on a related column between them. This is one of the most powerful features of SQL.

## Sample Tables

We'll use these two tables throughout this tutorial:

**customers table:**
```
+----+-----------+-------------+
| id | name      | city        |
+----+-----------+-------------+
| 1  | Alice     | New York    |
| 2  | Bob       | Los Angeles |
| 3  | Charlie   | Chicago     |
| 4  | Diana     | Houston     |
+----+-----------+-------------+
```

**orders table:**
```
+----+-------------+--------+------------+
| id | customer_id | amount | order_date |
+----+-------------+--------+------------+
| 1  | 1           | 250    | 2024-01-15 |
| 2  | 1           | 180    | 2024-01-20 |
| 3  | 2           | 320    | 2024-01-18 |
| 4  | 5           | 150    | 2024-01-22 |
+----+-------------+--------+------------+
```

Note: customer_id 5 doesn't exist in customers table, and customers 3 and 4 have no orders.

## INNER JOIN

Returns only matching rows from both tables.

### Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

### Example

```sql
SELECT
    customers.name,
    customers.city,
    orders.amount,
    orders.order_date
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;
```

**Result:**
```
+-----------+-------------+--------+------------+
| name      | city        | amount | order_date |
+-----------+-------------+--------+------------+
| Alice     | New York    | 250    | 2024-01-15 |
| Alice     | New York    | 180    | 2024-01-20 |
| Bob       | Los Angeles | 320    | 2024-01-18 |
+-----------+-------------+--------+------------+
```

Note: Charlie and Diana are excluded (no orders), and order with customer_id 5 is excluded (no matching customer).

### Using Table Aliases

```sql
SELECT
    c.name,
    c.city,
    o.amount
FROM customers c
INNER JOIN orders o
ON c.id = o.customer_id;
```

## LEFT JOIN (LEFT OUTER JOIN)

Returns all rows from the left table and matching rows from the right table. NULL for non-matching rows.

### Syntax

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

### Example

```sql
SELECT
    c.name,
    c.city,
    o.amount,
    o.order_date
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id;
```

**Result:**
```
+-----------+-------------+--------+------------+
| name      | city        | amount | order_date |
+-----------+-------------+--------+------------+
| Alice     | New York    | 250    | 2024-01-15 |
| Alice     | New York    | 180    | 2024-01-20 |
| Bob       | Los Angeles | 320    | 2024-01-18 |
| Charlie   | Chicago     | NULL   | NULL       |
| Diana     | Houston     | NULL   | NULL       |
+-----------+-------------+--------+------------+
```

All customers are included, even those without orders.

### Finding Customers Without Orders

```sql
SELECT c.name, c.city
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.id IS NULL;
```

**Result:**
```
+-----------+---------+
| name      | city    |
+-----------+---------+
| Charlie   | Chicago |
| Diana     | Houston |
+-----------+---------+
```

## RIGHT JOIN (RIGHT OUTER JOIN)

Returns all rows from the right table and matching rows from the left table.

### Example

```sql
SELECT
    c.name,
    o.amount,
    o.order_date
FROM customers c
RIGHT JOIN orders o
ON c.id = o.customer_id;
```

**Result:**
```
+-----------+--------+------------+
| name      | amount | order_date |
+-----------+--------+------------+
| Alice     | 250    | 2024-01-15 |
| Alice     | 180    | 2024-01-20 |
| Bob       | 320    | 2024-01-18 |
| NULL      | 150    | 2024-01-22 |
+-----------+--------+------------+
```

All orders included, even the one with non-existent customer_id 5.

## FULL OUTER JOIN

Returns all rows when there's a match in either table.

!!! note "Database Support"
    Not all databases support FULL OUTER JOIN (e.g., MySQL doesn't). You can simulate it using UNION of LEFT and RIGHT joins.

### Syntax

```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

### Simulating FULL OUTER JOIN in MySQL

```sql
SELECT c.name, o.amount
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id

UNION

SELECT c.name, o.amount
FROM customers c
RIGHT JOIN orders o ON c.id = o.customer_id;
```

## CROSS JOIN

Returns the Cartesian product of both tables (all possible combinations).

### Example

```sql
SELECT c.name, o.amount
FROM customers c
CROSS JOIN orders o;
```

This creates 16 rows (4 customers × 4 orders).

!!! warning "Use with Caution"
    CROSS JOIN can produce very large result sets. Use it only when you need all combinations.

## SELF JOIN

A table joined with itself.

### Example: Employee-Manager Relationship

**employees table:**
```
+----+-----------+------------+
| id | name      | manager_id |
+----+-----------+------------+
| 1  | Alice     | NULL       |
| 2  | Bob       | 1          |
| 3  | Charlie   | 1          |
| 4  | Diana     | 2          |
+----+-----------+------------+
```

```sql
SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;
```

**Result:**
```
+-----------+---------+
| employee  | manager |
+-----------+---------+
| Alice     | NULL    |
| Bob       | Alice   |
| Charlie   | Alice   |
| Diana     | Bob     |
+-----------+---------+
```

## Multiple Joins

Join more than two tables together.

### Example with Three Tables

**products table:**
```
+----+----------+-------+
| id | name     | price |
+----+----------+-------+
| 1  | Laptop   | 1000  |
| 2  | Mouse    | 25    |
+----+----------+-------+
```

**order_items table:**
```
+----+----------+------------+----------+
| id | order_id | product_id | quantity |
+----+----------+------------+----------+
| 1  | 1        | 1          | 2        |
| 2  | 1        | 2          | 1        |
| 3  | 2        | 1          | 1        |
+----+----------+------------+----------+
```

```sql
SELECT
    c.name AS customer,
    p.name AS product,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;
```

## Join with Aggregation

Combine joins with aggregate functions.

```sql
SELECT
    c.name,
    COUNT(o.id) AS order_count,
    COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY total_spent DESC;
```

**Result:**
```
+-----------+-------------+-------------+
| name      | order_count | total_spent |
+-----------+-------------+-------------+
| Alice     | 2           | 430         |
| Bob       | 1           | 320         |
| Charlie   | 0           | 0           |
| Diana     | 0           | 0           |
+-----------+-------------+-------------+
```

## Practice Exercises

Given these tables:

**authors:**
```
+----+-----------+
| id | name      |
+----+-----------+
| 1  | J.K. Rowling |
| 2  | George Orwell |
| 3  | Jane Austen |
+----+-----------+
```

**books:**
```
+----+-----------+-------------+------+
| id | title     | author_id   | year |
+----+-----------+-------------+------+
| 1  | Book A    | 1           | 1997 |
| 2  | Book B    | 1           | 1999 |
| 3  | Book C    | 2           | 1949 |
+----+-----------+-------------+------+
```

Try these queries:

1. List all books with their author names
2. Find authors who have written more than one book
3. List all authors, including those without books
4. Find authors who haven't written any books
5. Count the number of books per author

??? success "Solutions"
    ```sql
    -- 1. Books with author names
    SELECT b.title, a.name AS author, b.year
    FROM books b
    INNER JOIN authors a ON b.author_id = a.id;

    -- 2. Authors with more than one book
    SELECT a.name, COUNT(b.id) AS book_count
    FROM authors a
    INNER JOIN books b ON a.id = b.author_id
    GROUP BY a.id, a.name
    HAVING COUNT(b.id) > 1;

    -- 3. All authors including those without books
    SELECT a.name, b.title
    FROM authors a
    LEFT JOIN books b ON a.id = b.author_id;

    -- 4. Authors without books
    SELECT a.name
    FROM authors a
    LEFT JOIN books b ON a.id = b.author_id
    WHERE b.id IS NULL;

    -- 5. Book count per author
    SELECT a.name, COUNT(b.id) AS book_count
    FROM authors a
    LEFT JOIN books b ON a.id = b.author_id
    GROUP BY a.id, a.name
    ORDER BY book_count DESC;
    ```

## Visual Join Guide

```
INNER JOIN: Only matching rows
[A] ∩ [B]

LEFT JOIN: All from left + matching from right
[A] + [A ∩ B]

RIGHT JOIN: All from right + matching from left
[B] + [A ∩ B]

FULL OUTER JOIN: Everything
[A] + [B]

CROSS JOIN: All combinations
[A] × [B]
```

!!! tip "Join Performance"
    - Always join on indexed columns
    - Use INNER JOIN when possible (faster than OUTER JOINs)
    - Filter early using WHERE clauses
    - Consider using subqueries for complex joins

---

**Previous:** [Aggregate Functions](04_aggregate_functions.md) | **Next:** [Subqueries](06_subqueries.md)