# SQL

- It is a language used with the Databases and Database Management Systems, like for how computer it is binary(which can be understood by computers)

# Types of SQL commands

## DDL - Data Definition Language

- Data Definition Language is used to specify the structure i.e. schema of a relational database. DDL provides commands for creation, modification and deletion of various database objects like tables, views, stored procedures, indexes, constraints etc. The output of DDL is placed in data dictionary which contains metadata i.e. data about data.

### CREATE

- Used for creating an object(tables, view, indexes, etc,.).

### ALTER

- Used for modifying the object(tables, view, indexes, etc,.).

### DROP

- Used to delete the object.

### TRUNCATE

- Used to delete all the rows from the table.

## DML - Data Manipulation Language

- Data Manipulation Language enables users to access or manipulate data in a relational database. DML provides commands for retrieval, creation, deletion and modification of information in a database. DML requires a user to specify what data is needed without specifying how to get it. The database engine is left to figure out effective means of retrieving data.

### INSERT

- Used to insert the data in a table.

### UPDATE

- Used to update any entry in a table of a row

### DELETE

- Used to delete an row entry in the table.

### SELECT

- Retrive data from tables.

## DCL - Data Control Language

- Data Control Language enables users to provide access to various database objects like views, tables, stored procedures etc. in a relational database. Typically only DBAs have access to grant and revoke privileges. Whenever a user submits a query, the database checks against the granted privileges and rejects the query if it is not authorized.

### GRANT

- Provide access rights on Database.

### REVOKE

- Withdraw access rights on Database.

## Transactional Control Language

- Transaction Control Language specifies commands for beginning and ending a transaction. A transaction consists of a sequence of SQL statements that are applied in an atomic (all or none) manner. A commit makes all the changes applied by the transaction permanent on the database while a rollback undoes all the changed applied by the transaction.

### COMMIT

- Save database changes and end transaction.

### ROLLBACK

- Undo changes that are not commited and end transaction.