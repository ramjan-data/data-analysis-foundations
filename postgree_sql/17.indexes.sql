/* 
   SQL Indexing
   
*/


-- Create a Heap Table as a copy of Sales.Customers 
SELECT *
INTO Sales.DBCustomers
FROM Sales.Customers;


-- Test Query: Select Data and Check the Execution Plan
SELECT *
FROM Sales.DBCustomers
WHERE CustomerID = 1;




--INDEX TYPES | B-tree(used when : =, <, > , BETWEEN, ORDER BY, LIKE, MIN/MAX)

-- Create a B-tree Index on Sales.DBCustomers using CustomerID
CREATE INDEX idx_DBCustomers_ID
ON Sales.DBCustomers (CustomerID);

-- Drop the Index
DROP INDEX IF EXISTS sales.idx_DBCustomers_ID;


-- Create an additional B-tree Index on FirstName
CREATE INDEX idx_DBCustomers_FirstName
ON Sales.DBCustomers (FirstName);



--INDEX TYPES | COMPOSITE index(B-tree)
-- Create a Composite (Composed) Index on Country and Score 
CREATE INDEX idx_DBCustomers_CountryScore
ON Sales.DBCustomers (Country, Score);

-- Query that uses the Composite Index
SELECT *
FROM Sales.DBCustomers
WHERE Country = 'USA'
  AND Score > 500;

-- Query that likely won't use the Composite Index due to column order
SELECT *
FROM Sales.DBCustomers
WHERE Score > 500
  AND Country = 'USA';



/*
Leftmost Prefix Rule Explanation

	 For a composite index defined on columns (A, B, C, D)
	 	index will be used
		 	-A
		 	-A,B,
		 	-A,B,C
		index wont be used
			-B
			-A,C
			-A,B,D
			
*/



--INDEX TYPES | HASH (use : only for '=')
CREATE INDEX idx_customerid_hash
ON sales.customers USING HASH(customerid)

--Query
SELECT * FROM sales.customers
WHERE customerid=1




--INDEX TYPES | GIN(use : fast search inside arrays, Json, text search)
CREATE INDEX idx_status_gin
ON sales.orders USING GIN( to_tsvector('english', orderstatus));

--Query
SELECT * FROM Sales.orders
WHERE to_tsvector('english', orderstatus) @@ to_tsquery('shipped')




--INDEX TYPES | BRIN (use : huge table with correlated/ordered data)
CREATE INDEX idx_creationTime_brin
ON sales.orders USING BRIN(creationtime);

--Query
SELECT * FROM sales.orders
WHERE creationtime <= '2025-01-20';




--INDEX TYPES | Unique Indexes

-- Attempt to create a Unique Index on the Category column in Sales.Products.
   --Note: This may fail if duplicate values exist.
CREATE UNIQUE INDEX idx_Products_Category
ON Sales.Products (Category);
  
-- Create a Unique Index on the Product column in Sales.Products
CREATE UNIQUE INDEX idx_Products_Product
ON Sales.Products (Product);
  
-- Test Insert: Attempt to insert a duplicate value (should fail if the constraint is enforced)
INSERT INTO Sales.Products (ProductID, Product)
VALUES (106, 'Caps');




--INDEX TYPES | Partial  Index
-- Test Query: Select Customers where Country is 'USA' 
SELECT *
FROM Sales.Customers
WHERE Country = 'USA';
  
-- Create a Partial Index on the Country column for rows where Country = 'USA'
CREATE OR REPLACE INDEX idx_Customers_Country
ON Sales.Customers (customerid)
WHERE Country = 'USA';



--INDEX TYPES | Exression index 
CREATE INDEX index_lower_name
ON sales.customers(LOWER(firstname));

--Query that uses Expression index
SELECT * FROM sales.customers
WHERE LOWER(firstname)= 'jossef'


--Another example
CREATE INDEX idx_orders_month
ON sales.orders(EXTRACT(MONTH FROM orderdate));

--Query
SELECT * 
FROM sales.orders
WHERE EXTRACT(MONTH FROM orderdate)=2







/*_____________________________________________________________________________  
	Index Monitoring
-------------------------------------------------------------------------------
*/


--INDEX Monitoring | See index usage 
SELECT 
		schemaname,
		relname AS table_name,
		indexrelname AS index_name,
		idx_scan AS index_used,
		idx_tup_read ,
		idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC

--OR
SELECT * FROM pg_stat_user_indexes


--detect unused indexes
SELECT 
		relname AS table_name,
		indexrelname AS index_name
FROM pg_stat_user_indexes
WHERE idx_scan=0;




--INDEX Monitoring | Duplicate/redundant indexes
--example of redundancy
CREATE INDEX idx_customerid
ON sales.customers(customerid)

CREATE INDEX idx_customerid_name
ON sales.customers(customerid, firstname)


--audit all indexes on all table
SELECT 
		t.relname AS table_name,
		i.relname AS index_name,
		pg_get_indexdef(ix.indexrelid)
FROM pg_index ix
JOIN pg_class t 
ON t.oid=ix.indrelid
JOIN pg_class i
ON i.oid=ix.indrelid
ORDER BY table_name


--find duplicate indexes
SELECT 
		t.relname AS table_name,
		pg_get_indexdef(i.oid) AS index_defination,
		COUNT(*) AS how_many_dup
FROM pg_index ix
JOIN pg_class t 
ON t.oid=ix.indrelid
JOIN pg_class i
ON i.oid=ix.indrelid
GROUP BY t.relname,
pg_get_indexdef(i.oid) HAVING COUNT(*)>1;




--INDEX Monitoring | index size
SELECT 
		relname AS index_name,
		pg_size_pretty(pg_relation_size(oid)) AS size
FROM pg_class
WHERE relkind='i'
ORDER BY pg_relation_size(oid)


--index usage vs table scan reality
SELECT 
		relname,
		seq_scan,
		idx_scan
FROM pg_stat_user_tables;		



--index bloat / Fragmentation
SELECT 
		relname AS  index_name,
		pg_size_pretty(pg_relation_size(oid)) AS index_size
FROM pg_class
WHERE relkind='i'
ORDER BY pg_relation_size(oid) DESC

--to fix bloat
REINDEX INDEX idx_name;
REINDEX TABLE table_name;



/*statistics and planner decision
		key stats:
			n_distinct-how many unique values
			most_common_vals-frequent values
			most_common_freqs-their frequency
			null_frac-null percentage
*/			
SELECT 
		attname,
		n_distinct,
		most_common_vals
FROM pg_stats
WHERE tablename='orders';



--index-only scans
CREATE INDEX idx_orders_cover
ON sales.orders(orderid)
INCLUDE(orderstatus);

--Query
SELECT orderstatus
FROM sales.orders
WHERE orderid=1;



--indexes from a table
SELECT 
		i.relname  AS index_name,
		s.idx_scan,
		pg_get_indexdef(i.oid) AS index_defination
FROM pg_index ix
JOIN pg_class i 
ON i.oid=ix.indexrelid
LEFT JOIN pg_stat_user_indexes s
ON s.indexrelid=i.oid
WHERE ix.indrelid='sales.customers' :: regclass;






