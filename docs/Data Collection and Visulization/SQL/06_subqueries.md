# Subqueries

Learn how to use queries within queries to solve complex data problems.

## What is a Subquery?

A subquery (also called an inner query or nested query) is a query within another SQL query. Subqueries can be used in SELECT, FROM, WHERE, and HAVING clauses.

## Sample Data

**employees table:**
```
+----+-----------+-----------+--------+
| id | name      | department| salary |
+----+-----------+-----------+--------+
| 1  | Alice     | IT        | 75000  |
| 2  | Bob       | Sales     | 50000  |
| 3  | Charlie   | IT        | 80000  |
| 4  | Diana     | HR        | 60000  |
| 5  | Eva       | Sales     | 55000  |
+----+-----------+-----------+--------+
```

## Subquery in WHERE Clause

The most common use of subqueries.

### Find employees earning more than the average salary

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**Result:**
```
+-----------+--------+
| name      | salary |
+-----------+--------+
| Alice     | 75000  |
| Charlie   | 80000  |
+-----------+--------+
```

**How it works:**
1. Inner query calculates: `AVG(salary) = 64000`
2. Outer query uses this value: `WHERE salary > 64000`

### Find the highest-paid employee

```sql
SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

## Subquery with IN Operator

Use subqueries that return multiple values with IN.

### Find employees in departments that have more than one employee

```sql
SELECT name, department
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING COUNT(*) > 1
);
```

**Result:**
```
+-----------+-----------+
| name      | department|
+-----------+-----------+
| Alice     | IT        |
| Bob       | Sales     |
| Charlie   | IT        |
| Eva       | Sales     |
+-----------+-----------+
```

### Find employees in IT or Sales (simple example)

```sql
SELECT name, salary
FROM employees
WHERE department IN (
    SELECT DISTINCT department
    FROM employees
    WHERE department IN ('IT', 'Sales')
);
```

## Subquery in FROM Clause

Use a subquery as a temporary table (also called a derived table).

### Calculate department statistics

```sql
SELECT
    dept_stats.department,
    dept_stats.avg_salary,
    dept_stats.employee_count
