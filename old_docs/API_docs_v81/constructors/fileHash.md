---
title: fileHash
description: fileHash attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileHash  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|
|hash|[bytes](../types/bytes.md) | Yes|



### Type: [FileHash](../types/FileHash.md)


### Example:

```
$fileHash = ['_' => 'fileHash', 'offset' => int, 'limit' => int, 'hash' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "fileHash", "offset": int, "limit": int, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
fileHash={_='fileHash', offset=int, limit=int, hash='bytes'}

```


