-- Write your query below
WITH bonus as (
    SELECT employee_id, salary
    FROM employees
    WHERE employee_id % 2 != 0 AND name NOT LIKE 'M%'
)

SELECT e.employee_id, coalesce(b.salary,0) as bonus
FROM employees e LEFT JOIN bonus b ON e.employee_id = b.employee_id