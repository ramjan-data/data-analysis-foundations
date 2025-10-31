/* STARTING OF ADVANCED SQL TECHNIQUES 

SQL Subquery Functions 

     Table of Contents:
     1.RESULT TYPES
     2.FROM CLAUSE
     3.SELECT
     4.JOIN CLAUSE
     5.COMPARISON OPERATORS 
     6.IN OPERATOR
     7.ANY OPERATOR
     8.CORRELATED 
     9.EXISTS OPERATOR
*/

--to see matadata
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
SELECT DISTINCT TABLE_NAME FROM INFORMATION_SCHEMA.COLUMNS


--SUBQUERY | RESULT TYPES
--Scalar Query 
SELECT
    AVG(Sales)
FROM Sales.Orders;

--Row Query 
SELECT
    CustomerID
FROM Sales.Orders;

--Table Query 
SELECT
    OrderID,
    OrderDate
FROM Sales.Orders;


--SUBQUERY | FROM CLAUSE
--Find the products that have a price higher than the average price of all products.

-- Main Query
SELECT
*
FROM (
    -- Subquery
    SELECT
        ProductID,
        Price,
        AVG(Price) OVER () AS AvgPrice
    FROM Sales.Products
)
WHERE Price > AvgPrice;


--Rank Customers based on their total amount of sales.
SELECT *,
RANK() OVER(ORDER BY total_sales DESC) ranking
FROM(
	SELECT customerid,
	SUM(sales) AS total_sales
	FROM sales.orders
	GROUP BY customerid
)



--SUBQUERY | SELECT (only one single value can come from subquery)
--Show the product IDs, product names, prices, and the total number of orders.
SELECT
    productid,
    product,
    price,
    (SELECT COUNT(*) FROM sales.orders) AS TotalOrders -- Subquery
FROM sales.products;



--SUBQUERY | JOIN CLAUSE
--Show customer details along with their total sales.

-- Main Query
SELECT
    c.*,
    t.TotalSales
FROM Sales.Customers AS c
LEFT JOIN ( 
    -- Subquery
    SELECT
        CustomerID,
        SUM(Sales) AS TotalSales
    FROM Sales.Orders
    GROUP BY CustomerID
) AS t
    ON c.CustomerID = t.CustomerID;



--Show all customer details and the total orders of each customer.

-- Main Query
SELECT
    c.*,
    o.TotalOrders
FROM Sales.Customers AS c
LEFT JOIN (
    -- Subquery
    SELECT
        CustomerID,
        COUNT(*) AS TotalOrders
    FROM Sales.Orders
    GROUP BY CustomerID
) AS o
    ON c.CustomerID = o.CustomerID;


--SUBQUERY | COMPARISON OPERATORS
--Find the products that have a price higher than the average price of all products.

-- Main Query
SELECT
    ProductID,
    Price,
    (SELECT AVG(Price) FROM Sales.Products) AS AvgPrice -- Subquery
FROM Sales.Products
WHERE Price > (SELECT AVG(Price) FROM Sales.Products); -- Subquery



--SUBQUERY | IN OPERATOR
--Show the details of orders made by customers in Germany.

SELECT
    *
FROM Sales.Orders
WHERE CustomerID IN (
    -- Subquery
    SELECT
        CustomerID
    FROM Sales.Customers
    WHERE Country = 'Germany'
);


--Show the details of orders made by customers not in Germany.
SELECT
    *
FROM Sales.Orders
WHERE CustomerID NOT IN (
    -- Subquery
    SELECT
        CustomerID
    FROM Sales.Customers
    WHERE Country = 'Germany'
);


--SUBQUERY | ANY OPERATOR
--Find female employees whose salaries are greater than the salaries of any male employees.
SELECT
    EmployeeID, 
    FirstName,
    Salary
FROM Sales.Employees
WHERE Gender = 'F'
  AND Salary > ANY (
      SELECT Salary
      FROM Sales.Employees
      WHERE Gender = 'M'
  );


--CORRELATED SUBQUERY
--Show all customer details and the total orders for each customer using a correlated subquery.
SELECT
    *,
    (SELECT COUNT(*)
     FROM Sales.Orders o
     WHERE o.CustomerID = c.CustomerID) AS TotalSales
FROM Sales.Customers AS c;



--SUBQUERY | EXISTS OPERATOR
--Show the details of orders made by customers in Germany.
SELECT
    *
FROM Sales.Orders AS o
WHERE EXISTS (
    SELECT 1
    FROM Sales.Customers AS c
    WHERE Country = 'Germany'
      AND o.CustomerID = c.CustomerID
);


--Show the details of orders made by customers not in Germany.
SELECT
    *
FROM Sales.Orders AS o
WHERE NOT EXISTS (
    SELECT 1
    FROM Sales.Customers AS c
    WHERE Country = 'Germany'
      AND o.CustomerID = c.CustomerID
);