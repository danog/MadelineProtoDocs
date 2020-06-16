---
title: cdnFileHash
description: cdnFileHash attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnFileHash  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|
|hash|[bytes](../types/bytes.md) | Yes|



### Type: [CdnFileHash](../types/CdnFileHash.md)


### Example:

```php
$cdnFileHash = ['_' => 'cdnFileHash', 'offset' => int, 'limit' => int, 'hash' => 'bytes'];
```  


Or, if you're into Lua:

```lua
cdnFileHash={_='cdnFileHash', offset=int, limit=int, hash='bytes'}

```


