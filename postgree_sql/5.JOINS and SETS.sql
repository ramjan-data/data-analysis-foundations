--Combining DATA(JOINS, SET)


--JOINS
--No joins
SELECT *FROM customers;
SELECT* FROM orders;

--INNER JOIN(only the matches columns)
--get all customers along with their orders,but only for customers who placed an order
SELECT id,first_name,order_id, sales 
FROM customers
INNER JOIN orders
ON id=customer_id;

--if we got same columns name in both table we will have some issue ,in that case--
SELECT customers.id,
	   customers.first_name,
	   orders.order_id, 
	   orders.sales 
FROM customers
INNER JOIN orders
ON customers.id=orders.customer_id;

SELECT c.id,
	   c.name,
	   o.order_id, 
	   o.sales 
FROM customers AS c
INNER JOIN orders AS o
ON c.id=o.customer_id;


--LEFT JOIN(returns all rows from left table and only matching from right)
--get all customers along with their orders, including those without orders.
SELECT c.id,
	   c.first_name,
	   o.order_id, 
	   o.sales 
FROM customers AS c  --all data from cutomers(left)
LEFT JOIN orders AS o
ON c.id=o.customer_id;


--RIGHT JOIN(returns all rows from right table and only matching from left)
--get all customers with their orders, including order without matching customers
SELECT c.id,
	   c.first_name,
	   o.order_id, 
	   o.sales 
FROM customers AS c  
RIGHT JOIN orders AS o  --all data from orders(right)
ON c.id=o.customer_id;
--retrives the same result with left join
SELECT c.id,
	   c.first_name,
	   o.order_id, 
	   o.sales 
FROM  orders AS o   --LEFT TABLE
LEFT JOIN customers AS c  --RIGHT TABLE
ON c.id=o.customer_id;


--FULL JOIN(returns all rows from both tables)
--get all customers and all orders,even if there is no match
SELECT c.id,
	   c.first_name,
	   o.order_id, 
	   o.sales 
FROM  customers AS c   
FULL JOIN orders AS o
ON c.id=o.customer_id;

--ADVANCED JOINS
--LEFT ANTI JOIN(returns row from the left table that has no matching in right)
--get all customers who haven't placed any order
SELECT *
FROM customers
LEFT JOIN orders
ON id=customer_id
WHERE customer_id IS NULL;

--RIGHT ANTI JOIN
--get all orders without matching customers
SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
ON c.id=o.customer_id
WHERE c.id IS NULL;

--FULL ANTI JOIN(only unmatching data--opposite of inner join)
SELECT * FROM 
customers AS c
FULL JOIN orders AS o
ON c.id=o.customer_id
WHERE c.id IS NULL OR o.customer_id IS NULL


--CROSS JOIN(all possible combinations)
SELECT * FROM  customers
CROSS JOIN orders;

--we can join multiple table by joins
SELECT  c.customerid,
		c.firstname,
		e.salary,
		o.orderid,
		o.orderstatus
FROM sales.customers AS c
LEFT JOIN sales.employees AS e
ON c.customerid=e.employeeid
LEFT JOIN sales.orders AS o
ON c.customerid=o.customerid;



--SET OPERATORS(to join rows)
--UNION(returns all, without duplicates)
--UNION ALL(returns all,including duplicates)
SELECT 
	customerid ,
	firstname AS Name
FROM sales.customers
UNION
SELECT 
	employeeid,
	firstname
FROM sales.employees
ORDER BY customerid ASC;	

--EXCEPT(minus):returns unique rows from 1st table that are not in 2nd table
SELECT 
	customerid ,
	firstname AS first_name
FROM sales.customers
EXCEPT
SELECT 
	employeeid,
	firstname
FROM sales.employees
ORDER BY customerid ASC;

--INTERSECT:returns only rows that are common in both queries
SELECT 
	customerid ,
	firstname AS first_name
FROM sales.customers
INTERSECT
SELECT 
	employeeid,
	firstname
FROM sales.employees
ORDER BY customerid  ASC;

