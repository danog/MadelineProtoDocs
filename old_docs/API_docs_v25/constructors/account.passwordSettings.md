---
title: account.passwordSettings
description: Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_passwordSettings.html
---
# Constructor: account.passwordSettings  
[Back to constructors index](index.md)



Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](../types/string.md) | Yes|[2FA Recovery email](https://core.telegram.org/api/srp#email-verification)|
|secure\_salt|[bytes](../types/bytes.md) | Yes|
|secure\_secret|[bytes](../types/bytes.md) | Yes|
|secure\_secret\_id|[long](../types/long.md) | Yes|



### Type: [account.PasswordSettings](../types/account.PasswordSettings.md)


### Example:

```php
$account.passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string', 'secure_salt' => 'bytes', 'secure_secret' => 'bytes', 'secure_secret_id' => long];
```  


Or, if you're into Lua:

```lua
account.passwordSettings={_='account.passwordSettings', email='string', secure_salt='bytes', secure_secret='bytes', secure_secret_id=long}

```


