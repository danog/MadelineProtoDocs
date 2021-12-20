---
title: "auth.passwordRecovery"
description: "Recovery info of a 2FA password, only for accounts with a recovery email configured."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_passwordRecovery.html
---
# Constructor: auth.passwordRecovery  
[Back to constructors index](index.md)



Recovery info of a [2FA password](https://core.telegram.org/api/srp), only for accounts with a [recovery email configured](https://core.telegram.org/api/srp#email-verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](../types/string.md) | Yes|The email to which the recovery code was sent must match this [pattern](https://core.telegram.org/api/pattern).|



### Type: [auth.PasswordRecovery](../types/auth.PasswordRecovery.md)


### Example:

```php
$auth_passwordRecovery = ['_' => 'auth.passwordRecovery', 'email_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
auth_passwordRecovery={_='auth.passwordRecovery', email_pattern='string'}

```


