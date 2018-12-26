---
title: account.tmpPassword
description: Tmp password
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.tmpPassword  
[Back to constructors index](index.md)



Tmp password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tmp\_password|[bytes](../types/bytes.md) | Yes|Tmp password|
|valid\_until|[int](../types/int.md) | Yes|Valid until|



### Type: [account\_TmpPassword](../types/account_TmpPassword.md)


### Example:

```php
$account_tmpPassword = ['_' => 'account.tmpPassword', 'tmp_password' => 'bytes', 'valid_until' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.tmpPassword", "tmp_password": {"_": "bytes", "bytes":"base64 encoded bytes"}, "valid_until": int}
```


Or, if you're into Lua:

```lua
account_tmpPassword={_='account.tmpPassword', tmp_password='bytes', valid_until=int}

```


