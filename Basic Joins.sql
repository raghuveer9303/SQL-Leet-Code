# 1378. Replace Employee ID With The Unique Identifier
select EmployeeUNI.unique_id, Employees.name
from Employees
left join EmployeeUNI on Employees.id = EmployeeUNI.id

# 1068. Product Sales Analysis I
select Product.product_name, Sales.year, Sales.price 
from Sales 
left join Product on Sales.product_id = Product.product_id

# 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT 
  v.customer_id, 
  COUNT(t.visit_id) AS count_no_trans 
FROM 
  Visits AS v 
  LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id 
GROUP BY 
  v.customer_id
HAVING 
  COUNT(t.visit_id) > 0;  -- Exclude customers with 0 transactions

# 197. Rising Temperature
SELECT W1.id 
FROM
    Weather W1
JOIN
    Weather W2
ON
    DATEDIFF(W1.recordDate, w2.recordDate) = 1
WHERE
    W1.temperature > W2.temperature
