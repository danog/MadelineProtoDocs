---
title: secureFile
description: Secure file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureFile  
[Back to constructors index](index.md)



Secure file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|size|[int](../types/int.md) | Yes|Size|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|date|[int](../types/int.md) | Yes|Date|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [SecureFile](../types/SecureFile.md)


### Example:

```php
$secureFile = ['_' => 'secureFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'date' => int, 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureFile={_='secureFile', id=long, access_hash=long, size=int, dc_id=int, date=int, file_hash='bytes', secret='bytes'}

```


