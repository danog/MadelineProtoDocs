# auth.loginTokenMigrateTo

> Repeat the query to the specified DC

[Back to constructors index](/API_docs/constructors/index.html)



Repeat the query to the specified DC

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID|
|token|[bytes](/API_docs/types/bytes.html) | Yes|Token to use for login|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.html)


### Example:

```
$auth_loginTokenMigrateTo = ['_' => 'auth.loginTokenMigrateTo', 'dc_id' => int, 'token' => 'bytes'];
```
