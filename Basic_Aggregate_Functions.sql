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

#1633. Percentage of Users Attended a Contest

SELECT R.contest_id, ROUND((COUNT(R.user_id)/(SELECT COUNT(*) FROM Users))*100,2) AS percentage
FROM Register AS R
LEFT JOIN Users AS U
ON U.user_id = R.user_id
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id ASC 

# 1211. Queries Quality and Percentage
SELECT query_name, ROUND(SUM(rating/position)/COUNT(query_name),2) AS quality, ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(query_name) *100 ,2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name

# 1193. Monthly Transactions 1
SELECT DATE_FORMAT(STR_TO_DATE(CONCAT(YEAR(trans_date),'-',MONTH(trans_date)), '%Y-%m'), '%Y-%m') AS month, country, COUNT(*) AS trans_count, SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) as trans_total_amount, SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY country, YEAR(trans_date), MONTH(trans_date)