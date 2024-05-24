/* 1378. Replace Employee ID With The Unique Identifier */
SELECT  name, unique_id
FROM Employees as e1
LEFT JOIN EmployeeUNI AS e2 ON e1.id = e2.id
