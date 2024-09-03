# 1378. Replace Employee ID With The Unique Identifier
select EmployeeUNI.unique_id, Employees.name
from Employees
left join EmployeeUNI on Employees.id = EmployeeUNI.id

# 1068. Product Sales Analysis I
select Product.product_name, Sales.year, Sales.price 
from Sales 
left join Product on Sales.product_id = Product.product_id