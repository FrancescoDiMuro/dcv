SELECT Customers.name, 
MAX(Jobs.id) AS 'total_jobs',
MAX(Documents.id) AS 'total_documents'
FROM Customers, Jobs, Documents
WHERE Jobs.customer_id = Customers.id
AND Documents.job_id = Jobs.id
GROUP BY Customers.id

SELECT Customers.name, 
MAX(Jobs.id) AS 'total_jobs'
FROM Customers 
LEFT JOIN Jobs
ON Jobs.customer_id = Customers.id
GROUP BY Customers.id