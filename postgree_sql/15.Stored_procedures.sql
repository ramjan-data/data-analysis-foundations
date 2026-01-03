/* Procedures Syntax: 

		CREATE PROCEDURE procedure_name(parameters)
		LANGUAGE plpgsql
		AS $$
		BEGIN
   			 -- SQL statements
		END;
		$$;


Execution: CALL procedure_name(args);
		
*/


--Print a message
CREATE OR REPLACE PROCEDURE say_hello()
LANGUAGE plpgsql
AS $$
BEGIN
	RAISE NOTICE 'hello from postgreeSQL procedure';
END;
$$;	

--Call it
CALL say_hello()


SELECT * FROM customers
--Procedure with Input Parameters
--increase the score of customers
CREATE PROCEDURE increase_salary(
	p_id INT,
	P_increment NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
	UPDATE customers
	SET score=score + p_increment
	WHERE ID= p_id;
END;
$$;

--call it
CALL increase_salary(1, 122)

--see results
SELECT *  FROM customers




--Using IF Condition Inside Procedure
CREATE OR REPLACE PROCEDURE check_score(p_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    current_score NUMERIC;
BEGIN
    SELECT score INTO current_score
    FROM customers
    WHERE id = p_id;

    IF current_score > 500 THEN
        RAISE NOTICE 'High score';
    ELSE
        RAISE NOTICE 'low score';
    END IF;
END;
$$;

CALL check_score(1)


--transcription control
CREATE OR REPLACE PROCEDURE transfer_money(
    from_ID INT,
    to_ID INT,
    amount NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE 
	sender_balance NUMERIC;
BEGIN
	SELECT salary INTO sender_balance
	FROM sales.employees
	WHERE employeeid= from_id;

	IF sender_balance < amount THEN 
			RAISE EXCEPTION 'Insufficient balance';
	END IF;

	UPDATE sales.employees SET salary=salary-amount WHERE employeeid=from_id;
	UPDATE sales.employees SET salary=salary+amount WHERE employeeid=to_id;

EXCEPTION
    WHEN others THEN
        ROLLBACK;
        RAISE NOTICE 'Transfer failed';
	
END;
$$;

SELECT employeeid,salary FROM sales.employees
CALL transfer_money(1,2,5000);



/* IN ,OUT, INOUT Parameters */
--IN (Used to pass values into a procedure)
CREATE OR REPLACE PROCEDURE get_bonus(
    IN p_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Bonus is %', p_salary * 0.10;
END;
$$;

CALL get_bonus(1200) 



--OUT(Used to return values from a procedure)
CREATE OR REPLACE PROCEDURE calculate_bonus(
    IN p_salary NUMERIC,
    OUT bonus NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    bonus = p_salary * 0.10;
END;
$$;

CALL calculate_bonus( 1200, NULL)



--INOUT(Act as both)
CREATE OR REPLACE PROCEDURE tax_adjustment(
    INOUT amount NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    amount = amount - (amount * 0.15);
END;
$$;

CALL tax_adjustment(1200)


