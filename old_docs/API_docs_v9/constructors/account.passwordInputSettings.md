---
title: account.passwordInputSettings
description: Settings for setting up a new password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_passwordInputSettings.html
---
# Constructor: account.passwordInputSettings  
[Back to constructors index](index.md)



Settings for setting up a new password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_salt|[bytes](../types/bytes.md) | Optional|
|new\_password\_hash|[bytes](../types/bytes.md) | Optional|The [computed password hash](https://core.telegram.org/api/srp)|
|hint|[string](../types/string.md) | Optional|Text hint for the password|
|email|[string](../types/string.md) | Optional|Password recovery email|



### Type: [account.PasswordInputSettings](../types/account.PasswordInputSettings.md)


### Example:

```php
$account_passwordInputSettings = ['_' => 'account.passwordInputSettings', 'new_salt' => 'bytes', 'new_password_hash' => 'bytes', 'hint' => 'string', 'email' => 'string'];
```  


Or, if you're into Lua:

```lua
account_passwordInputSettings={_='account.passwordInputSettings', new_salt='bytes', new_password_hash='bytes', hint='string', email='string'}

```


