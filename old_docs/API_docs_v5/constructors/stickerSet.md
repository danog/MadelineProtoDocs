---
title: stickerSet
description: Represents a stickerset (stickerpack)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](index.md)



Represents a stickerset (stickerpack)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID of the stickerset|
|access\_hash|[long](../types/long.md) | Yes|Access hash of stickerset|
|title|[string](../types/string.md) | Yes|Title of stickerset|
|short\_name|[string](../types/string.md) | Yes|Short name of stickerset to use in `tg://addstickers?set=short_name`|
|count|[int](../types/int.md) | Yes|Number of stickers in pack|
|hash|[int](../types/int.md) | Yes|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'count' => int, 'hash' => int];
```  


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', id=long, access_hash=long, title='string', short_name='string', count=int, hash=int}

```


