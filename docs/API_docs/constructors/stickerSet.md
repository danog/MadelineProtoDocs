---
title: stickerSet
description: stickerSet attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|archived|[Bool](../types/Bool.md) | Optional|
|official|[Bool](../types/Bool.md) | Optional|
|masks|[Bool](../types/Bool.md) | Optional|
|installed\_date|[int](../types/int.md) | Optional|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|title|[string](../types/string.md) | Yes|
|short\_name|[string](../types/string.md) | Yes|
|count|[int](../types/int.md) | Yes|
|hash|[int](../types/int.md) | Yes|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'installed_date' => int, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'count' => int, 'hash' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "stickerSet", "archived": Bool, "official": Bool, "masks": Bool, "installed_date": int, "id": long, "access_hash": long, "title": "string", "short_name": "string", "count": int, "hash": int}
```


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', archived=Bool, official=Bool, masks=Bool, installed_date=int, id=long, access_hash=long, title='string', short_name='string', count=int, hash=int}

```


