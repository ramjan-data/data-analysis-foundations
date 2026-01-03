/* SQL Partitioning : Splitting one logical table into multiple physical tables based on a rule.

			Postgree SQL Structure:
							parent table- no data
							child table- actual data
							
			Types of partitioning:
								1.Range -by intervals(date, number)
								2.List  -by exact values(country, status...)
								3.Hash  -by distribution
*/


/*
______________________________________________________________________________________________________________________________
Partitioning type | Range
______________________________________________________________________________________________________________________________
*/
--rename old table
ALTER TABLE sales.orders RENAME TO orders_old;

--recreate table structure(it doesnt work because of primary key)
CREATE TABLE sales.orders
(LIKE sales.orders_old INCLUDING ALL)
PARTITION BY RANGE (creationtime);

--drop the primary key
SELECT constraint_name 
FROM information_schema.table_constraints
WHERE table_schema='sales'
	AND table_name='orders_old'
	AND constraint_type='PRIMARY KEY';

ALTER TABLE sales.orders_old 
DROP CONSTRAINT orders_pkey;

--recreate the partition table
CREATE TABLE sales.orders
(LIKE sales.orders_old INCLUDING ALL)
PARTITION BY RANGE (creationtime);

--now fix the primary key
ALTER TABLE sales.orders
ADD CONSTRAINT orders_pkey
PRIMARY KEY (orderid, creationtime);


--Create partitions
CREATE TABLE sales.orders_2025_jan
PARTITION OF sales.orders
FOR VALUES FROM('2025-01-01') TO ('2025-01-31');

CREATE TABLE sales.orders_2025_feb
PARTITION OF sales.orders
FOR VALUES FROM('2025-02-01') TO ('2025-02-28');

CREATE TABLE sales.orders_2025_MARCH
PARTITION OF sales.orders
FOR VALUES FROM('2025-03-01') TO ('2025-03-31');

--create a default partition(otherwise if any row falls outside defined ranges--insert fail)
CREATE TABLE sales.orders_default
PARTITION OF sales.orders DEFAULT;

	
--Move data
INSERT INTO sales.orders 
SELECT * FROM sales.orders_old;


--Quering partitioned table
SELECT *
FROM sales.orders
WHERE creationtime <= '2025-01-15';


--to create a parents table (if i dont have any)
CREATE TABLE sales.orderss (
    order_id     BIGINT,
    customer_id  BIGINT NOT NULL,
    order_date   DATE NOT NULL,
    status       TEXT,
    total_amount NUMERIC(12,2),
    PRIMARY KEY (order_id, order_date)
)
PARTITION BY RANGE (order_date);



/*
Good partition keys:
		-order_date (time-series)
		-created_at
		-tenant_id
		-region_id

Bad partition keys:
		-High-cardinality random values (uuid, order_id)
		-Columns rarely used in WHERE clauses
		-Frequently updated columns
*/



/*
________________________________________________________________________________
LIST Partitioning(categorical data-country,region,status,business unit...)
_________________________________________________________________________________
*/

--same syntax with:
PARTITION BY LIST (status)

FOR VALUES IN ('completed', 'shipped')



--HASH Partioning
PARTITION BY HASH (customer_id)

FOR VALUES WITH (MODULUS 4, REMAINDER 0)




--INDEXES | Each partition has its own index,Indexes are local to partitions
CREATE INDEX idx_orders_customer
ON sales.orders (customerid);



--Detaching & Dropping Old Data
ALTER TABLE sales.orders
DETACH PARTITION sales.orders_2023_01;

DROP TABLE sales.orders_2023_01;




--Monitoring
--Check partition sizes
SELECT
  relname,
  pg_size_pretty(pg_total_relation_size(relid))
FROM pg_catalog.pg_statio_user_tables
WHERE schemaname = 'sales'
ORDER BY pg_total_relation_size(relid) DESC;

--Check if pruning works
EXPLAIN ANALYZE
SELECT *
FROM sales.orders
WHERE creationtime <= '2025-01-15';



--Moving Data Between Partitions
INSERT INTO sales.orders_2025_jan
SELECT *
FROM sales.orders_default
WHERE order_date >= '2025-01-01'
  AND order_date < '2025-02-01';

DELETE FROM sales.orders_default
WHERE order_date >= '2025-01-01'
  AND order_date < '2025-02-01';









