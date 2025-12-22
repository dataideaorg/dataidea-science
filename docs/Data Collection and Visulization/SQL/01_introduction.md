# Introduction to SQL

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. It's essential for data scientists, analysts, and anyone working with data.

## What is SQL?

SQL is a domain-specific language used to:

- **Query data** from databases
- **Insert, update, and delete** records
- **Create and modify** database structures
- **Control access** to data
- **Manage transactions**

## Why Learn SQL?

- **Universal:** Works across most database systems (MySQL, PostgreSQL, SQL Server, Oracle, SQLite)
- **Essential for Data Science:** Most data is stored in relational databases
- **High Demand:** SQL skills are among the most sought-after in tech jobs
- **Foundation:** Understanding SQL helps you work with modern data tools

## Database Concepts

### What is a Database?

A database is an organized collection of structured data stored electronically. Think of it as a digital filing cabinet where data is organized into:

- **Tables:** Similar to spreadsheets, organized in rows and columns
- **Rows:** Individual records (like a person, product, or transaction)
- **Columns:** Attributes or fields (like name, price, or date)

### Example Database Structure

```
Customers Table:
+----+----------+-------+-------------------+
| id | name     | age   | email             |
+----+----------+-------+-------------------+
| 1  | John Doe | 30    | john@email.com    |
| 2  | Jane Smith| 25   | jane@email.com    |
+----+----------+-------+-------------------+

Orders Table:
+----+-------------+--------+------------+
| id | customer_id | amount | order_date |
+----+-------------+--------+------------+
| 1  | 1           | 150.00 | 2024-01-15 |
| 2  | 2           | 200.00 | 2024-01-16 |
+----+-------------+--------+------------+
```

## Types of SQL Commands

SQL commands are divided into several categories:

### 1. Data Query Language (DQL)
- `SELECT` - Retrieve data from tables

### 2. Data Definition Language (DDL)
- `CREATE` - Create databases, tables, indexes
- `ALTER` - Modify database structure
- `DROP` - Delete databases or tables
- `TRUNCATE` - Remove all records from a table

### 3. Data Manipulation Language (DML)
- `INSERT` - Add new records
- `UPDATE` - Modify existing records
- `DELETE` - Remove records

### 4. Data Control Language (DCL)
- `GRANT` - Give user access privileges
- `REVOKE` - Remove user access privileges

### 5. Transaction Control Language (TCL)
- `COMMIT` - Save changes permanently
- `ROLLBACK` - Undo changes
- `SAVEPOINT` - Set a point to rollback to

## Popular Database Systems

| Database | Description | Use Cases |
|----------|-------------|-----------|
| **MySQL** | Open-source, widely used | Web applications, small to medium businesses |
| **PostgreSQL** | Advanced open-source | Complex queries, data integrity |
| **SQLite** | Lightweight, file-based | Mobile apps, small applications |
| **SQL Server** | Microsoft's enterprise solution | Enterprise applications, Windows environments |
| **Oracle** | Enterprise-grade | Large corporations, mission-critical systems |

## Your First SQL Query

Here's the most basic SQL query - selecting all data from a table:

```sql
SELECT * FROM customers;
```

This query:
- `SELECT` - tells the database you want to retrieve data
- `*` - means "all columns"
- `FROM customers` - specifies the table name

## Setting Up Your Environment

To practice SQL, you can use:

1. **Online SQL Editors:**
   - [SQLFiddle](http://sqlfiddle.com/)
   - [DB Fiddle](https://www.db-fiddle.com/)
   - [SQL Online IDE](https://sqliteonline.com/)

2. **Local Installation:**
   - MySQL Community Server
   - PostgreSQL
   - SQLite (comes with Python)

3. **Cloud Platforms:**
   - Google BigQuery
   - Amazon RDS
   - Azure SQL Database

## Next Steps

In the following tutorials, you'll learn:

1. **Basic Queries** - SELECT, WHERE, ORDER BY
2. **Filtering Data** - AND, OR, IN, BETWEEN
3. **Aggregate Functions** - COUNT, SUM, AVG, MAX, MIN
4. **Joins** - Combining data from multiple tables
5. **Subqueries** - Queries within queries
6. **Database Design** - Creating efficient table structures

!!! tip "Practice Makes Perfect"
    The best way to learn SQL is by writing queries. Try to practice with real datasets and experiment with different commands.

---

**Next Tutorial:** [Basic SQL Queries](02_basic_queries.md)