-- 1587. Bank Account Summary II
SELECT name, SUM(amount) as balance
FROM Users as u
LEFT JOIN Transactions as t ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000
