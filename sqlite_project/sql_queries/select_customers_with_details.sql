SELECT Customers.name, 
COUNT(Jobs.id) AS 'total_jobs'
FROM Customers 
LEFT JOIN Jobs
ON Jobs.customer_id = Customers.id
WHERE Customers.deleted_at IS NULL
GROUP BY Customers.id