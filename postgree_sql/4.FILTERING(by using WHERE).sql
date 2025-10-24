--FILTERING DATA (WHERE operators)
--comparison operators(=,=!, >, >=, <, <=)
SELECT * FROM orders;

--retrieve all orders with sales more than 20
SELECT * FROM orders 
WHERE sales>20;   

--retrieve all orders with atmost 20 sales
SELECT * FROM orders
WHERE sales<= 20; 
--so on...





--LOGICAL operators(AND,OR,NOT)
--AND(all conditions must be true)
--OR(atleast one conditions must be true)
--NOT(exclude matching value)
SELECT * FROM customers
WHERE country='USA' AND score>=100;


--RANGE operators(BETWEEN--check if a value within a range)
SELECT * FROM customers
WHERE score BETWEEN 500 AND 800;


--Membership operators(IN--if a value exist in list, NOT IN-vice versa)
SELECT * FROM customers
WHERE country IN ('USA', 'Germany');  --works like OR operators

--SEARCH operators(LIKE-search for a pattern in text)
--find all customers whose name start with 'M'
SELECT * FROM customers
WHERE first_name LIKE 'M%';

--find all customers whose name ends with 'n'
SELECT * FROM customers
WHERE first_name LIKE '%n';

--find all customers whose name has 'n'
SELECT * FROM customers
WHERE first_name LIKE '%n%';

--find all customers whose third position of name has 'r'
SELECT * FROM customers
WHERE  first_name LIKE '__r%';








