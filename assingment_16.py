# ANS = 1
"""
A database is an organized collection of structured information, or data,
typically stored electronically in a computer system. 

________ Deffrence between SQL and NOSQL________
SQL is the programming language used to interface with relational databases. 
(Relational databases model data as records in rows and tables with logical links between them). 
NoSQL is a class of DBMs that are non-relational and generally do not use SQL.
"""
# ANS = 2

""""
DDL stands for Data Definition Language. 
It is a subset of SQL (Structured Query Language) that is used to define and manipulate the 
structure of a database, including tables, indexes, and constraints.
CREATE:
This command used for creat new table 
CREATE TABLE employees (
  name VARCHAR(50),
  age INT,
  salary DECIMAL(10,2)
);
DROP: This command is used to delete a table or other database object.
DROP TABLE student;

ALTER: This command is used to modify the structure of an existing table
ALTER TABLE employees ADD COLUMN department VARCHAR(50);

TRUNCATE: This command is used to delete all the data from a table, 
but keep the table structure intact.

TRUNCATE TABLE employees;
"""

# ANS = 3

""""
DML stands for Data Manipulation Language,
which is a subset of SQL used to manipulate data stored in a database.
INSERT: This command is used to insert new data into a table.
ex.
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

UPDATE: This command is used to modify existing data in a table
ex.
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
DELETE: This command is used to delete data from a table.
DELETE FROM table_name
WHERE condition;
"""
# ANS = 4
""""
DQL stands for Data Query Language, which is a subset of SQL 
(Structured Query Language) used for querying and retrieving data from a database.

SELECT first_name, last_name, salary
FROM employees
WHERE department = 'sales' AND salary > 50000;

"""
# ANS = 5
""""
A primary key is a column or set of columns in a database table that uniquely 
identifies each row in the table. It is a special type of constraint that ensures 
data integrity by guaranteeing that no two rows can have the same values for the primary
key columns. Typically, primary keys are used as the basis for relationships between tables,
allowing other tables to reference them using foreign keys.


A foreign key is a column or set of columns in a table that refers to the 
primary key of another table. It is used to establish a relationship between
two tables, where the foreign key column in one table is used to identify the
corresponding row in the referenced table. This relationship allows users to link 
data between tables, 
enabling queries to retrieve information from multiple tables in a single operation.
"""

