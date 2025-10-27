/*  Aggregrations

  Table of Contents:
     1. Basic Aggregate Functions
        - COUNT
        - SUM
        - AVG
        - MAX
        - MIN
     2. Grouped Aggregations
        - GROUP BY
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


