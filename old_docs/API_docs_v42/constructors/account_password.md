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
|current\_salt|[bytes](../types/bytes.md) | Yes|Current salt|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|hint|[string](../types/string.md) | Yes|Hint|
|has\_recovery|[Bool](../types/Bool.md) | Yes|Has recovery?|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|Email unconfirmed pattern|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'hint' => 'string', 'has_recovery' => Bool, 'email_unconfirmed_pattern' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.password", "current_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "new_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "hint": "string", "has_recovery": Bool, "email_unconfirmed_pattern": "string"}
```


Or, if you're into Lua:

```lua
account_password={_='account.password', current_salt='bytes', new_salt='bytes', hint='string', has_recovery=Bool, email_unconfirmed_pattern='string'}

```


