---
title: cdnFileHash
description: CDN file hash
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnFileHash  
[Back to constructors index](index.md)



CDN file hash

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset|
|limit|[int](../types/int.md) | Yes|Limit|
|hash|[bytes](../types/bytes.md) | Yes|Hash|



### Type: [CdnFileHash](../types/CdnFileHash.md)


### Example:

```php
$cdnFileHash = ['_' => 'cdnFileHash', 'offset' => int, 'limit' => int, 'hash' => 'bytes'];
```  


Or, if you're into Lua:

```lua
cdnFileHash={_='cdnFileHash', offset=int, limit=int, hash='bytes'}

```


