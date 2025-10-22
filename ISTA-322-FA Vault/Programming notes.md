
## Aggregating
---
#### `.groupby` in pandas:
``` python
(baby                # the dataframe
 .groupby('Year')    # column(s) to group
 ['Count']           # column(s) to aggregate
 .sum()              # how to aggregate
)
```
#### `.agg` in pandas:
```python
(baby
.groupby('Year')
.agg({'Count':['sum']}) # keys = column name; value = agg function(s) to apply
)
```
## SQL
---
### General Syntax:
```SQL
SELECT column1, column2, ... 
FROM table_name 
[WHERE condition] 
[GROUP BY column_list] 
[HAVING group_condition] 
[ORDER BY column [ASC|DESC]] 
[LIMIT number] 
```
### Selecting Columns and Filtering Rows:

> Select names and salary of employees older than 30
#### `Pandas`:
```python
employees[['name', 'salary']][employees['age'] > 30]
```
#### `SQL`:
```SQL
SELECT name, salary
FROM employees
WHERE age > 30;
```
### Sorting:

> Sort employees based on salary in descending order
#### `Pandas`:
```Python
employees.sort_values('salary', ascending=False)
```
#### `SQL`:
```SQL
SELECT *
FROM employees
ORDER BY salary DESC;
```
### Aggregation and GROUP BY:

> Aggregate the sum of salary, grouping by department
#### `Pandas`:
```Python
employee.groupby('department_id')['salary'].sum()
```
	#### `SQL`:
``` SQL
SELECT department_id, SUM(salary) as total_salary
FROM employee
GROUP BY department_id;
```
### Filtering After Aggregation (HAVING):

> Filter salary based on comparison (after aggregation)

#### `Pandas`:
```Python
total_salary =
employee.groupby('department_id')['salary'].sum()
total_salary[total_salary['salary'] > 150000]
```
#### `SQL`:
``` SQL
SELECT department_id, SUM(salary) as total_salary
FROM employee
GROUP BY department_id
HAVING SUM(salary) > 150000;
```
### Multiple Aggregations:

> Perform multiple aggregations, using multiple variables

#### `Pandas`:
```Python
employee.groupby('department_id').agg({'salary': ['mean', 'max', 'min']})
```
#### `SQL`:
```SQL
SELECT department_id, AVG(salary) AS avg_salary, MAX(salary)
AS max_salary, MIN(salary) AS min_salary
FROM employees
GROUP BY department_id;
```
### Joining Tables:

> Join multiple tables, using keys to index the join

#### `Pandas`:
```Python
pd.merge(employee, department, on='dept_id', how='inner')
```
#### `SQL`:
```SQL
SELECT e.*, d.department_name
FROM employee e
JOIN department d
ON e.department_id = d.department_id;
```

### Filtering on Joined Data:

> Filter after joining data

#### `Pandas`:
```Python
merged = pd.merge(employee, department, on='department_id')
merged[(merged['department_name'] == 'Engineering') &
(merged['salary'] > 80000)]
```
#### `SQL`:
```SQL
SELECT e.first_name, e.last_name, e.salary, d.department_name
FROM employee e
JOIN department d ON e.department_id = d.department_id
WHERE d.department_name = 'Engineering' AND e.salary > 80000;
```
### Calculated Columns:

> Performing calculations on specific columns

#### `Pandas`:
```Python
employee['annual_bonus'] = employees['salary'] * 0.10
```
#### `SQL`:
```SQL
SELECT first_name, last_name,
	salary, salary * 0.10 AS annual_bonus
FROM employee;
```
### Subqueries (Nested Queries)

> Self explanatory...

#### `Pandas`:
```Python
avg_salary = employee['salary'].mean()
employee[employee['salary'] > avg_salary]
```
#### `SQL`:
```SQL
SELECT *
FROM employee
WHERE salary > (
	SELECT AVG(salary) FROM employee
);
```

### IN, NOT IN, and EXISTS:

> Discrete filtering

#### `Pandas`:
```Python
exclude_depts = department[(department['department_name'] == 'HR') | (department['department)name'] == 'Marketing')]['deparment_id']
employee[~employee['department_id'].isin(exclude_depts)]
```
#### `SQL`:
```SQL
SELECT *
FROM employees
WHERE department_is NOT IN (SELECT department_id
	FROM department
	WHERE department_name = 'HR' OR department_name = 'Marketing');
```
### Null Values and Missing Data:

>Null filtering

#### `Pandas`:
```Python
employee[employee['salary'].isnull()]
employee[employee['salary'].notnull()]
```
#### `SQL`:
```SQL
SELECT * FROM employees WHERE salary IS NULL;
SELECT * FROM employees WHERE salary IS NOT NULL;
```
### Strings in SQL:
`%s` as a placeholder operator that allows you to pass a specified value into a string. 
You specify what value you want to place there by using `%` and then what you want to insert. 
Here's a simple example:
```Python
>>> print('hello my name is %s' % 'dan')
hello my name is dan
```

