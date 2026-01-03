 /* SQL VIEWS

   Table of Contents:
     1. Create, Drop, Modify View
     2. USE CASE - HIDE COMPLEXITY
     3. USE CASE - DATA SECURITY
*/

--find the running total of sales for each month

--using CTEs

WITH monthly_summery AS(
SELECT 
	DATE_TRUNC('month', orderdate) ordermonth,
	SUM(sales) total_sales
FROM sales.orders	
GROUP BY DATE_TRUNC('month', orderdate)
)
SELECT 
	ordermonth,
	total_sales,
	SUM(total_sales) OVER(ORDER BY ordermonth)
FROM monthly_summery




--Using VIEW

CREATE VIEW sales.V_monthly_summery AS(
SELECT 
	DATE_TRUNC('month', orderdate) ordermonth,
	SUM(sales) total_sales,
	COUNT(orderid) AS total_order,
	SUM(quantity) total_quantities
FROM sales.orders	
GROUP BY DATE_TRUNC('month', orderdate)
)

--running total of sales
SELECT 
	ordermonth,
	total_sales,
	SUM(total_sales) OVER(ORDER BY ordermonth) running_total
FROM sales.V_monthly_summery

--to delete the view
DROP VIEW sales.V_monthly_summery




--USE CASE | HIDE COMPLEXITY
--provide a view that combines details from orders,products,customer and employees Table

CREATE VIEW sales.order_details AS(
SELECT 
	o.orderid,
	o.orderdate,
	p.product,
	p.category,	
	CONCAT(c.firstname,' ',c.lastname) customer_name,
	country AS customer_country,
	CONCAT(e.firstname,' ',e.lastname) employee_name,
	e.department,
	o.sales,
	o.quantity	
FROM sales.orders AS o
LEFT JOIN sales.products p
ON p.productid=o.productid
LEFT JOIN sales.customers c
ON c.customerid=o.customerid
LEFT JOIN sales.employees e
ON e.employeeid=o.salesPersonID
)


SELECT orderid,sales,employee_name,customer_name, department,category
FROM sales.order_details




--USE CASE| Data security
/*provide a view for the EU sales team that combines details from all tables
and excludes data related to the USA */

CREATE VIEW sales.order_detais_EU AS(
SELECT 
	o.orderid,
	o.orderdate,
	p.product,
	p.category,	
	CONCAT(c.firstname,' ',c.lastname) customer_name,
	country AS customer_country,
	CONCAT(e.firstname,' ',e.lastname) employee_name,
	e.department,
	o.sales,
	o.quantity	
FROM sales.orders AS o
LEFT JOIN sales.products p
ON p.productid=o.productid
LEFT JOIN sales.customers c
ON c.customerid=o.customerid
LEFT JOIN sales.employees e
ON e.employeeid=o.salesPersonID
WHERE c.country != 'USA'
)




--USE CASE | Flexibily and Dynamic
--USE CASE | Multiple language
--USE CASE | Virtual data marts in DWH






				