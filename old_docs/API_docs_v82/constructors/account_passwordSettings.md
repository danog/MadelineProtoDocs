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
|secure\_salt|[bytes](../types/bytes.md) | Yes|Secure salt|
|secure\_secret|[bytes](../types/bytes.md) | Yes|Secure secret|
|secure\_secret\_id|[long](../types/long.md) | Yes|Secure secret ID|



### Type: [account\_PasswordSettings](../types/account_PasswordSettings.md)


### Example:

```php
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string', 'secure_salt' => 'bytes', 'secure_secret' => 'bytes', 'secure_secret_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.passwordSettings", "email": "string", "secure_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secure_secret": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secure_secret_id": long}
```


Or, if you're into Lua:

```lua
account_passwordSettings={_='account.passwordSettings', email='string', secure_salt='bytes', secure_secret='bytes', secure_secret_id=long}

```


