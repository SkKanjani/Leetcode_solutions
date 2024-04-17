
-- Problem: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT v.customer_id, SUM(CASE WHEN t.transaction_id IS NULL THEN 1 ELSE 0 END) count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON t.visit_id=v.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id