## Data Definition Language (SQL)
### Creating a Database:
- `CREATE DATABASE`: creates a new database
- `IF NOT EXISTS`: prevents an error if it already exists
##### Example:
``` SQL
CREATE DATABASE IF NOT EXISTS university;
```
### Switching to the Database:
> Once our database exists, we need to tell the SQL server to use it for our next actions. Otherwise, we might accidentally create tables somewhere else! Note that when we use python connection, we identify the database name that we are working with to get the connection.

- The `USE` command tells SQL which database we're working with
##### Example:
```SQL
USE university
```
### Creating Tables:
##### Student Table:
```SQL
CREATE TABLE IF NOT EXISTS student (
	sId INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);
```
- `PRIMARY KEY` makes each ID unique
- `VARCHAR(255) NOT NULL` allows for 255 characters and no blanks allowed
##### Course Table:
```SQL
CREATE TABLE IF NOT EXISTS course (
	cId INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);
```
##### Enrolled Table:
```SQL
CREATE TABLE IF NOT EXISTS enrolled (
	sId INT,
	cId INT,
	grade FLOAT,
	PRIMARY KEY (sId, cId),
	FOREIGN KEY (sId) REFERENCES student(sId),
	FOREIGN KEY (cId) REFERENCES course(cId)
);
```

- `PRIMARY KEY (sId, cId)`: Creates a **Composite Key** which is a unique combination of columns
	- student ID and course ID in this case
- `FOREIGN KEY (sId) REFERENCES student(sId)`: Only allows enrollment for students that exist in the student table. (same for courseId)

### Altering Tables:
```SQL
ALTER TABLE student ADD COLUMN email VARCHAR(255) UNIQUE;
```
- Adds an `email` column to the student table
```SQL
ALTER TABLE student DROP COLUMN email;
```
- Removes the `email` column from the table (data permanently lost)
### Dropping and Truncating Tables:
```SQL
DROP TABLE enrolled;
```
- `DROP` deletes both table definition and its data permanently
```SQL
TRUNCATE TABLE enrolled;
```
- `TRUNCATE` deletes data but keeps definition

## Data Manipulation Language (SQL)

### Schema Setup:
```SQL
CREATE TABLE student (
	sId INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);

CREATE TABLE course (
	cId INT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
);

CREATE TABLE enrolled (
	sId INT,
	cId INT,
	grade FLOAT,
	PRIMARY KEY (sId, cId),
	FOREIGN KEY (sId) REFERENCES student (sId),
	FOREIGN KEY (cId) REFERENCES course (cId)
);
```
![[Pasted image 20250929193218.png]]
### Inserting Data:
- `INSERT INTO`: Adds rows to a table
##### Using tuples to insert DF data:
```python
#load data
data_tups = [tuple(x) for x in judge_df.to_numpy()]

insert_query = '''
INSERT INTO casedb_judge(judge_id, judge_name, party_name, gender_name, race_name) 
VALUES (%s, %s, %s, %s, %s);
'''

conn, cur = get_conn_cur()
cur.executemany(insert_query, data_tups)
conn.commit() # commit
cur.close() # close
conn.close() # close
```
##### Adding Students:
```SQL
INSERT INTO student ( sId , name ) VALUES (1 , ’ Alice ’);
INSERT INTO student ( sId , name ) VALUES (2 , ’ Bob ’);
INSERT INTO student ( sId , name ) VALUES (3 , ’ Sara ’);
```
##### Adding Courses:
```SQL
INSERT INTO course ( cId , name ) VALUES (480 , ’ Database Systems ’);
INSERT INTO course ( cId , name ) VALUES (394 , ’ Data Engineering ’);
```
##### Enrolling Students in Courses:
```SQL
INSERT INTO enrolled ( sId , cId , grade ) VALUES (1 , 480 , 0);
INSERT INTO enrolled ( sId , cId , grade ) VALUES (2 , 394 , 0);
INSERT INTO enrolled ( sId , cId , grade ) VALUES (1 , 394 , 0);
```

### Updating Data:
> Sets Bob's grade in Data Engineering to `4.0`
```SQL
UPDATE enrolled
SET grade = 4.0
WHERE sId = 2 AND cId = 394;
```
### Deleting Data:
> Removes Bob from the student table
```SQL
DELETE FROM student
WHERE sId = 2;
```
- If Bob is still enrolled in any courses, the foreign key constraint may prevent deletion.
- Databases can be set to `ON DELETE CASCADE`, which automatically removes related enrollments, or you must manually delete from enrolled first.
- Without a `WHERE` clause, `DELETE FROM student;` would remove all students.
