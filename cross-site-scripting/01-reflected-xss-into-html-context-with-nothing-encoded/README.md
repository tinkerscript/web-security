# Reflected XSS into HTML context with nothing encoded
APPRENTICE

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function.

## Решение
Вожу в строке поиска:

`<img src=x onerror=alert(1)>`

Задание выполнено.
