/* Aggregation  AND WINDOW FUNCTION
*/

--aggregration
SELECT customer_id,
COUNT(*) AS total_numbr_order,
SUM(sales) AS total_sales,
AVG(sales) AS avg_sales,
MAX(sales) AS highest_sales,
MIN(sales) AS lowest_sales
FROM orders
GROUP BY customer_id
ORDER BY customer_id ASC

--find the total sales across all orders
SELECT 
SUM(sales) AS total_sales
FROM sales.orders

--find the total sales for each product 
SELECT productid,
SUM(sales) AS total_sales
FROM sales.orders
GROUP BY productid


--window function
--find the total sales for each product, additionally probide details such orderid and orderdate(window func)
--use PARTITION BY
SELECT orderid,
orderdate,
productid,
orderstatus,
sales,
SUM(sales) OVER() total_sales,
SUM(sales) OVER(PARTITION BY productid) total_salesby_products,
SUM(sales) OVER(PARTITION BY productid, orderstatus) total_salesby_productsand_status
FROM sales.orders

--rank each order based on their sales from highest to lowest
SELECT
orderid,
orderdate,
sales,
RANK() OVER(ORDER BY sales DESC) rank_sales
FROM sales.orders

--ROWS BETWEEN
SELECT 
orderid,
orderdate,
orderstatus,
sales,
SUM(sales) OVER(PARTITION BY orderstatus ORDER BY orderdate 
ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING) AS totalsales_of_three_f,

SUM(sales) OVER(PARTITION BY orderstatus ORDER BY orderdate 
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS totalsales_of_three_p,

SUM(sales) OVER(PARTITION BY orderstatus ORDER BY orderdate 
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS totalsales_of_unbounded_p
FROM sales.orders





/*window aggregate function

 Table of Contents:
    1. COUNT
    2. SUM
    3. AVG
    4. MAX / MIN
    5. ROLLING SUM & AVERAGE Use Case
*/


--Find the Total Number of Orders and the Total Number of Orders for Each Customer
SELECT
    orderID,
    orderDate,
    customerID,
    COUNT(*) OVER() AS TotalOrders,
    COUNT(*) OVER(PARTITION BY CustomerID) AS OrdersByCustomers
FROM Sales.orders


/*
   - Find the Total Number of Customers
   - Find the Total Number of Scores for Customers
   - Find the Total Number of Countries
*/
SELECT
    *,
    COUNT(*) OVER () AS TotalCustomersStar,
    COUNT(1) OVER () AS TotalCustomersOne,
    COUNT(score) OVER() AS TotalScores,
    COUNT(country) OVER() AS TotalCountries
FROM Sales.customers

 
--Check whether the table 'OrdersArchive' contains any duplicate rows
SELECT 
    * 
FROM (
    SELECT 
        *,
        COUNT(*) OVER(PARTITION BY OrderID) AS CheckDuplicates
    FROM Sales.OrdersArchive
) t
WHERE CheckDuplicates > 1


--SUM()
/*  - Find the Total Sales Across All Orders 
   - Find the Total Sales for Each Product
*/
SELECT
    orderid,
    orderdate,
    sales,
    productid,
    SUM(sales) OVER () AS TotalSales,
    SUM(sales) OVER (PARTITION BY productid) AS SalesByProduct
FROM sales.orders


--Find the Percentage Contribution of Each Product's Sales to the Total Sales
SELECT
    orderid,
    productid,
    sales,
    SUM(sales) OVER () AS TotalSales,
    ROUND(CAST(sales AS NUMERIC) / SUM(Sales) OVER () * 100, 2) AS PercentageOfTotal
FROM sales.orders


--AVG()
/* - Find the Average Sales Across All Orders 
   - Find the Average Sales for Each Product
*/
SELECT
    orderid,
    orderdate,
    sales,
    productid,
    ROUND(AVG(sales) OVER (),2) AS AvgSales,
    ROUND(AVG(sales) OVER (PARTITION BY productid),2) AS AvgSalesByProduct
FROM sales.orders


--Find the Average Scores of Customers
SELECT
    customerid,
    lastname,
    score,
    COALESCE(score, 0) AS CustomerScore,
    AVG(score) OVER () AS AvgScore,
    AVG(COALESCE(score, 0)) OVER () AS AvgScoreWithoutNull
FROM sales.customers


--Find all orders where Sales exceed the average Sales across all orders
SELECT
    *
FROM (
    SELECT
        orderid,
        productid,
        sales,
        AVG(sales) OVER () AS Avg_Sales
    FROM sales.orders
) t 
WHERE sales > Avg_Sales


--MAX(), MIN()
--Find the Highest and Lowest Sales across all orders
SELECT 
    MIN(Sales) AS MinSales, 
    MAX(Sales) AS MaxSales 
FROM Sales.Orders


--Find the Lowest Sales across all orders and by Product
SELECT 
    orderid,
    productid,
    orderdate,
    sales,
    MIN(sales) OVER () AS LowestSales,
    MIN(sales) OVER (PARTITION BY ProductID) AS LowestSalesByProduct
FROM sales.orders


--Show the employees who have the highest salaries
SELECT *
FROM (
	SELECT *,
		   MAX(Salary) OVER() AS HighestSalary
	FROM Sales.Employees
) t
WHERE Salary = HighestSalary


--Find the deviation of each Sale from the minimum and maximum Sales
SELECT
    OrderID,
    OrderDate,
    ProductID,
    Sales,
    MAX(Sales) OVER () AS HighestSales,
    MIN(Sales) OVER () AS LowestSales,
    Sales - MIN(Sales) OVER () AS DeviationFromMin,
    MAX(Sales) OVER () - Sales AS DeviationFromMax
FROM Sales.Orders


--ROLLING AVERAGE
--Calculate the moving average of Sales for each Product over time
SELECT
    OrderID,
    ProductID,
    OrderDate,
    Sales,
    AVG(Sales) OVER (PARTITION BY ProductID) AS AvgByProduct,
    AVG(Sales) OVER (PARTITION BY ProductID ORDER BY OrderDate) AS MovingAvg
FROM Sales.Orders


--Calculate the moving average of Sales for each Product over time, including only the next order.
SELECT
    OrderID,
    ProductID,
    OrderDate,
    Sales,
    AVG(Sales) OVER (PARTITION BY ProductID ORDER BY OrderDate ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS RollingAvg
FROM Sales.Orders

