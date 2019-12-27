---
title: auth.exportedAuthorization
description: Data for copying of authorization between data centres.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.exportedAuthorization  
[Back to constructors index](index.md)



Data for copying of authorization between data centres.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|current user identifier|
|bytes|[bytes](../types/bytes.md) | Yes|authorizes key|



### Type: [auth\_ExportedAuthorization](../types/auth_ExportedAuthorization.md)


### Example:

```php
$auth_exportedAuthorization = ['_' => 'auth.exportedAuthorization', 'id' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth_exportedAuthorization={_='auth.exportedAuthorization', id=int, bytes='bytes'}

```


