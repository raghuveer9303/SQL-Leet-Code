# 2356. Number of Unique Subjects Taught by Each Teacher

SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt 
FROM Teacher
GROUP BY teacher_id

# 1141. User Activity for the Past 30 Days I

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE datediff('2019-07-27',activity_date)<30 
AND activity_date <= '2019-07-27' 
GROUP BY activity_date


# 596. Classes More Than 5 Students

SELECT class FROM Courses GROUP BY class HAVING COUNT(class) >= 5


# 1729. Find Followers COUNT

SELECT user_id, COUNT(follower_id) AS followers_count FROM Followers
GROUP BY user_id
ORDER BY user_id ASC