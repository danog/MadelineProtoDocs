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
|current\_salt|[bytes](../types/bytes.md) | Yes|Current salt|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|hint|[string](../types/string.md) | Yes|Text hint for the password|
|has\_recovery|[Bool](../types/Bool.md) | Yes|Has recovery?|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|A [password recovery email](https://core.telegram.org/api/srp#email-verification) with the specified [pattern](https://core.telegram.org/api/pattern) is still awaiting verification|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account.password = ['_' => 'account.password', 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'hint' => 'string', 'has_recovery' => Bool, 'email_unconfirmed_pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
account.password={_='account.password', current_salt='bytes', new_salt='bytes', hint='string', has_recovery=Bool, email_unconfirmed_pattern='string'}

```


