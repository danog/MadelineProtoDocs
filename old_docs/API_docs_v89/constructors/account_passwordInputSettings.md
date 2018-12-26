---
title: account.passwordInputSettings
description: 2FA password settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.passwordInputSettings  
[Back to constructors index](index.md)



2FA password settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Optional|New algo|
|new\_password\_hash|[bytes](../types/bytes.md) | Optional|`hash('sha256', $new_salt.$new_password.$new_salt, true)`|
|hint|[string](../types/string.md) | Optional|Hint|
|email|[string](../types/string.md) | Optional|Email|
|new\_secure\_settings|[SecureSecretSettings](../types/SecureSecretSettings.md) | Optional|New secure settings|



### Type: [account\_PasswordInputSettings](../types/account_PasswordInputSettings.md)


### Example:

```php
$account_passwordInputSettings = ['_' => 'account.passwordInputSettings', 'new_algo' => PasswordKdfAlgo, 'new_password_hash' => 'bytes', 'hint' => 'string', 'email' => 'string', 'new_secure_settings' => SecureSecretSettings];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.passwordInputSettings", "new_algo": PasswordKdfAlgo, "new_password_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "hint": "string", "email": "string", "new_secure_settings": SecureSecretSettings}
```


Or, if you're into Lua:

```lua
account_passwordInputSettings={_='account.passwordInputSettings', new_algo=PasswordKdfAlgo, new_password_hash='bytes', hint='string', email='string', new_secure_settings=SecureSecretSettings}

```


