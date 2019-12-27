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
|archived|[Bool](../types/Bool.md) | Optional|Whether this stickerset was archived (due to too many saved stickers in the current account)|
|official|[Bool](../types/Bool.md) | Optional|Is this stickerset official|
|masks|[Bool](../types/Bool.md) | Optional|Is this a mask stickerset|
|installed\_date|[int](../types/int.md) | Optional|When was this stickerset installed|
|id|[long](../types/long.md) | Yes|ID of the stickerset|
|access\_hash|[long](../types/long.md) | Yes|Access hash of stickerset|
|title|[string](../types/string.md) | Yes|Title of stickerset|
|short\_name|[string](../types/string.md) | Yes|Short name of stickerset to use in `tg://addstickers?set=short_name`|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|Thumbnail for stickerset|
|thumb\_dc\_id|[int](../types/int.md) | Optional|DC ID of thumbnail|
|count|[int](../types/int.md) | Yes|Number of stickers in pack|
|hash|[int](../types/int.md) | Yes|Hash|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'installed_date' => int, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'thumb' => PhotoSize, 'thumb_dc_id' => int, 'count' => int, 'hash' => int];
```  


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', archived=Bool, official=Bool, masks=Bool, installed_date=int, id=long, access_hash=long, title='string', short_name='string', thumb=PhotoSize, thumb_dc_id=int, count=int, hash=int}

```


