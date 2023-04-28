SELECT Customers.name
FROM Customers
WHERE Customers.deleted_at IS NULL
ORDER BY Customers.name