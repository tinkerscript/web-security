# Username enumeration via subtly different responses
PRACTITIONER

This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

Candidate usernames
Candidate passwords
To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

## Решение
Intruder -> Settings -> Grep - Extract -> Add -> Fetch response. Выделить "Invalid username of password."

В окне результатов появится новая колонка. После сортировки станет ясно, что в случае одного из запросов сообщение не имеет точки на конце. Это пользователь "as400".

Выполню перебор паролей по предложенному словарю. По размеру ответа явно выделяется один из запросов. Это пароль "robert":
```
HTTP/2 302 Found
Location: /my-account?id=as400
Set-Cookie: session=K55PSAPlSF6fx1hyPCrcbHe7N5r0BotK; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0
```
Логинюсь как as400:robert. Задание выполнено.
