---
title: fileHash
description: File hash
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileHash  
[Back to constructors index](index.md)



File hash

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|limit|[int](../types/int.md) | Yes|Limit|
|hash|[bytes](../types/bytes.md) | Yes|Hash|



### Type: [FileHash](../types/FileHash.md)


### Example:

```php
$fileHash = ['_' => 'fileHash', 'offset' => int, 'limit' => int, 'hash' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "fileHash", "offset": int, "limit": int, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
fileHash={_='fileHash', offset=int, limit=int, hash='bytes'}

```


