--data query language

--selecting all columns
SELECT * FROM orders;

--selecting few columns
SELECT order_id,sales FROM orders;
			
--WHERE(filters data based on conditions)
SELECT * FROM orders 
WHERE sales>=20;

--ORDER BY(sort data ascending or descending)
SELECT*FROM orders 
ORDER BY sales ASC;

SELECT * FROM crimson 
ORDER BY 
	score ASC,
	salary DESC;


--GROUP BY(combine rows with the same values)
--find total score for each country's emloyees
SELECT country,
SUM(score) AS total_scores
FROM customers
GROUP BY country;


--find total score and total number of employee for each country
SELECT  country,
	SUM(score) AS tatal_scores,
	COUNT (id) AS total_employee
FROM customers
GROUP BY country;

--HAVING(can be use only after GROUP BY),its like a conditions.
SELECT country,
	SUM(score) AS tatal_scores,
	COUNT (id) AS total_employee
FROM customers
GROUP BY country
HAVING SUM(score)>800;

--Use both WHERE AND HAVING
SELECT country,
	SUM(score) AS tatal_scores,
	COUNT (id) AS total_employee
FROM customers
WHERE score>320
GROUP BY country
HAVING SUM(score)>800;


--DISTINCT(remove duplicates data)
SELECT DISTINCT country 
FROM customers;

--LIMIT(restrict the number of rows returned)
SELECT * FROM customers
LIMIT 3;

--top three according to highest score
SELECT * FROM customers
ORDER BY score DESC
LIMIT 3;

--lowest three score
SELECT * FROM customers
ORDER BY score ASC
LIMIT 3;


--seeing somthing new
SELECT 123 AS statistics_data;
SELECT 'hey man' AS welcome;

--to see a new column in output
SELECT id, score, 'nothing' AS idk FROM customers;

SELECT id, score, score*2 AS double_score FROM customers;



			