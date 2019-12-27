---
title: account.passwordInputSettings
description: Settings for setting up a new password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.passwordInputSettings  
[Back to constructors index](index.md)



Settings for setting up a new password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Optional|The [SRP algorithm](https://core.telegram.org/api/srp) to use|
|new\_password\_hash|[bytes](../types/bytes.md) | Optional|The [computed password hash](https://core.telegram.org/api/srp)|
|hint|[string](../types/string.md) | Optional|Text hint for the password|
|email|[string](../types/string.md) | Optional|Password recovery email|
|new\_secure\_settings|[SecureSecretSettings](../types/SecureSecretSettings.md) | Optional|Telegram [passport](https://core.telegram.org/passport) settings|



### Type: [account.PasswordInputSettings](../types/account.PasswordInputSettings.md)


### Example:

```php
$account.passwordInputSettings = ['_' => 'account.passwordInputSettings', 'new_algo' => PasswordKdfAlgo, 'new_password_hash' => 'bytes', 'hint' => 'string', 'email' => 'string', 'new_secure_settings' => SecureSecretSettings];
```  


Or, if you're into Lua:

```lua
account.passwordInputSettings={_='account.passwordInputSettings', new_algo=PasswordKdfAlgo, new_password_hash='bytes', hint='string', email='string', new_secure_settings=SecureSecretSettings}

```


