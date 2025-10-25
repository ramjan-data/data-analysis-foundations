'''
SQL FUNCTIONS:
i.single row functions(string, numeric, date and time, null)
ii.multi-row functions(aggregate, window)
'''

--(1) STRING FUNC(manipulation, calculation,extraction)
--manipulation(concate, upper, lower, trim, replace)
--CONCATE(combines multiple strings into one)
SELECT firstname,
		country,
		CONCAT(firstname, '-', country) AS name_country,
		UPPER(firstname) AS up_name,
		LOWER(firstname) AS low_name
FROM sales.customers;

--TRIM(removes leading and trailling space)
--find the customers whose first name contains leading or trailing space
SELECT firstname
FROM sales.customers
WHERE firstname != TRIM(firstname)
--OR
SELECT firstname ,
		LENGTH(firstname) AS len_name,
		LENGTH(firstname)-LENGTH(TRIM(firstname)) AS flagg
FROM sales.customers

--REPLACE
--remove dashes(-) from a phone number
SELECT '123-456-789' AS old_numbr,
REPLACE('123-456-789','-','') AS clean_numbr;

--change a  file type
SELECT 'report.png' AS old_file,
REPLACE('report.png','.png','.txt') AS new_file;

--LENGTH()-yk

--EXTRACTION(LEFT, RIGHT, SUBSTRING)
SELECT firstname ,
	LEFT(firstname, 2) AS first_2_char,
	RIGHT(firstname, 2) AS last_2_char,
	SUBSTRING(firstname, 2, 3) AS middle_3_char,  --SUBSTRING(value, start, length)
	SUBSTRING(firstname, 2, LENGTH(firstname)) AS after_1_char  
FROM sales.customers





--(2) NUMERIC FUNCT()
--ROUND 
SELECT 3.516 AS raw_val,
ROUND (3.516, 2),
ROUND(3.516,1),
ROUND (3.516,0)

--ABS
SELECT -10,
ABS(-10),
ABS(10)




--(3) DATE AND TIME FUNC
SELECT orderid,
	orderdate,
	shipdate,
	creationtime,
	'2025-10-09' AS hardcoded,
	NOW() AS today  --current date and time when quiry executed
FROM sales.orders;



--part extraction
SELECT  orderid,
		creationtime,
		EXTRACT(YEAR FROM creationtime) AS year,
		EXTRACT(HOUR FROM creationtime) AS hours,

		DATE_PART('month',creationtime) months,
		DATE_PART('week',creationtime) AS weeks,
		DATE_PART('quarter',creationtime) AS quarter,

		TO_CHAR(creationtime,'day') AS day_name, 
		TO_CHAR(creationtime,'month') AS month_name,

		DATE_TRUNC('minute',creationtime) till_min,
		DATE_TRUNC('month',creationtime)  till_month
		
FROM sales.orders;	


--Uses in analysis
--how many orders placed on each month
SELECT TO_CHAR(creationtime,'month'),
COUNT(*)
FROM sales.orders
GROUP BY TO_CHAR(creationtime,'month');

SELECT EXTRACT(MONTH FROM creationtime),
COUNT(*)
FROM sales.orders
GROUP BY EXTRACT(MONTH FROM creationtime);

--show all orders that were placed in february
SELECT * FROM sales.orders
WHERE EXTRACT(MONTH FROM creationtime)=2;


--Formating and Casting
--FORMAT(use TO_CHAR(YYYY,YY,MM,Mon,Month,dd,dy,day,HH24:MI:SS) instead)
SELECT  orderid,
		creationtime,
		TO_CHAR(creationtime,'day') dd,
		TO_CHAR(creationtime,'Mon YYYY') months_yr,
		TO_CHAR(creationtime,'YYYY-MM-dd') fulldate,
		TO_CHAR(creationtime,'HH24:MI:SS') times
FROM sales.orders;	

--write(Day Wed Jan Q1 2025)
SELECT orderid,
creationtime,
'Day ' || TO_CHAR(creationtime,'Dy Mon') ||' '||' Q1 '||
DATE_PART('year',creationtime) AS customformat
FROM sales.orders

--format in aggregration
SELECT TO_CHAR(orderdate,'Mon yy'),
COUNT(*)
FROM sales.orders
GROUP BY TO_CHAR(orderdate,'Mon yy')
--format in standerdization

--CAST(converts a datetime to diff data types)
SELECT 
CAST('1223' AS INT)  AS str_to_int,
CAST('2025-03-04' AS DATE) str_to_date,
CAST(creationtime AS DATE),
CAST(creationtime AS VARCHAR) datetime_to_varchar
FROM sales.orders


--Calculations(add,diff)
SELECT orderdate,
		orderdate + INTERVAL '5 days' five_day_later, 	--add 5 days
		orderdate + INTERVAL '5 months' five_month_later,	--add 5 months
		orderdate - INTERVAL '5 months' five_month_before,	--substruct 5 months
		NOW()-INTERVAL '10minutes',
		creationtime - orderdate AS diff  --difference
FROM sales.orders;


