
-- Problem: https://leetcode.com/problems/rising-temperature
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT w1.id
FROM Weather w1
INNER JOIN Weather w2 ON w1.id<>w2.id
WHERE dateDiff(Day, w2.recordDate,w1.recordDate) = 1 AND w1.Temperature > w2.Temperature;