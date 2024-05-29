-- 1661. Average Time of Process per Machine
WITH CTE AS(
SELECT *, sum(case when activity_type = "end" then timestamp else -timestamp end) as sub
FROM Activity
GROUP BY machine_id, process_id
)
SELECT machine_id, ROUND(AVG(sub),3) as processing_time
FROM CTE
GROUP BY machine_id

