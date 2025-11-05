/* 

SQL Common Table Expressions (CTEs)

   Table of Contents:
     1. NON-RECURSIVE CTE
	 		a.Standalone CTE
			b.Nested CTE
     2. RECURSIVE CTE | GENERATE SEQUENCE
     3. RECURSIVE CTE | BUILD HIERARCHY
	 
*/

--NON-RECURSIVE CTE
-- Step1: Find the total Sales Per Customer (Standalone CTE)
WITH CTE_total_sales AS(
SELECT 
	customerid,
	SUM(sales) AS total_sales
FROM sales.orders
GROUP BY customerid
)
-- Step2: Find the last order date for each customer (Standalone CTE)
, CTE_last_orderdate AS
(
SELECT
	customerid,
	MAX(orderdate) AS last_orderdate
FROM sales.orders
GROUP BY customerid	
)
-- Step3: Rank Customers based on Total Sales Per Customer (Nested CTE)
, CTE_customer_rank AS
(
SELECT 
	customerid,
	RANK() OVER(ORDER BY total_sales DESC) AS customer_rank
FROM CTE_total_sales	
)
-- Step4: segment customers based on their total sales (Nested CTE)
, CTE_customer_segment AS
(
SELECT 
	customerid,
	CASE
		WHEN total_sales>100 THEN 'high'
		WHEN total_sales>50 THEN 'median'
		ELSE 'low'
END customer_segment
FROM CTE_total_sales
)
--Main query
SELECT 
	c.customerid,
	c.firstname,
	c.lastname,
	cts.total_sales,
	clo.last_orderdate,
	ccr.customer_rank,
	ccs.customer_segment
FROM sales.customers AS c
LEFT JOIN CTE_total_sales AS cts
ON cts.customerid=c.customerid
LEFT JOIN CTE_last_orderdate AS clo
ON clo.customerid=c.customerid
LEFT JOIN CTE_customer_rank AS ccr
ON ccr.customerid=c.customerid
LEFT JOIN CTE_customer_segment AS ccs
ON ccs.customerid=c.customerid




--RECURSIVE CTE | GENERATE SEQUENCE
--Generate a sequence of numbers from 1 to 20.

WITH RECURSIVE Series AS (
    -- Anchor Query
    SELECT 1 AS MyNumber
    UNION ALL
    -- Recursive Query
    SELECT MyNumber + 1
    FROM Series
    WHERE MyNumber < 20
)
-- Main Query
SELECT *
FROM Series


--Generate a sequence of numbers from 1 to 1000.
WITH RECURSIVE Series AS
(
    -- Anchor Query
    SELECT 1 AS MyNumber
    UNION ALL
    -- Recursive Query
    SELECT MyNumber + 1
    FROM Series
    WHERE MyNumber < 1000
)
-- Main Query
SELECT *
FROM Series




--RECURSIVE CTE | BUILD HIERARCHY
/* 
   Build the employee hierarchy by displaying each employee's level within the organization.
   - Anchor Query: Select employees with no manager.
   - Recursive Query: Select subordinates and increment the level.
*/

WITH RECURSIVE CTE_Emp_Hierarchy AS
(
    -- Anchor Query: Top-level employees (no manager)
    SELECT
        EmployeeID,
        FirstName,
        ManagerID,
        1 AS Level
    FROM Sales.Employees
    WHERE ManagerID IS NULL
    UNION ALL
    -- Recursive Query: Get subordinate employees and increment level
    SELECT
        e.EmployeeID,
        e.FirstName,
        e.ManagerID,
        Level + 1
    FROM Sales.Employees AS e
    INNER JOIN CTE_Emp_Hierarchy AS ceh
        ON e.ManagerID = ceh.EmployeeID
)
-- Main Query
SELECT *
FROM CTE_Emp_Hierarchy;

