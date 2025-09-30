### Data Definition Language
> [[DE-SQL-DDL.pdf]]
#### Definition:
- Category of SQL commands
- Used to **define**, **modify**, and **remove** the structure of database objects
- Statements specify how data is stored, organized, and related within the database
	- They don't manipulate the actual data within the tables
#### Foreign Keys and Referential Integrity:
- A **foreign key** is a column (or a set of columns) in one table that creates a link between data in two tables. 
- It acts as a reference to the **primary key** in another table, ensuring that relationships between records remain consistent
- Data Engineering importance:
	- Enforces **referential integrity**
	- Introduces **performance trade-offs**
	- In large databases, relationships may be enforced through **ETL processes or application code** to improve scalability and flexibility
#### Altering Tables (DE perspective):
- Allows **schema evolution** without recreating the entire database
- Adding columns with constraints (eg. UNIQUE or NOT NULL) helps enforce data quality
- Changes on large tables can be **expensive**, as the database may need to rewrite data or rebuild indexes
- For production systems, **migration scripts** manage schema changes and version control
#### Dropping and Truncating Tables (DE perspective):
- `TRUNCATE` cannot be rolled back in some databases systems unless wrapped in a transaction
- `TRUNCATE` used when reloading staging tables during ETL processes
- `DROP` used when a table is no longer needed
#### Database Schema:
- **Blueprint** or **Map** of a database (tables and relations)
- Shows how data is organized, tables, columns, datatypes of columns, and how tables are related through keys
- No data, just the design
- Shared common understanding of data structure
#### Key Components of a Schema:
- **Tables**: The main entities
- **Columns**: The attributes of each table
- **Data Types**: Define what kind of data each column can hold
- **Primary Keys**: Unique id for rows in a table
- **Foreign Keys**: References to primary keys in other tables, creating links between them
- **Relationships**: The logical connections between tables (represented as lines in a schema diagram)
#### How to Read the Schema Diagram:
- Rectangles = tables
- Column names and data types are inside respective rectangle
- Primary Key is underlined or marked with a key symbol
- Arrows between tables show foreign key relationships

> Example of schema for the university database

![[Pasted image 20250929193218.png]]


### Data Manipulation Language
> [[DE-SQL-DML.pdf]]
#### Definition:
- Part of SQL that deals with managing the data inside tables
- **Add**, **Change**, and **Remove** information
- Common Commands:
	- `INSERT INTO`: Add new rows to a table
	- `UPDATE`: Change data in existing rows
	- `DELETE FROM`: Remove rows from tables
#### Inserting Data:
- If you omit a column in the `INSERT`, it must either have a default value or allow NULL
- Database will reject non-unique primary keys
- Foreign Key constraints ensure data validity
#### Updating Data:
```SQL
UPDATE enrolled
SET grade = 4.0
WHERE sId = 2 AND cId = 394;
```
#### Deleting Data:
```SQL
DELETE FROM student
WHERE sId = 2;
```
- This removes Bob from the student table
- **Caution**:
	- If Bob is enrolled in course, the **foreign key** constraint may prevent deletion
	- Databases can use `ON DELETE CASCADE`
		- `ON DELETE CASCADE`: removes related elements
	- Without a `WHERE` clause, `DELETE FROM student;` would remove *all students*

> ### Risks of UPDATE or DELETE without a WHERE clause:
>**Important: Always use a `WHERE` clause!**
	- Without `WHERE` clause, database would update *every row* in the table

#### Security Risks and Protection:
- **Data Loss**:
	- without a `WHERE` clause, and entire table of data can be corrupted or deleted
- **Privilege Management**:
	- Production databases often restrict `UPDATE` and `DELETE` permissions to admins or specific roles
- **Safe mode in tools**:
	- Many SQL management tools include settings to warn or block queries that affect all rows
- **Transactions**:
	- Wrapping updates and deletes inside a transaction allows you to `ROLLBACK` if the command affects more rows than expected
- **Row Count Checks**:
	- Good practice is to check how many rows will be updated/deleted using a `SELECT` first:
```SQL
		SELECT COUNT(*) FROM enrolled WHERE grade < 2.0;
```
		and then apply the DELETE or UPDATE with the same WHERE clause
- **Audit Logging**:
	- Some databases log every change to critical tables, allowing admins to detect or revert unintended mass updates/deletes

#### Best Practice for Engineers:
Always:
1. Write the `UPDATE/DELETE` with the `WHERE` clause
2. Run a `SELECT` with the same condition to preview the selected rows
3. Use transactions so mistakes can be rolled back safely