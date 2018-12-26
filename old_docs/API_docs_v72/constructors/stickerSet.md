---
title: stickerSet
description: Sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](index.md)



Sticker set

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|installed|[Bool](../types/Bool.md) | Optional|Installed?|
|archived|[Bool](../types/Bool.md) | Optional|Archived?|
|official|[Bool](../types/Bool.md) | Optional|Official?|
|masks|[Bool](../types/Bool.md) | Optional|Masks?|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|short\_name|[string](../types/string.md) | Yes|Short name|
|count|[int](../types/int.md) | Yes|Count|
|hash|[int](../types/int.md) | Yes|Hash|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'installed' => Bool, 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'count' => int, 'hash' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "stickerSet", "installed": Bool, "archived": Bool, "official": Bool, "masks": Bool, "id": long, "access_hash": long, "title": "string", "short_name": "string", "count": int, "hash": int}
```


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', installed=Bool, archived=Bool, official=Bool, masks=Bool, id=long, access_hash=long, title='string', short_name='string', count=int, hash=int}

```


