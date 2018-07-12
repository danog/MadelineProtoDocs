---
title: secureFile
description: secureFile attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureFile  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|size|[int](../types/int.md) | Yes|
|dc\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|file\_hash|[bytes](../types/bytes.md) | Yes|
|secret|[bytes](../types/bytes.md) | Yes|



### Type: [SecureFile](../types/SecureFile.md)


### Example:

```
$secureFile = ['_' => 'secureFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'date' => int, 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureFile", "id": long, "access_hash": long, "size": int, "dc_id": int, "date": int, "file_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secret": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
secureFile={_='secureFile', id=long, access_hash=long, size=int, dc_id=int, date=int, file_hash='bytes', secret='bytes'}

```


