# 1378. Replace Employee ID With The Unique Identifier
select EmployeeUNI.unique_id, Employees.name
from Employees
left join EmployeeUNI on Employees.id = EmployeeUNI.id

