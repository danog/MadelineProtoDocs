---
title: auth.exportedAuthorization
description: Exported authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.exportedAuthorization  
[Back to constructors index](index.md)



Exported authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



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


