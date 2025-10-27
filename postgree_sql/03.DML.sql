--data manipulation language
--DML(insert,update,delete)

--insert data into orders
INSERT INTO orders(order_id, customer_id, sales)
		VALUES(1005, 3, 45)

--insert data from one table to another
--if both has same column then...
INSERT INTO customers SELECT* FROM orders;

--if it shared some same kinda columns
INSERT INTO persons(id, name, phone,salary, email)
SELECT employeeid,firstname, 'unknown',salary,'unknown'  FROM sales.employees;



--UPDATE(always use WHERE to avoid updating all rows)
--change the scores of employee 6 to 0
UPDATE orders
SET sales=0
WHERE order_id=1005;

--change the customerid and orderdate of order_id 1005
UPDATE orders
SET customer_id=2,
	order_date='2021-09-23'
WHERE order_id=1005;

--change all customers with customer_id 2 ,sales 50
UPDATE orders
SET sales=50
WHERE customer_id=2;



--DELETE(always use where to avoid deleting all data)
DELETE FROM orders
WHERE order_id=1005;

--delete all data from table(use truncate )
TRUNCATE TABLE crimson;
