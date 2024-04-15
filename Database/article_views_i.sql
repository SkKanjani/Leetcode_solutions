
-- Problem: https://leetcode.com/problems/article-views-i
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT DISTINCT(author_id) id
FROM Views
WHERE author_id=viewer_id
ORDER BY author_id ASC