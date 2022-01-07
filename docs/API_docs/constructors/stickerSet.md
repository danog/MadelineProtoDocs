---
title: "stickerSet"
description: "Represents a stickerset (stickerpack)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](/API_docs/constructors/index.md)



Represents a stickerset (stickerpack)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|archived|[Bool](/API_docs/types/Bool.md) | Optional|Whether this stickerset was archived (due to too many saved stickers in the current account)|
|official|[Bool](/API_docs/types/Bool.md) | Optional|Is this stickerset official|
|masks|[Bool](/API_docs/types/Bool.md) | Optional|Is this a mask stickerset|
|animated|[Bool](/API_docs/types/Bool.md) | Optional|Is this an animated stickerpack|
|installed\_date|[int](/API_docs/types/int.md) | Optional|When was this stickerset installed|
|id|[long](/API_docs/types/long.md) | Yes|ID of the stickerset|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash of stickerset|
|title|[string](/API_docs/types/string.md) | Yes|Title of stickerset|
|short\_name|[string](/API_docs/types/string.md) | Yes|Short name of stickerset to use in `tg://addstickers?set=short_name`|
|thumbs|Array of [PhotoSize](/API_docs/types/PhotoSize.md) | Optional|
|thumb\_dc\_id|[int](/API_docs/types/int.md) | Optional|DC ID of thumbnail|
|thumb\_version|[int](/API_docs/types/int.md) | Optional|
|count|[int](/API_docs/types/int.md) | Yes|Number of stickers in pack|
|hash|[int](/API_docs/types/int.md) | Yes|



### Type: [StickerSet](/API_docs/types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'animated' => Bool, 'installed_date' => int, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'thumbs' => [PhotoSize, PhotoSize], 'thumb_dc_id' => int, 'thumb_version' => int, 'count' => int, 'hash' => int];
```  
