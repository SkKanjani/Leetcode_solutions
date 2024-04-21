
-- Problem: https://leetcode.com/problems/not-boring-movies
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT * 
FROM Cinema
WHERE id%2<>0 AND description<>'boring'
ORDER BY rating DESC