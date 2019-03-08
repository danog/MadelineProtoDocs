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
|email|[string](../types/string.md) | Optional|Email|
|secure\_settings|[SecureSecretSettings](../types/SecureSecretSettings.md) | Optional|Secure settings|



### Type: [account\_PasswordSettings](../types/account_PasswordSettings.md)


### Example:

```php
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string', 'secure_settings' => SecureSecretSettings];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.passwordSettings", "email": "string", "secure_settings": SecureSecretSettings}
```


Or, if you're into Lua:

```lua
account_passwordSettings={_='account.passwordSettings', email='string', secure_settings=SecureSecretSettings}

```


