---
title: account.passwordSettings
description: Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info & so on)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.passwordSettings  
[Back to constructors index](index.md)



Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info & so on)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](../types/string.md) | Yes|[2FA Recovery email](https://core.telegram.org/api/srp#email-verification)|



### Type: [account\_PasswordSettings](../types/account_PasswordSettings.md)


### Example:

```php
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string'];
```  


Or, if you're into Lua:

```lua
account_passwordSettings={_='account.passwordSettings', email='string'}

```


