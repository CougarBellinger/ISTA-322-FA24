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



[[DE-SQL-DML.pdf]]

