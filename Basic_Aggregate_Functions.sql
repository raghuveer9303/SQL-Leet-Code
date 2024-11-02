# 620. Not Boring Movies
SELECT * FROM Cinema 
WHERE id%2 <> 0 AND description <> 'boring'
ORDER BY rating DESC

#1251. Average Selling Price
SELECT P.product_id, COALESCE(ROUND(SUM(P.price*U.units)/SUM(U.units),2),0) AS average_price
    FROM Prices AS P
LEFT JOIN UnitsSold AS U
    ON P.product_id = U.product_id 
    AND U.purchase_date <= P.end_date 
    AND U.purchase_date >= P.start_date
GROUP BY P.product_id

#1075. Project Employees 1
SELECT P.project_id, ROUND(AVG(E.experience_years),2) AS average_years
FROM Project AS P
LEFT JOIN Employee AS E
ON P.employee_id = E.employee_id
GROUP BY P.project_id