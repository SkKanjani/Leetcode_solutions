
-- Problem: https://leetcode.com/problems/recyclable-and-low-fat-products
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT product_id
FROM Products
WHERE low_fats='Y' AND recyclable='Y'