---
title: auth.exportedAuthorization
description: auth_exportedAuthorization attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.exportedAuthorization  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|bytes|[bytes](../types/bytes.md) | Yes|



### Type: [auth\_ExportedAuthorization](../types/auth_ExportedAuthorization.md)


### Example:

```php
$auth_exportedAuthorization = ['_' => 'auth.exportedAuthorization', 'id' => int, 'bytes' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.exportedAuthorization", "id": int, "bytes": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
auth_exportedAuthorization={_='auth.exportedAuthorization', id=int, bytes='bytes'}

```


