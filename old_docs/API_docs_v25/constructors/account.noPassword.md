---
title: account.noPassword
description: account.noPassword attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_noPassword.html
---
# Constructor: account.noPassword  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|new\_salt|[bytes](../types/bytes.md) | Yes|
|new\_secure\_salt|[bytes](../types/bytes.md) | Yes|
|secure\_random|[bytes](../types/bytes.md) | Yes|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account_noPassword = ['_' => 'account.noPassword', 'new_salt' => 'bytes', 'new_secure_salt' => 'bytes', 'secure_random' => 'bytes', 'email_unconfirmed_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
account_noPassword={_='account.noPassword', new_salt='bytes', new_secure_salt='bytes', secure_random='bytes', email_unconfirmed_pattern='string'}

```


