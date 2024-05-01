---
title: "account.passwordInputSettings"
description: "Settings for setting up a new password"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_passwordInputSettings.html
---
# Constructor: account.passwordInputSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Settings for setting up a new password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_algo|[PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html) | Optional|The [SRP algorithm](https://core.telegram.org/api/srp) to use|
|new\_password\_hash|[bytes](/API_docs/types/bytes.html) | Optional|The [computed password hash](https://core.telegram.org/api/srp)|
|hint|[string](/API_docs/types/string.html) | Optional|Text hint for the password|
|email|[string](/API_docs/types/string.html) | Optional|Password recovery email|
|new\_secure\_settings|[SecureSecretSettings](/API_docs/types/SecureSecretSettings.html) | Optional|Telegram [passport](https://core.telegram.org/passport) settings|



### Type: [account.PasswordInputSettings](/API_docs/types/account.PasswordInputSettings.html)


### Example:

```
$account_passwordInputSettings = ['_' => 'account.passwordInputSettings', 'new_algo' => PasswordKdfAlgo, 'new_password_hash' => 'bytes', 'hint' => 'string', 'email' => 'string', 'new_secure_settings' => SecureSecretSettings];
```  