FROM (
    SELECT
        department,
        AVG(salary) AS avg_salary,
        COUNT(*) AS employee_count
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE dept_stats.avg_salary > 60000;
```

**Result:**
```
+-----------+------------+----------------+
| department| avg_salary | employee_count |
+-----------+------------+----------------+
| IT        | 77500      | 2              |
+-----------+------------+----------------+
```

!!! note "Alias Required"
    Subqueries in FROM clause must have an alias (e.g., `AS dept_stats`).

## Subquery in SELECT Clause

Return a single value in the SELECT list.

### Show each employee with the department average

```sql
SELECT
    name,
    salary,
    department,
    (SELECT AVG(salary)
     FROM employees e2
     WHERE e2.department = e1.department) AS dept_avg
FROM employees e1;
```

**Result:**
```
+-----------+--------+-----------+----------+
| name      | salary | department| dept_avg |
+-----------+--------+-----------+----------+
| Alice     | 75000  | IT        | 77500    |
| Bob       | 50000  | Sales     | 52500    |
| Charlie   | 80000  | IT        | 77500    |
| Diana     | 60000  | HR        | 60000    |
| Eva       | 55000  | Sales     | 52500    |
+-----------+--------+-----------+----------+
```

## Correlated Subqueries

A subquery that references columns from the outer query.

### Find employees earning more than their department average

```sql
SELECT name, department, salary
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

**Result:**
```
+-----------+-----------+--------+
| name      | department| salary |
+-----------+-----------+--------+
| Charlie   | IT        | 80000  |
| Eva       | Sales     | 55000  |
+-----------+-----------+--------+
```

**How it works:**
- For each row in outer query, inner query executes
- Inner query uses the current row's department
- Compares the salary with that department's average

## EXISTS Operator

Tests for the existence of rows in a subquery. Returns TRUE if subquery returns any rows.

### Find departments that have employees

```sql
SELECT DISTINCT department
FROM employees e1
WHERE EXISTS (
    SELECT 1
    FROM employees e2
    WHERE e2.department = e1.department
    AND e2.salary > 70000
);
```

**Result:**
```
+-----------+
| department|
+-----------+
| IT        |
+-----------+
```

### NOT EXISTS Example

Find departments with no high earners (salary > 70000):

```sql
SELECT DISTINCT department
FROM employees e1
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e2
    WHERE e2.department = e1.department
    AND e2.salary > 70000
);
```

## Multiple Row Subqueries

### ANY Operator

Compare with any value returned by the subquery.

```sql
-- Find employees earning more than ANY Sales employee
SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department = 'Sales'
);
```

This is equivalent to "greater than the minimum Sales salary."

### ALL Operator

Compare with all values returned by the subquery.

```sql
-- Find employees earning more than ALL Sales employees
SELECT name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department = 'Sales'
);
```

This is equivalent to "greater than the maximum Sales salary."

## Nested Subqueries

Subqueries within subqueries.

### Find employees in the highest-paying department

```sql
SELECT name, department, salary
FROM employees
WHERE department = (
    SELECT department
    FROM employees
    GROUP BY department
    ORDER BY AVG(salary) DESC
    LIMIT 1
);
```

**Result:**
```
+-----------+-----------+--------+
| name      | department| salary |
+-----------+-----------+--------+
| Alice     | IT        | 77500  |
| Charlie   | IT        | 80000  |
+-----------+-----------+--------+
```

## Common Table Expressions (CTE)

An alternative to subqueries that's often more readable. Uses WITH clause.

### Basic CTE

```sql
WITH dept_averages AS (
    SELECT
        department,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT
    e.name,
    e.salary,
    e.department,
    da.avg_salary
FROM employees e
JOIN dept_averages da ON e.department = da.department
WHERE e.salary > da.avg_salary;
```

### Multiple CTEs

```sql
WITH
high_earners AS (
    SELECT *
    FROM employees
    WHERE salary > 60000
),
dept_stats AS (
    SELECT
        department,
        COUNT(*) AS emp_count
    FROM high_earners
    GROUP BY department
)
SELECT *
FROM dept_stats
WHERE emp_count > 1;
```

## Subquery Performance Tips

1. **Use JOINs when possible** - Often faster than subqueries
   ```sql
   -- Instead of this:
   SELECT name FROM employees
   WHERE department IN (SELECT department FROM departments WHERE location = 'NY');

   -- Use this:
   SELECT e.name
   FROM employees e
   JOIN departments d ON e.department = d.department
   WHERE d.location = 'NY';
   ```

2. **Use EXISTS instead of IN for large datasets**
   ```sql
   -- Better performance with large subquery results:
   SELECT name FROM employees e
   WHERE EXISTS (
       SELECT 1 FROM orders o
       WHERE o.employee_id = e.id
   );
   ```

3. **Avoid correlated subqueries when possible** - They execute once per row

## Practice Exercises

Using this **products** and **sales** tables:

**products:**
```
+----+----------+-------+
| id | name     | price |
+----+----------+-------+
| 1  | Laptop   | 1000  |
| 2  | Mouse    | 25    |
| 3  | Keyboard | 75    |
+----+----------+-------+
```

**sales:**
```
+----+------------+----------+
| id | product_id | quantity |
+----+------------+----------+
| 1  | 1          | 5        |
| 2  | 2          | 20       |
| 3  | 1          | 3        |
+----+------------+----------+
```

Try these queries:

1. Find products with above-average price
2. Find products that have been sold
3. Find the most expensive product
4. Calculate total revenue per product
5. Find products sold more than once

??? success "Solutions"
    ```sql
    -- 1. Above-average price
    SELECT name, price
    FROM products
    WHERE price > (SELECT AVG(price) FROM products);

    -- 2. Products that have been sold
    SELECT name
    FROM products
    WHERE id IN (SELECT DISTINCT product_id FROM sales);

    -- 3. Most expensive product
    SELECT name, price
    FROM products
    WHERE price = (SELECT MAX(price) FROM products);

    -- 4. Total revenue per product (using CTE)
    WITH product_revenue AS (
        SELECT
            p.name,
            SUM(s.quantity * p.price) AS revenue
        FROM products p
        JOIN sales s ON p.id = s.product_id
        GROUP BY p.id, p.name
    )
    SELECT * FROM product_revenue
    ORDER BY revenue DESC;

    -- 5. Products sold more than once
    SELECT p.name
    FROM products p
    WHERE (
        SELECT COUNT(*)
        FROM sales s
        WHERE s.product_id = p.id
    ) > 1;
    ```

!!! tip "When to Use Subqueries"
    - When you need to filter based on aggregate values
    - When the subquery is simple and returns few rows
    - When you need to reference the result multiple times (use CTE)
    - For readability in complex queries

---

**Previous:** [SQL Joins](05_joins.md)