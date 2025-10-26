
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


