# Aggregate Functions

Learn how to perform calculations on data sets using SQL's powerful aggregate functions.

## What are Aggregate Functions?

Aggregate functions perform calculations on a set of values and return a single value. They're essential for data analysis and reporting.

## Common Aggregate Functions

| Function | Description | Example |
|----------|-------------|---------|
| `COUNT()` | Counts the number of rows | `COUNT(*)` |
| `SUM()` | Calculates the sum of values | `SUM(salary)` |
| `AVG()` | Calculates the average | `AVG(age)` |
| `MAX()` | Returns the maximum value | `MAX(price)` |
| `MIN()` | Returns the minimum value | `MIN(price)` |

## Sample Dataset

We'll use this `employees` table:

```
+----+-----------+-----------+--------+-----+
| id | name      | department| salary | age |
+----+-----------+-----------+--------+-----+
| 1  | Alice     | IT        | 75000  | 28  |
| 2  | Bob       | Sales     | 50000  | 32  |
| 3  | Charlie   | IT        | 80000  | 35  |
| 4  | Diana     | HR        | 60000  | 29  |
| 5  | Eva       | Sales     | 55000  | 26  |
| 6  | Frank     | IT        | 70000  | 31  |
+----+-----------+-----------+--------+-----+
```

## COUNT Function

Counts the number of rows.

### Count All Rows

```sql
SELECT COUNT(*) AS total_employees
FROM employees;
```

**Result:**
```
+------------------+
| total_employees  |
+------------------+
| 6                |
+------------------+
```

### Count Specific Column

```sql
SELECT COUNT(department) AS dept_count
FROM employees;
```

### Count Distinct Values

```sql
SELECT COUNT(DISTINCT department) AS unique_departments
FROM employees;
```

**Result:**
```
+--------------------+
| unique_departments |
+--------------------+
| 3                  |
+--------------------+
```

## SUM Function

Calculates the total sum of a numeric column.

```sql
SELECT SUM(salary) AS total_payroll
FROM employees;
```

**Result:**
```
+---------------+
| total_payroll |
+---------------+
| 390000        |
+---------------+
```

### SUM with WHERE

```sql
SELECT SUM(salary) AS it_payroll
FROM employees
WHERE department = 'IT';
```

**Result:**
```
+-------------+
| it_payroll  |
+-------------+
| 225000      |
+-------------+
```

## AVG Function

Calculates the average value.

```sql
SELECT AVG(salary) AS average_salary
FROM employees;
```

**Result:**
```
+----------------+
| average_salary |
+----------------+
| 65000.00       |
+----------------+
```

### Rounding Averages

```sql
SELECT ROUND(AVG(salary), 2) AS average_salary
FROM employees;
```

## MAX and MIN Functions

Find the highest and lowest values.

### Maximum Value

```sql
SELECT MAX(salary) AS highest_salary
FROM employees;
```

**Result:**
```
+----------------+
| highest_salary |
+----------------+
| 80000          |
+----------------+
```

### Minimum Value

```sql
SELECT MIN(salary) AS lowest_salary
FROM employees;
```

### Multiple Aggregates in One Query

```sql
SELECT
    MAX(salary) AS highest,
    MIN(salary) AS lowest,
    AVG(salary) AS average
FROM employees;
```

**Result:**
```
+---------+--------+----------+
| highest | lowest | average  |
+---------+--------+----------+
| 80000   | 50000  | 65000.00 |
+---------+--------+----------+
```

## GROUP BY Clause

Group rows with the same values and apply aggregate functions to each group.

### Basic GROUP BY

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```

**Result:**
```
+-----------+----------------+
| department| employee_count |
+-----------+----------------+
| IT        | 3              |
| Sales     | 2              |
| HR        | 1              |
+-----------+----------------+
```

### Multiple Aggregates with GROUP BY

```sql
SELECT
    department,
    COUNT(*) AS num_employees,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees
