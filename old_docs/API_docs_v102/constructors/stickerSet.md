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
|archived|[Bool](../types/Bool.md) | Optional|Archived?|
|official|[Bool](../types/Bool.md) | Optional|Official?|
|masks|[Bool](../types/Bool.md) | Optional|Masks?|
|animated|[Bool](../types/Bool.md) | Optional|Animated stickerset?|
|installed\_date|[int](../types/int.md) | Optional|Installed date|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|short\_name|[string](../types/string.md) | Yes|Short name|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|Thumbnail|
|thumb\_dc\_id|[int](../types/int.md) | Optional|DC ID|
|count|[int](../types/int.md) | Yes|Count|
|hash|[int](../types/int.md) | Yes|Hash|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'animated' => Bool, 'installed_date' => int, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'thumb' => PhotoSize, 'thumb_dc_id' => int, 'count' => int, 'hash' => int];
```  


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', archived=Bool, official=Bool, masks=Bool, animated=Bool, installed_date=int, id=long, access_hash=long, title='string', short_name='string', thumb=PhotoSize, thumb_dc_id=int, count=int, hash=int}

```


