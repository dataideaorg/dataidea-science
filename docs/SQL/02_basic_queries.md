# Basic SQL Queries

Learn the fundamental SQL commands to retrieve and filter data from databases.

## The SELECT Statement

The `SELECT` statement is used to retrieve data from a database. It's the most commonly used SQL command.

### Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

### Example Dataset

Throughout this tutorial, we'll use a `students` table:

```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 2  | Bob       | 22  | B     | LA    |
| 3  | Charlie   | 21  | A     | NYC   |
| 4  | Diana     | 23  | C     | Chicago|
| 5  | Eva       | 20  | B     | LA    |
+----+-----------+-----+-------+-------+
```

## Selecting Specific Columns

### Select One Column

```sql
SELECT name FROM students;
```

**Result:**
```
+-----------+
| name      |
+-----------+
| Alice     |
| Bob       |
| Charlie   |
| Diana     |
| Eva       |
+-----------+
```

### Select Multiple Columns

```sql
SELECT name, age, grade FROM students;
```

**Result:**
```
+-----------+-----+-------+
| name      | age | grade |
+-----------+-----+-------+
| Alice     | 20  | A     |
| Bob       | 22  | B     |
| Charlie   | 21  | A     |
| Diana     | 23  | C     |
| Eva       | 20  | B     |
+-----------+-----+-------+
```

### Select All Columns

```sql
SELECT * FROM students;
```

The `*` (asterisk) selects all columns from the table.

## The WHERE Clause

The `WHERE` clause filters records based on specified conditions.

### Basic Syntax

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Examples

**Filter by exact match:**
```sql
SELECT * FROM students
WHERE grade = 'A';
```

**Result:**
```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 3  | Charlie   | 21  | A     | NYC   |
+----+-----------+-----+-------+-------+
```

**Filter by numeric comparison:**
```sql
SELECT name, age FROM students
WHERE age > 21;
```

**Result:**
```
+-----------+-----+
| name      | age |
+-----------+-----+
| Bob       | 22  |
| Diana     | 23  |
+-----------+-----+
```

## Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal to | `age = 20` |
| `!=` or `<>` | Not equal to | `grade != 'C'` |
| `>` | Greater than | `age > 21` |
| `<` | Less than | `age < 22` |
| `>=` | Greater than or equal | `age >= 21` |
| `<=` | Less than or equal | `age <= 22` |

## Logical Operators

### AND Operator

Both conditions must be true:

```sql
SELECT * FROM students
WHERE grade = 'A' AND city = 'NYC';
```

**Result:**
```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 3  | Charlie   | 21  | A     | NYC   |
+----+-----------+-----+-------+-------+
```

### OR Operator

At least one condition must be true:

```sql
SELECT * FROM students
WHERE city = 'NYC' OR city = 'LA';
```

**Result:**
```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 2  | Bob       | 22  | B     | LA    |
| 3  | Charlie   | 21  | A     | NYC   |
| 5  | Eva       | 20  | B     | LA    |
+----+-----------+-----+-------+-------+
```

### NOT Operator

Negates a condition:

```sql
SELECT * FROM students
WHERE NOT grade = 'C';
```

## ORDER BY Clause

Sort results in ascending or descending order.

### Ascending Order (Default)

```sql
SELECT * FROM students
ORDER BY age;
```

**Result:**
```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 5  | Eva       | 20  | B     | LA    |
| 3  | Charlie   | 21  | A     | NYC   |
| 2  | Bob       | 22  | B     | LA    |
| 4  | Diana     | 23  | C     | Chicago|
+----+-----------+-----+-------+-------+
```

### Descending Order

```sql
SELECT * FROM students
ORDER BY age DESC;
```

### Multiple Columns

```sql
SELECT * FROM students
ORDER BY grade ASC, age DESC;
```

## LIMIT Clause

Restrict the number of rows returned:

```sql
SELECT * FROM students
LIMIT 3;
```

**Result:**
```
+----+-----------+-----+-------+-------+
| id | name      | age | grade | city  |
+----+-----------+-----+-------+-------+
| 1  | Alice     | 20  | A     | NYC   |
| 2  | Bob       | 22  | B     | LA    |
| 3  | Charlie   | 21  | A     | NYC   |
+----+-----------+-----+-------+-------+
```

## DISTINCT Keyword

Remove duplicate values:

```sql
SELECT DISTINCT city FROM students;
```

**Result:**
```
+---------+
| city    |
+---------+
| NYC     |
| LA      |
| Chicago |
+---------+
```

## Practice Exercises

Try these queries on your own:

1. Select all students from NYC
2. Find students aged 20 or 21
3. Get names of students with grade A, sorted alphabetically
4. Find the 2 oldest students
5. List all unique grades in the table

??? success "Solutions"
    ```sql
    -- 1. Students from NYC
    SELECT * FROM students WHERE city = 'NYC';

    -- 2. Students aged 20 or 21
    SELECT * FROM students WHERE age = 20 OR age = 21;

    -- 3. Grade A students, sorted by name
    SELECT name FROM students WHERE grade = 'A' ORDER BY name;

    -- 4. Two oldest students
    SELECT * FROM students ORDER BY age DESC LIMIT 2;

    -- 5. Unique grades
    SELECT DISTINCT grade FROM students;
    ```

!!! tip "SQL is Case-Insensitive"
    SQL keywords are not case-sensitive. `SELECT`, `select`, and `SeLeCt` all work the same. However, it's a good practice to write keywords in UPPERCASE for readability.

---

**Previous:** [Introduction to SQL](01_introduction.md) | **Next:** [Filtering and Pattern Matching](03_filtering.md)