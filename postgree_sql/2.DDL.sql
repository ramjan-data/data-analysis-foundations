--Data definition language(CREATE, ALTER, DROP)

--create a DATABASE
CREATE DATABASE company_1;

--CREATE A SCHEMA
CREATE SCHEMA sales;


--create a table 
CREATE TABLE persons(
	id INT NOT NULL,
	name VARCHAR NOT NULL,
	birth_date DATE,
	phone VARCHAR(15) NOT NULL,
	salary NUMERIC(10,2),
	score INT ,
	CONSTRAINT pk_persons PRIMARY KEY(id)
);

SELECT*FROM persons;


--ALTER
--add a new column "email"
ALTER TABLE persons
ADD COLUMN email VARCHAR(50) NOT NULL;

--rename  column
ALTER TABLE persons
RENAME COLUMN score to performance_score; 

--modify column type
ALTER TABLE persons
ALTER COLUMN salary TYPE DECIMAL(12,2);

--change a column type
ALTER TABLE users
ALTER COLUMN performance_score TYPE INT
USING performance_score::integer;

--rename table
ALTER TABLE persons RENAME TO staff;
ALTER TABLE staff RENAME TO persons;

--set not null 
ALTER TABLE persons
ALTER COLUMN salary SET NOT NULL;



--DROP(delete objects permanently)
--delete table
DROP TABLE persons;

--drop database
DROP DATABASE company;

--drop index
DROP INDEX idx_name;

--drop column "phone" from the table
ALTER TABLE persons
DROP COLUMN phone; 

--TRUNCATE(delete rows, while having structure)
TRUNCATE TABLE persons;


--COMMENT
COMMENT ON TABLE persons IS 'stores employee information';
COMMENT ON COLUMN persons.salary IS 'employees mothly salary';

SELECT * FROM persons;














