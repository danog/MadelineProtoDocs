---
title: "fileHash"
description: "SHA256 Hash of an uploaded file, to be checked for validity after download"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileHash  
[Back to constructors index](index.md)



SHA256 Hash of an uploaded file, to be checked for validity after download

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset from where to start computing SHA-256 hash|
|limit|[int](../types/int.md) | Yes|Length|
|hash|[bytes](../types/bytes.md) | Yes|SHA-256 Hash of file chunk, to be checked for validity after download|



### Type: [FileHash](../types/FileHash.md)


### Example:

```php
$fileHash = ['_' => 'fileHash', 'offset' => int, 'limit' => int, 'hash' => 'bytes'];
```  


Or, if you're into Lua:

```lua
fileHash={_='fileHash', offset=int, limit=int, hash='bytes'}

```


