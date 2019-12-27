---
title: account.password
description: Configuration for two-factor authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.password  
[Back to constructors index](index.md)



Configuration for two-factor authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_recovery|[Bool](../types/Bool.md) | Optional|Whether the user has a recovery method configured|
|has\_secure\_values|[Bool](../types/Bool.md) | Optional|Whether telegram [passport](https://core.telegram.org/passport) is enabled|
|current\_salt|[bytes](../types/bytes.md) | Yes|Current salt|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|new\_secure\_salt|[bytes](../types/bytes.md) | Yes|New secure salt|
|secure\_random|[bytes](../types/bytes.md) | Yes|Secure random string|
|hint|[string](../types/string.md) | Yes|Text hint for the password|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|A [password recovery email](https://core.telegram.org/api/srp#email-verification) with the specified [pattern](https://core.telegram.org/api/pattern) is still awaiting verification|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account.password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'new_secure_salt' => 'bytes', 'secure_random' => 'bytes', 'hint' => 'string', 'email_unconfirmed_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
account.password={_='account.password', has_recovery=Bool, has_secure_values=Bool, current_salt='bytes', new_salt='bytes', new_secure_salt='bytes', secure_random='bytes', hint='string', email_unconfirmed_pattern='string'}

```


