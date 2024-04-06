# SSRF
## Обход фильтрации
127.0.0.1 можно представить как `2130706433`, `017700000001`, `127.1` или `127.0.1`:
```
┌──(tinker㉿catpants)-[~/projects/codeby-wapt/07-ssrf]
└─$ ping 2130706433   
PING 2130706433 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.066 ms
^C
```
```
┌──(tinker㉿catpants)-[~/projects/codeby-wapt/07-ssrf]
└─$ ping 017700000001
PING 017700000001 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.033 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.055 ms
```
* Use an alternative IP representation of 127.0.0.1, such as 2130706433, 017700000001, or 127.1.
* Register your own domain name that resolves to 127.0.0.1. You can use spoofed.burpcollaborator.net for this purpose.
* Obfuscate blocked strings using URL encoding or case variation.
* Provide a URL that you control, which redirects to the target URL. Try using different redirect codes, as well as different protocols for the target URL. For example, switching from an http: to https: URL during the redirect has been shown to bypass some anti-SSRF filters.

### Double encoding
https://owasp.org/www-community/Double_Encoding


* `#` = `%23`
* `%` = `%25`
* `%2523`
