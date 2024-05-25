-- 1407. Top Travellers
SELECT  name,
    CASE
        WHEN user_id is NULL THEN 0
        ELSE SUM(distance)
    END as travelled_distance
FROM Users as u
LEFT JOIN Rides as r ON r.user_id = u.id
GROUP BY user_id
ORDER BY travelled_distance desc, name asc;
