
-- Problem: https://leetcode.com/problems/average-time-of-process-per-machine
-- Difficulty: Easy
-- Solution: 

/* Write your T-SQL query statement below */
SELECT a1.machine_id, ROUND((SUM(a2.timestamp-a1.timestamp))/COUNT(a1.process_id), 3) processing_time
FROM Activity a1
INNER JOIN Activity a2 ON a2.machine_id=a1.machine_id AND a2.process_id=a1.process_id
WHERE a1.activity_type='start' AND a2.activity_type='end'
GROUP BY a1.machine_id