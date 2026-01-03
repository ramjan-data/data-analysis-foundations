/* 
	SQL Temporary Tables
*/

--CTAS(create table as select)
--create a parmanent  table
CREATE TABLE sales.monthly_summeries AS (
	SELECT 
	DATE_TRUNC('month', orderdate) ordermonth,
	SUM(sales) total_sales,
	COUNT(orderid) AS total_order,
	SUM(quantity) total_quantities
FROM sales.orders	
GROUP BY DATE_TRUNC('month', orderdate)		
)

--DROP table
DROP TABLE sales.monthly_summeries;





--Temporary table
CREATE TEMP TABLE orders AS (
SELECT * 
FROM sales.orders
)

/*we can insert data using
	INSERT INTO table_name(columns name...)
		VALUES(...)

like normal table */


--Query temp table
SELECT * FROM orders


--Drop table manually
DROP TABLE orders

