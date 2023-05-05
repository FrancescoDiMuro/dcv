SELECT Customers.name AS 'customer', 
Documents.name AS 'document',
MAX(Revisions.version) AS 'actual_version',
MAX(Revisions.updated_at) AS 'last_modified',
Users.name
FROM Customers
LEFT JOIN Jobs 
ON Jobs.customer_id = Customers.id
LEFT JOIN Documents
ON Documents.job_id = Jobs.id
LEFT JOIN Revisions
ON Revisions.document_id = Documents.id
LEFT JOIN Users
ON Users.id = Revisions.user_id
WHERE Customers.id = 1 AND
Customers.deleted_at IS NULL
GROUP BY Documents.id