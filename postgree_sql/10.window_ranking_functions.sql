/*
   SQL Window Ranking Functions

   Table of Contents:
     1. ROW_NUMBER
     2. RANK
     3. DENSE_RANK
     4. NTILE
     5. CUME_DIST
*/

--ROW_NUMBER, RANK, DENSE_RANK
--Rank Orders Based on Sales from Highest to Lowest
SELECT
    orderid,
    productid,
    sales,
    ROW_NUMBER() OVER(ORDER BY sales DESC) AS SalesRank_Row,
    RANK() OVER(ORDER BY sales DESC) AS SalesRank_Rank,
    DENSE_RANK()  OVER(ORDER BY Sales DESC) AS SalesRank_Dense
FROM Sales.Orders;


--Use Case | Top-N Analysis: Find the Highest Sale for Each Product
SELECT *
FROM (
    SELECT
        orderid,
        productid,
        sales,
        ROW_NUMBER() OVER (PARTITION BY Productid ORDER BY sales DESC) AS RankByProduct
    FROM sales.orders
) AS TopProductSales
WHERE RankByProduct = 1;


--Use Case | Bottom-N Analysis: Find the Lowest 2 Customers Based on Their Total Sales
SELECT *
FROM (
    SELECT
        customerid,
        SUM(sales) AS TotalSales,
        ROW_NUMBER() OVER (ORDER BY SUM(Sales)) AS RankCustomers
    FROM sales.orders
    GROUP BY customerid
) AS BottomCustomerSales
WHERE RankCustomers <= 2;


--Use Case | Assign Unique IDs to the Rows of the 'Order Archive'
SELECT
    ROW_NUMBER() OVER (ORDER BY OrderID, OrderDate) AS UniqueID,
    *
FROM Sales.OrdersArchive;

/*
   Use Case | Identify Duplicates:
   Identify Duplicate Rows in 'Order Archive' and return a clean result without any duplicates
*/
SELECT *
FROM (
    SELECT
        ROW_NUMBER() OVER (PARTITION BY OrderID ORDER BY CreationTime DESC) AS rn,
        *
    FROM Sales.OrdersArchive
) AS UniqueOrdersArchive
WHERE rn = 1;


--NTILE()
--Divide Orders into Groups Based on Sales
SELECT 
    OrderID,
    Sales,
    NTILE(1) OVER (ORDER BY Sales) AS OneBucket,
    NTILE(2) OVER (ORDER BY Sales) AS TwoBuckets,
    NTILE(3) OVER (ORDER BY Sales) AS ThreeBuckets,
    NTILE(4) OVER (ORDER BY Sales) AS FourBuckets,
    NTILE(2) OVER (PARTITION BY ProductID ORDER BY Sales) AS TwoBucketByProducts
FROM Sales.Orders;

--Segment all Orders into 3 Categories: High, Medium, and Low Sales.
SELECT
    OrderID,
    Sales,
    Buckets,
    CASE 
        WHEN Buckets = 1 THEN 'High'
        WHEN Buckets = 2 THEN 'Medium'
        WHEN Buckets = 3 THEN 'Low'
    END AS SalesSegmentations
FROM (
    SELECT
        OrderID,
        Sales,
        NTILE(3) OVER (ORDER BY Sales DESC) AS Buckets
    FROM Sales.Orders
) AS SalesBuckets;


--Divide Orders into Groups for Processing
SELECT 
    NTILE(5) OVER (ORDER BY OrderID) AS Buckets,
    *
FROM Sales.Orders;



-- CUME_DIST
--Find Products that Fall Within the Highest 40% of the Prices
SELECT 
    Product,
    Price,
    DistRank,
    CONCAT(DistRank * 100, '%') AS DistRankPerc
FROM (
    SELECT
        Product,
        Price,
        CUME_DIST() OVER (ORDER BY Price DESC) AS DistRank
    FROM Sales.Products
) AS PriceDistribution
WHERE DistRank <= 0.4;