
# 1757. Recyclable and Low Fat Products 
select product_id from Products where low_fats = 'Y' and recyclable = 'Y'

# 584. Find Customer Referee   
select name from Customer where referee_id <> '2' or referee_id is null;
# Learnt about null statements here 

# 595. Big Countries
select name, population, area from World where area >= 3000000 or population >= 25000000

# 1148. Article Views is
select distinct author_id as id from Views where author_id = viewer_id order by id

