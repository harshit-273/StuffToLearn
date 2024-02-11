# `CREATE`

- It is used to create database, tables, views, etc,.

### Syntax

```sql
CREATE TABLE Table_name (
	column1 DATATYPE1,
	column2 DATATYPE2
);
```

## `CONSTRAINT`

- It is something which can be used to restrict the column values to few specific values or apply few condition to write them into the database.
- They can be column level or table level.
- Composite constraints can only be applied at table level.
- It is not necessary to give names to all the constraints, but it would come in handy in case the constraint needs to be removed in the future.

### `NOT NULL`
- The column having this as constraint can not have `NULL` values.
- It can only be applied on the column level constraints.

### `UNIQUE`

- The column having this as constraint can not have any rows having same entry.

```
Note:
Anything that is `NULL`, can be `UNIQUE`
```

### `PRIMARY KEY`
- It is something used to uniquely identify the entire row.
- This can not be `NULL` or `UNIQUE`.

### `CHECK`
- Used to check specific type of constraint _e.g.,_ age restriction for 18 years, date of birth is not future date, _etc,._

### `DEFAULT`
- Not a constraint. It is used to specify the default value, in case we are not passing any values to it.

### `REFERENCES`
- Used when we want use the values on present in a different table column and not out of it.

### Example with constraints

```sql
CREATE TABLE Student (
	StudentId INTEGER CONSTRAINT stud_sid_pk PRIMARY KEY,
	FirstName VARCHAR2(10) CONSTRAINT stud_fname_nn NOT NULL,
	LastName VARCHAR2(10) NOT NULL,
	Gender CHAR(1) CONSTRAINT stud_gender_ck CHECK(Gender IN ('M', 'F')),
	DOJ DATE DEFAULT SYSDATE, /* Here SYSDATE would take up the current date */
	ContactNo NUMBER(10) UNIQUE,
	PersonId INTEGER CONSTRAINT stud_pid_fk REFERENCES Person(PersonId), /* We are assuming that "Person" table already exists. */
	CONSTRAINT stud_name_ck CHECK(FirstName <> LastName) /* Composite constraint */
);
```

### Example with constraints

```sql
CREATE TABLE Student (
	StudentId INTEGER, 
	FirstName VARCHAR2(10) CONSTRAINT stud_fname_nn NOT NULL,
	LastName VARCHAR2(10) NOT NULL,
	Gender CHAR(1),
	DOJ DATE DEFAULT SYSDATE,
	ContactNo NUMBER(10) ,
	PersonId INTEGER,
	CONSTRAINT stud_sid_pk PRIMARY KEY(StudentId),
	CONSTRAINT stud_gender_ck CHECK(Gender IN ('M', 'F')),
	CONSTRAINT stud_name_ck CHECK(FirstName <> LastName),
	UNIQUE(ContactNo),
	CONSTRAINT stud_pid_fk REFERENCES Person(PersonId)
);
```

# `DROP`

- It is used to delete the table.

### Syntax

```sql
DROP TABLE Tablename;
```

```
Note:
Any parent table(the one from which the column is referenced) can not be dropped before dropping the child table(the one which references the column from the other table).
```

### Syntax to resolve issues with the references with primary or unique constraints

```sql
DROP TABLE Tablename CASCADE CONSTRAINTS;
```

