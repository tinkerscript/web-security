# File path traversal, traversal sequences stripped with superfluous URL-decode
PRACTITIONER

This lab contains a path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
Найдено перебором по dotdotpwn.txt:

`/image?filename=%2e%2e%252f%2e%2e%252f%2e%2e%252fetc%252fpasswd`

Задание выполнено.

Официальное решение:

`/image?filename=..%252f..%252f..%252fetc/passwd`

Смысл решения в том, что фильтруемая последовательность символов "../" URL-кодируется по технике "Double encoding":
1. Сначала "../" превращается в "..%2f"
2. Затем в "..%2f" символ процента кодируется в %25 и в итоге последовательность принимает значение "..%252f"

После этого можно также закодировать точки в %2e, но это роли не играет. После первого декодирования строка примет значение "..%2f", будет пропущена фильтром и превратится в "../".
