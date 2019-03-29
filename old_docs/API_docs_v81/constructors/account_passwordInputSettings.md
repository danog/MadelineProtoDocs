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
|new\_salt|[bytes](../types/bytes.md) | Optional|`$new_salt = $MadelineProto->account->getPassword()['new_salt'].$MadelineProto->random(8);`|
|new\_password\_hash|[bytes](../types/bytes.md) | Optional|`hash('sha256', $new_salt.$new_password.$new_salt, true)`|
|hint|[string](../types/string.md) | Optional|Hint|
|email|[string](../types/string.md) | Optional|Email|
|new\_secure\_salt|[bytes](../types/bytes.md) | Optional|New secure salt|
|new\_secure\_secret|[bytes](../types/bytes.md) | Optional|New secure secret|
|new\_secure\_secret\_id|[long](../types/long.md) | Optional|New secure secret ID|



### Type: [account\_PasswordInputSettings](../types/account_PasswordInputSettings.md)


### Example:

```php
$account_passwordInputSettings = ['_' => 'account.passwordInputSettings', 'new_salt' => 'bytes', 'new_password_hash' => 'bytes', 'hint' => 'string', 'email' => 'string', 'new_secure_salt' => 'bytes', 'new_secure_secret' => 'bytes', 'new_secure_secret_id' => long];
```  


Or, if you're into Lua:

```lua
account_passwordInputSettings={_='account.passwordInputSettings', new_salt='bytes', new_password_hash='bytes', hint='string', email='string', new_secure_salt='bytes', new_secure_secret='bytes', new_secure_secret_id=long}

```


