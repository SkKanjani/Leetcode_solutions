
-- Problem: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT eu.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eu ON eu.id=e.id
