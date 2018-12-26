---
title: account.passwordSettings
description: Password settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.passwordSettings  
[Back to constructors index](index.md)



Password settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](../types/string.md) | Yes|Email|



### Type: [account\_PasswordSettings](../types/account_PasswordSettings.md)


### Example:

```php
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.passwordSettings", "email": "string"}
```


Or, if you're into Lua:

```lua
account_passwordSettings={_='account.passwordSettings', email='string'}

```


