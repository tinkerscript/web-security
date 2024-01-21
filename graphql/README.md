# GraphQL

## POST to GET

POST body:
```json
{
    "query": "query {__schema{types{name}}}",
    "variables": {},
    "operationName": null
}
```

GET request:
`/graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D`
