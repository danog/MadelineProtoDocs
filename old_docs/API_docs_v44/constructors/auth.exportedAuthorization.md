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
|id|[int](../types/int.md) | Yes|Current user identifier|
|bytes|[bytes](../types/bytes.md) | Yes|Authorizes key|



### Type: [auth.ExportedAuthorization](../types/auth.ExportedAuthorization.md)


### Example:

```php
$auth.exportedAuthorization = ['_' => 'auth.exportedAuthorization', 'id' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth.exportedAuthorization={_='auth.exportedAuthorization', id=int, bytes='bytes'}

```