GROUP BY department;
```

**Result:**
```
+-----------+---------------+------------+------------+------------+
| department| num_employees | avg_salary | max_salary | min_salary |
+-----------+---------------+------------+------------+------------+
| IT        | 3             | 75000.00   | 80000      | 70000      |
| Sales     | 2             | 52500.00   | 55000      | 50000      |
| HR        | 1             | 60000.00   | 60000      | 60000      |
+-----------+---------------+------------+------------+------------+
```

### GROUP BY Multiple Columns

```sql
SELECT
    department,
    CASE
        WHEN age < 30 THEN 'Under 30'
        ELSE '30 and over'
    END AS age_group,
    COUNT(*) AS count
FROM employees
GROUP BY department, age_group;
```

## HAVING Clause

Filter groups based on aggregate values (WHERE filters individual rows, HAVING filters groups).

### Basic HAVING

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

**Result:**
```
+-----------+------------+
| department| avg_salary |
+-----------+------------+
| IT        | 75000.00   |
+-----------+------------+
```

### HAVING with COUNT

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;
```

**Result:**
```
+-----------+----------------+
| department| employee_count |
+-----------+----------------+
| IT        | 3              |
| Sales     | 2              |
+-----------+----------------+
```

## WHERE vs HAVING

- **WHERE:** Filters rows BEFORE grouping
- **HAVING:** Filters groups AFTER grouping

```sql
-- Filter individual rows, then group
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE age > 28
GROUP BY department
HAVING AVG(salary) > 65000;
```

## Combining Everything

A comprehensive query using multiple concepts:

```sql
SELECT
    department,
    COUNT(*) AS total_employees,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(age) AS youngest,
    MAX(age) AS oldest
FROM employees
WHERE salary >= 50000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY avg_salary DESC;
```

## Common Patterns

### 1. Find departments with above-average salaries

```sql
SELECT department, AVG(salary) AS dept_avg
FROM employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

### 2. Count employees by age range

```sql
SELECT
    CASE
        WHEN age < 30 THEN '20-29'
        WHEN age < 40 THEN '30-39'
        ELSE '40+'
    END AS age_range,
    COUNT(*) AS count,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY age_range
ORDER BY age_range;
```

### 3. Top N by group

```sql
SELECT department, MAX(salary) AS top_salary
FROM employees
GROUP BY department
ORDER BY top_salary DESC
LIMIT 3;
```

## Practice Exercises

Using this `sales` table:

```
+----+-----------+--------+--------+------------+
| id | product   | region | amount | sale_date  |
+----+-----------+--------+--------+------------+
| 1  | Laptop    | East   | 1200   | 2024-01-15 |
| 2  | Mouse     | West   | 25     | 2024-01-16 |
| 3  | Laptop    | East   | 1200   | 2024-01-17 |
| 4  | Keyboard  | West   | 75     | 2024-01-18 |
| 5  | Monitor   | East   | 300    | 2024-01-19 |
| 6  | Mouse     | East   | 25     | 2024-01-20 |
+----+-----------+--------+--------+------------+
```

Try these queries:

1. Calculate total sales amount
2. Find average sale amount by region
3. Count number of sales per product
4. Find products with more than 1 sale
5. Find regions with total sales over $1000

??? success "Solutions"
    ```sql
    -- 1. Total sales amount
    SELECT SUM(amount) AS total_sales
    FROM sales;

    -- 2. Average sale by region
    SELECT region, AVG(amount) AS avg_sale
    FROM sales
    GROUP BY region;

    -- 3. Sales count per product
    SELECT product, COUNT(*) AS sale_count
    FROM sales
    GROUP BY product
    ORDER BY sale_count DESC;

    -- 4. Products with more than 1 sale
    SELECT product, COUNT(*) AS sale_count
    FROM sales
    GROUP BY product
    HAVING COUNT(*) > 1;

    -- 5. Regions with sales over $1000
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
    HAVING SUM(amount) > 1000;
    ```

!!! tip "Performance Tip"
    Use aggregate functions wisely. On large tables, they can be expensive. Consider using indexes on grouped columns for better performance.

---

**Previous:** [Filtering and Pattern Matching](03_filtering.md) | **Next:** [SQL Joins](05_joins.md)