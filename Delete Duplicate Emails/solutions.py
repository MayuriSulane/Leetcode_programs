# Write your MySQL query statement below
DELETE e1 
FROM Person e1, Person e2 
WHERE e1.id > e2.id 
AND e1.email = e2.email ;