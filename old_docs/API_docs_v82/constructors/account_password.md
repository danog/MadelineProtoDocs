---
title: account.password
description: Password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.password  
[Back to constructors index](index.md)



Password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_recovery|[Bool](../types/Bool.md) | Optional|Has recovery?|
|has\_secure\_values|[Bool](../types/Bool.md) | Optional|Has secure values?|
|current\_salt|[bytes](../types/bytes.md) | Yes|Current salt|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|new\_secure\_salt|[bytes](../types/bytes.md) | Yes|New secure salt|
|secure\_random|[bytes](../types/bytes.md) | Yes|Secure random|
|hint|[string](../types/string.md) | Yes|Hint|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|Email unconfirmed pattern|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'new_secure_salt' => 'bytes', 'secure_random' => 'bytes', 'hint' => 'string', 'email_unconfirmed_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
account_password={_='account.password', has_recovery=Bool, has_secure_values=Bool, current_salt='bytes', new_salt='bytes', new_secure_salt='bytes', secure_random='bytes', hint='string', email_unconfirmed_pattern='string'}

```


