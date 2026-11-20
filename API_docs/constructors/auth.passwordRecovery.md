# auth.passwordRecovery

> Recovery info of a 2FA password, only for accounts with a recovery email configured.

[Back to constructors index](/API_docs/constructors/index.html)



Recovery info of a [2FA password](https://core.telegram.org/api/srp), only for accounts with a [recovery email configured](https://core.telegram.org/api/srp#email-verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](/API_docs/types/string.html) | Yes|The email to which the recovery code was sent must match this [pattern](https://core.telegram.org/api/pattern).|



### Type: [auth.PasswordRecovery](/API_docs/types/auth.PasswordRecovery.html)


### Example:

```
$auth_passwordRecovery = ['_' => 'auth.passwordRecovery', 'email_pattern' => 'string'];
```
