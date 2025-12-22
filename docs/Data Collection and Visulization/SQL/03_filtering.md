# Filtering and Pattern Matching

Learn advanced filtering techniques including pattern matching, ranges, and NULL handling.

## IN Operator

The `IN` operator allows you to specify multiple values in a WHERE clause.

### Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

### Example

Instead of writing:
```sql
SELECT * FROM students
WHERE city = 'NYC' OR city = 'LA' OR city = 'Chicago';
```

You can write:
```sql
SELECT * FROM students
WHERE city IN ('NYC', 'LA', 'Chicago');
```

**Using NOT IN:**
```sql
SELECT * FROM students
WHERE grade NOT IN ('C', 'F');
```

## BETWEEN Operator

The `BETWEEN` operator selects values within a given range (inclusive).

### Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

### Examples

**Numeric ranges:**
```sql
SELECT name, age FROM students
WHERE age BETWEEN 20 AND 22;
```

**Result:**
```
+-----------+-----+
| name      | age |
+-----------+-----+
| Alice     | 20  |
| Bob       | 22  |
| Charlie   | 21  |
| Eva       | 20  |
+-----------+-----+
```

**Date ranges:**
```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
```

**NOT BETWEEN:**
```sql
SELECT name, age FROM students
WHERE age NOT BETWEEN 20 AND 21;
```

## LIKE Operator

The `LIKE` operator searches for a specified pattern in a column.

### Wildcards

| Wildcard | Description | Example |
|----------|-------------|---------|
| `%` | Represents zero or more characters | `'a%'` finds values starting with "a" |
| `_` | Represents a single character | `'a_'` finds two-character values starting with "a" |

### Examples

**Starts with 'A':**
```sql
SELECT name FROM students
WHERE name LIKE 'A%';
```

**Result:**
```
+-----------+
| name      |
+-----------+
| Alice     |
+-----------+
```

**Ends with 'e':**
```sql
SELECT name FROM students
WHERE name LIKE '%e';
```

**Result:**
```
+-----------+
| name      |
+-----------+
| Alice     |
| Charlie   |
+-----------+
```

**Contains 'a' anywhere:**
```sql
SELECT name FROM students
WHERE name LIKE '%a%';
```

**Second letter is 'i':**
```sql
SELECT name FROM students
WHERE name LIKE '_i%';
```

**Result:**
```
+-----------+
| name      |
+-----------+
| Diana     |
+-----------+
```

**Exactly 3 characters:**
```sql
SELECT name FROM students
WHERE name LIKE '___';
```

**Result:**
```
+-----------+
| name      |
+-----------+
| Bob       |
| Eva       |
+-----------+
```

## Case-Insensitive Searching

Different databases handle case sensitivity differently:

**MySQL (case-insensitive by default):**
```sql
SELECT * FROM students WHERE name LIKE 'alice';
```

**PostgreSQL (case-sensitive, use ILIKE):**
```sql
SELECT * FROM students WHERE name ILIKE 'alice';
```

**SQL Server (use UPPER or LOWER):**
```sql
SELECT * FROM students WHERE UPPER(name) LIKE 'ALICE';
```

## NULL Values

`NULL` represents missing or unknown data. It's different from zero or empty string.

### IS NULL

Find records with NULL values:

```sql
SELECT * FROM students
WHERE email IS NULL;
```

### IS NOT NULL

Find records without NULL values:

```sql
SELECT * FROM students
WHERE email IS NOT NULL;
```

!!! warning "NULL Comparison"
    You cannot use `=` or `!=` with NULL. Always use `IS NULL` or `IS NOT NULL`.

    ```sql
    -- WRONG
    WHERE email = NULL

    -- CORRECT
    WHERE email IS NULL
    ```

## Combining Multiple Conditions

You can combine different filtering techniques:

```sql
SELECT name, age, city FROM students
WHERE (grade IN ('A', 'B'))
  AND (age BETWEEN 20 AND 22)
  AND (city LIKE '%C%')
  AND (email IS NOT NULL);
```

## Practical Examples

### Example 1: Find students whose name starts with 'C' or 'D' and are older than 20

```sql
SELECT * FROM students
WHERE name LIKE 'C%' OR name LIKE 'D%'
  AND age > 20;
```

### Example 2: Find students not from NYC or LA with grades A or B

```sql
SELECT name, city, grade FROM students
WHERE city NOT IN ('NYC', 'LA')
  AND grade IN ('A', 'B');
```

### Example 3: Find students with names containing 'ar' and age between 18-25

```sql
SELECT * FROM students
WHERE name LIKE '%ar%'
  AND age BETWEEN 18 AND 25;
```

## Pattern Matching Best Practices

1. **Use specific patterns** - `name LIKE 'A%'` is faster than `name LIKE '%A%'`
2. **Avoid leading wildcards** - `LIKE '%text'` can be slow on large tables
3. **Consider indexes** - Columns frequently used in LIKE should be indexed
4. **Use exact matches when possible** - `=` is faster than `LIKE`

## Practice Exercises

Using a hypothetical `employees` table:

```
+----+-----------+-----------+--------+------------+
| id | name      | department| salary | hire_date  |
+----+-----------+-----------+--------+------------+
| 1  | John Doe  | Sales     | 50000  | 2020-01-15 |
| 2  | Jane Smith| IT        | 75000  | 2019-06-20 |
| 3  | Bob Wilson| Sales     | 55000  | 2021-03-10 |
| 4  | Alice Lee | HR        | NULL   | 2022-01-05 |
+----+-----------+-----------+--------+------------+
```

Try these queries:

1. Find employees in Sales or IT departments
2. Find employees hired between 2020 and 2022
3. Find employees whose name contains 'son'
4. Find employees with no salary information
5. Find employees in Sales with salary above 52000

??? success "Solutions"
    ```sql
    -- 1. Employees in Sales or IT
    SELECT * FROM employees
    WHERE department IN ('Sales', 'IT');

    -- 2. Hired between 2020 and 2022
    SELECT * FROM employees
    WHERE hire_date BETWEEN '2020-01-01' AND '2022-12-31';

    -- 3. Name contains 'son'
    SELECT * FROM employees
    WHERE name LIKE '%son%';

    -- 4. No salary information
    SELECT * FROM employees
    WHERE salary IS NULL;

    -- 5. Sales employees with salary > 52000
    SELECT * FROM employees
    WHERE department = 'Sales' AND salary > 52000;
    ```

---

**Previous:** [Basic SQL Queries](02_basic_queries.md) | **Next:** [Aggregate Functions](04_aggregate_functions.md)