--calculate the age of employees
SELECT  employeeid,
		birthdate,
		AGE(birthdate) ,
		NOW()-birthdate AS age_in_days
FROM sales.employees

--find the shipping duration in days for each month
SELECT  TO_CHAR(orderdate,'Mon') AS month_name,
ROUND(AVG(shipdate-orderdate),2) AS avg_shipping_day 
FROM sales.orders
GROUP BY TO_CHAR(orderdate,'Mon');

--find the numbr of days between each order and the previous order
SELECT orderid,
orderdate AS currentdate,
LAG(orderdate) OVER (ORDER BY orderdate) AS previous_order_date,
orderdate - LAG(orderdate) OVER (ORDER BY orderdate) AS diff
FROM sales.orders




--(4)NULL FUNCTIONS
--COALESCE(value, value2, value3,...)
--find the average scores of the customers
SELECT  customerid,
score ,  
COALESCE(score,0) AS score2 ,
AVG(score) OVER() AS  avgscores,
AVG(COALESCE(score,0)) OVER() avgscores2
FROM sales.customers
ORDER BY customerid ASC

--display the full name of customers in a single field by merging their first and last names, and add  10 bonus point to each customers score
SELECT  customerid,
firstname,
lastname,
COALESCE(lastname,'') lasname2,
firstname ||' '|| COALESCE(lastname,'') AS fullname,
score,
COALESCE(score,0)+10 score_with_bonus
FROM sales.customers	
--fix null before doing JOIN

--sort the customers from lowest to highest scores, with NULLs appearing last(we already have it in postgree)
SELECT customerid,
score
FROM sales.customers
ORDER BY score

SELECT customerid,
score
--CASE WHEN score IS NULL THEN 1 ELSE 0 END flags
FROM sales.customers
ORDER BY  CASE WHEN score IS NULL THEN 1 ELSE 0 END, score


--NULLIF(value1,value2)-if two values match,it'll show NULL otherwise the first value
--find the sales price for each order by dividing sales by quantity
SELECT orderid,
sales,
quantity,
sales/NULLIF(quantity,0) AS Price
FROM sales.orders

--value IS NULL(returns TRUE if the values is NULL--checking)
--value IS NOT NULL(revers)
--idenntify the customers who have no scores(uses of filtering data)
SELECT * FROM sales.customers
WHERE score IS NULL

--list all customers who have scores
SELECT * FROM sales.customers
WHERE score IS NOT NULL

--IS NULL use case ANTI JOINS
--list all detsils for customers who have not placed any orders
SELECT 
c.*,
o.orderid
FROM sales.customers AS c
LEFT JOIN sales.orders AS o
ON c.customerid=o.customerid
WHERE o.customerid IS NULL

--NULL vs EMPTY vs SPACE
WITH ordersss AS(
SELECT 1 id, 'A' category UNION
SELECT 2,NULL UNION
SELECT 3, '' UNION
SELECT 4, '  '
)
SELECT *,
LENGTH(category) categorylen,
TRIM(category) AS policy1,  --policy1- use null and empty, not a space
LENGTH(TRIM(category)),
NULLIF(TRIM(category),'') AS policy2,	--policy2-use null
COALESCE(NULLIF(TRIM(category),''), 'unknown' ) policy3
FROM ordersss
ORDER BY id ASC



--CASE Statement(condition)
--use1-Categorizing data
SELECT category,
SUM(sales) AS totalsales
FROM(
SELECT orderid,
sales,
CASE 
	WHEN sales > 50 THEN 'high'
	WHEN sales > 20 THEN 'medium'
	ELSE 'low'
END	category
FROM sales.orders
)
GROUP BY category
ORDER BY totalsales DESC

--use2-MAPPING(transform the values from one form to another)
--retrive empoyee details with gender displayed as full text
SELECT employeeid,
firstname,
lastname,
gender,
CASE 
	WHEN gender= 'M' THEN 'MALE'
	WHEN gender= 'F' THEN 'FEMALE'
	ELSE 'N/A'
END gender_fulltxt,

CASE gender						--short/quick form of CASE statement
	WHEN 'M' THEN 'MALE'
	WHEN 'F' THEN 'FEMALE'
	ELSE 'N/A'
END gender_fulltxt2	
FROM sales.employees


--use3-NULL handling
SELECT customerid,
lastname,
score,
ROUND(AVG(score) OVER()) avgscore,
CASE 
	WHEN score IS NULL THEN 0
	ELSE score
END score2,

AVG(CASE 
	WHEN score IS NULL THEN 0
	ELSE score
END) OVER() avgscore2
FROM sales.customers


--conditional aggregation
--count how many times each customers has made an order with sales greater than 30
SELECT orderid,
customerid,
sales,
CASE 
	WHEN sales>30 THEN 1
	ELSE 0
END salesflag	
FROM sales.orders
ORDER BY customerid ASC

--step2
SELECT 
customerid,
SUM(CASE 
	WHEN sales>30 THEN 1
	ELSE 0
END) totalorders_highsales,
COUNT(*) totalorders
FROM sales.orders
GROUP BY customerid










