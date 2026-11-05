# auth.sentCodeSuccess

> The user successfully authorized using future auth tokens

[Back to constructors index](/API_docs/constructors/index.html)



The user successfully authorized using [future auth tokens](https://core.telegram.org/api/auth#future-auth-tokens)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization|[auth.Authorization](/API_docs/constructors/auth.Authorization.html) | Yes|Authorization info|



### Type: [auth.SentCode](/API_docs/types/auth.SentCode.html)


### Example:

```
$auth_sentCodeSuccess = ['_' => 'auth.sentCodeSuccess', 'authorization' => auth.Authorization];
```
