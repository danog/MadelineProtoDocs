---
title: "account.passwordSettings"
description: "Private info associated to the password info (recovery email, telegram passport info & so on)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_passwordSettings.html
---
# Constructor: account.passwordSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Private info associated to the password info (recovery email, telegram [passport](https://core.telegram.org/passport) info &amp; so on)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](/API_docs/types/string.html) | Optional|[2FA Recovery email](https://core.telegram.org/api/srp#email-verification)|
|secure\_settings|[SecureSecretSettings](/API_docs/types/SecureSecretSettings.html) | Optional|Telegram [passport](https://core.telegram.org/passport) settings|



### Type: [account.PasswordSettings](/API_docs/types/account.PasswordSettings.html)


### Example:

```
$account_passwordSettings = ['_' => 'account.passwordSettings', 'email' => 'string', 'secure_settings' => SecureSecretSettings];
```  
