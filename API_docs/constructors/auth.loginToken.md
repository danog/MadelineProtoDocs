# auth.loginToken

> Login token (for QR code login)

[Back to constructors index](/API_docs/constructors/index.html)



Login token (for [QR code login](https://core.telegram.org/api/qr-login))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.html) | Yes|Expiration date of QR code|
|token|[bytes](/API_docs/types/bytes.html) | Yes|Token to render in QR code|



### Type: [auth.LoginToken](/API_docs/types/auth.LoginToken.html)


### Example:

```
$auth_loginToken = ['_' => 'auth.loginToken', 'expires' => int, 'token' => 'bytes'];
```
