---
title: "account.passwordSettings"
description: "Private info associated to the password info (recovery email, telegram passport info & so on)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_passwordSettings.html
---
# Constructor: account.passwordSettings  
[Back to constructors index](index.md)



Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](../types/string.md) | Optional|[2FA Recovery email](https://core.telegram.org/api/srp#email-verification)|
|secure\_settings|[SecureSecretSettings](../types/SecureSecretSettings.md) | Optional|Telegram [passport](https://core.telegram.org/passport) settings|



### Type: [account.PasswordSettings](../types/account.PasswordSettings.md)


### Example:

```php
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string', 'secure_settings' => SecureSecretSettings];
```  


Or, if you're into Lua:

```lua
account_passwordSettings={_='account.passwordSettings', email='string', secure_settings=SecureSecretSettings}

```


