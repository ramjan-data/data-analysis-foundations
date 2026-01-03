/* Trigger: trigger is database logic that executes 
			 automatically when a specific event happens on a table.

	It fires on:
		-INSERT
		-UPDATE
		-DELETE


	syntax:
		CREATE OR REPLACE FUNCTION function_name()
		RETURNS TRIGGER
		LANGUAGE plpgsql
		AS $$
		BEGIN
   			-- logic
    		RETURN NEW; -- or OLD
		END;
		$$;


NEW → new row (INSERT / UPDATE)
OLD → existing row (UPDATE / DELETE)


Creating the Trigger:
					CREATE TRIGGER trigger_name
					BEFORE INSERT OR UPDATE
					ON table_name
					FOR EACH ROW
					EXECUTE FUNCTION function_name();


*/

ALTER TABLE sales.employees
ADD COLUMN updated_at TIMESTAMP;


--USE | Auto-update updated_at
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_updated_at
BEFORE UPDATE
ON sales.employees
FOR EACH ROW
EXECUTE FUNCTION set_updated_at();

--check
UPDATE sales.employees
SET department ='marketingg'
WHERE employeeid= 1

SELECT * FROM sales.employees




--USE | Data validation (Reject Bad data)
CREATE OR REPLACE FUNCTION validate_salary()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$ 
BEGIN
 	IF NEW.salary <=0 THEN
	 	RAISE EXCEPTION 'Salary must be positive';
	END IF;
	RETURN NEW;
END;
$$;

CREATE TRIGGER trg_validate_salary
BEFORE INSERT OR UPDATE
ON sales.employees
FOR EACH ROW
EXECUTE FUNCTION validate_salary();
	
--Check
UPDATE sales.employees
SET salary = -12000
WHERE employeeid=1




--USE| Prevent Deletion (Business Rule Enforcement)
CREATE OR REPLACE FUNCTION block_sales_employee_delete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN 
	IF OLD.department = 'Sales' THEN
		RAISE EXCEPTION 'Sales employees should not be deleted';
	END IF;
	RETURN OLD;
END;
$$;

CREATE OR REPLACE TRIGGER trg_block_sales
BEFORE DELETE
ON sales.employees
FOR EACH ROW
EXECUTE FUNCTION block_sales_employee_delete();
	
--check
DELETE FROM sales.employees
WHERE department='Sales'



--USE | Auditing / Logging (Very Common)
CREATE TABLE sales.employee_audit(
	audit_id SERIAL PRIMARY KEY,
	employee_id INT,
	old_salary NUMERIC,
	new_salary NUMERIC,
	changed_at TIMESTAMP
)


CREATE OR REPLACE FUNCTION log_salary_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN

	--Log only if salary actually changed
	IF OLD.salary IS DISTINCT FROM NEW.salary THEN
    INSERT INTO sales.employee_audit(employee_id, old_salary, new_salary, changed_at)
    VALUES (OLD.employeeid, OLD.salary, NEW.salary, NOW());
	END IF;

    RETURN NEW;
END;
$$;


CREATE TRIGGER trg_salary_audit
AFTER UPDATE OF salary   --Trigger fires only when salary changes, not on every update.
ON sales.employees
FOR EACH ROW
EXECUTE FUNCTION log_salary_change();


UPDATE sales.employees
SET salary = 60000
WHERE employeeid=1


SELECT * FROM sales.employee_audit





--Disabling and Dropping Triggers
ALTER TABLE sales.employees DISABLE TRIGGER trg_salary_audit;

DROP TRIGGER trg_salary_audit ON sales.employees;






