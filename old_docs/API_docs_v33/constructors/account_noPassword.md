---
title: account.noPassword
description: No password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.noPassword  
[Back to constructors index](index.md)



No password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Yes|Email unconfirmed pattern|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_noPassword = ['_' => 'account.noPassword', 'new_salt' => 'bytes', 'email_unconfirmed_pattern' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.noPassword", "new_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}, "email_unconfirmed_pattern": "string"}
```


Or, if you're into Lua:

```lua
account_noPassword={_='account.noPassword', new_salt='bytes', email_unconfirmed_pattern='string'}

```


