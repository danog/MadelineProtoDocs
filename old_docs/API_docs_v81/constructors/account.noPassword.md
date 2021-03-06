---
title: account.noPassword
description: No password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_noPassword.html
---
# Constructor: account.noPassword  
[Back to constructors index](index.md)



No password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|new\_secure\_salt|[bytes](../types/bytes.md) | Yes|New secure salt|
|secure\_random|[bytes](../types/bytes.md) | Yes|Secure random|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|Email unconfirmed pattern|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account.noPassword = ['_' => 'account.noPassword', 'new_salt' => 'bytes', 'new_secure_salt' => 'bytes', 'secure_random' => 'bytes', 'email_unconfirmed_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
account.noPassword={_='account.noPassword', new_salt='bytes', new_secure_salt='bytes', secure_random='bytes', email_unconfirmed_pattern='string'}

```


