---
title: account.password
description: account_password attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.password  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|has\_recovery|[Bool](../types/Bool.md) | Optional|
|has\_secure\_values|[Bool](../types/Bool.md) | Optional|
|current\_salt|[bytes](../types/bytes.md) | Yes|
|new\_salt|[bytes](../types/bytes.md) | Yes|
|new\_secure\_salt|[bytes](../types/bytes.md) | Yes|
|secure\_random|[bytes](../types/bytes.md) | Yes|
|hint|[string](../types/string.md) | Yes|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'new_secure_salt' => 'bytes', 'secure_random' => 'bytes', 'hint' => 'string', 'email_unconfirmed_pattern' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.password", "has_recovery": Bool, "has_secure_values": Bool, "current_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "new_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "new_secure_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secure_random": {"_": "bytes", "bytes":"base64 encoded bytes"}, "hint": "string", "email_unconfirmed_pattern": "string"}
```


Or, if you're into Lua:

```lua
account_password={_='account.password', has_recovery=Bool, has_secure_values=Bool, current_salt='bytes', new_salt='bytes', new_secure_salt='bytes', secure_random='bytes', hint='string', email_unconfirmed_pattern='string'}

```


