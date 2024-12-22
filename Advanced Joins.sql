-- 1731. The Number of Employees Which Report to Each Employee

SELECT a.reports_to AS employee_id, b.name, count(a.reports_to) AS reports_count, round(avg(a.age),0) AS average_age FROM Employees as a
INNER JOIN Employees as b
ON a.reports_to = b.employee_id
GROUP BY a.reports_to
ORDER BY employee_id

-- 1789. Primary Department for Each Employee

SELECT employee_id, department_id FROM Employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1

UNION

SELECT employee_id, department_id FROM Employee
WHERE primary_flag = 'Y'