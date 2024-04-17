
-- Problem: https://leetcode.com/problems/product-sales-analysis-i
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT p.product_name, s.year, s.price
FROM Sales s
LEFT JOIN Product p ON p.product_id=s.product_id