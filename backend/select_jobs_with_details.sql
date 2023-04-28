SELECT Jobs.name,
COUNT(Documents.id) AS 'total_documents'
FROM Jobs
LEFT JOIN Documents
ON Documents.job_id = Jobs.id
WHERE Jobs.deleted_at IS NULL
GROUP BY Jobs.id
ORDER BY Jobs.name