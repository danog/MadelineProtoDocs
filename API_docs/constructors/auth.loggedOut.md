# auth.loggedOut

> Future auth token » to be used on subsequent authorizations

[Back to constructors index](/API_docs/constructors/index.html)



[Future auth token »](https://core.telegram.org/api/auth#future-auth-tokens) to be used on subsequent authorizations

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|future\_auth\_token|[bytes](/API_docs/types/bytes.html) | Optional|[Future auth token »](https://core.telegram.org/api/auth#future-auth-tokens) to be used on subsequent authorizations|



### Type: [auth.LoggedOut](/API_docs/types/auth.LoggedOut.html)


### Example:

```
$auth_loggedOut = ['_' => 'auth.loggedOut', 'future_auth_token' => 'bytes'];
```
