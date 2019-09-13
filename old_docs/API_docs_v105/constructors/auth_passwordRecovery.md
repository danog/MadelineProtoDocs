---
title: auth.passwordRecovery
description: Password recovery
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.passwordRecovery  
[Back to constructors index](index.md)



Password recovery

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](../types/string.md) | Yes|Email pattern|



### Type: [auth\_PasswordRecovery](../types/auth_PasswordRecovery.md)


### Example:

```php
$auth_passwordRecovery = ['_' => 'auth.passwordRecovery', 'email_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
auth_passwordRecovery={_='auth.passwordRecovery', email_pattern='string'}

```


