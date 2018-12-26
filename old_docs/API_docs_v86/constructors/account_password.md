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
|has\_password|[Bool](../types/Bool.md) | Optional|Has password?|
|current\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Optional|Current algo|
|srp\_B|[bytes](../types/bytes.md) | Optional|Srp b|
|srp\_id|[long](../types/long.md) | Optional|Srp ID|
|hint|[string](../types/string.md) | Optional|Hint|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Optional|Email unconfirmed pattern|
|new\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Yes|New algo|
|new\_secure\_algo|[SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md) | Yes|New secure algo|
|secure\_random|[bytes](../types/bytes.md) | Yes|Secure random|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'has_password' => Bool, 'current_algo' => PasswordKdfAlgo, 'srp_B' => 'bytes', 'srp_id' => long, 'hint' => 'string', 'email_unconfirmed_pattern' => 'string', 'new_algo' => PasswordKdfAlgo, 'new_secure_algo' => SecurePasswordKdfAlgo, 'secure_random' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.password", "has_recovery": Bool, "has_secure_values": Bool, "has_password": Bool, "current_algo": PasswordKdfAlgo, "srp_B": {"_": "bytes", "bytes":"base64 encoded bytes"}, "srp_id": long, "hint": "string", "email_unconfirmed_pattern": "string", "new_algo": PasswordKdfAlgo, "new_secure_algo": SecurePasswordKdfAlgo, "secure_random": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
account_password={_='account.password', has_recovery=Bool, has_secure_values=Bool, has_password=Bool, current_algo=PasswordKdfAlgo, srp_B='bytes', srp_id=long, hint='string', email_unconfirmed_pattern='string', new_algo=PasswordKdfAlgo, new_secure_algo=SecurePasswordKdfAlgo, secure_random='bytes'}

```


