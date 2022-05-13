---
title: "stickerSet"
description: "Represents a stickerset (stickerpack)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a stickerset (stickerpack)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|archived|[Bool](/API_docs/types/Bool.html) | Optional|Whether this stickerset was archived (due to too many saved stickers in the current account)|
|official|[Bool](/API_docs/types/Bool.html) | Optional|Is this stickerset official|
|masks|[Bool](/API_docs/types/Bool.html) | Optional|Is this a mask stickerset|
|animated|[Bool](/API_docs/types/Bool.html) | Optional|Is this an animated stickerpack|
|videos|[Bool](/API_docs/types/Bool.html) | Optional|Is this a video stickerpack|
|installed\_date|[int](/API_docs/types/int.html) | Optional|When was this stickerset installed|
|id|[long](/API_docs/types/long.html) | Yes|ID of the stickerset|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of stickerset|
|title|[string](/API_docs/types/string.html) | Yes|Title of stickerset|
|short\_name|[string](/API_docs/types/string.html) | Yes|Short name of stickerset to use in `tg://addstickers?set=short_name`|
|thumbs|Array of [PhotoSize](/API_docs/types/PhotoSize.html) | Optional|Stickerset thumbnail|
|thumb\_dc\_id|[int](/API_docs/types/int.html) | Optional|DC ID of thumbnail|
|thumb\_version|[int](/API_docs/types/int.html) | Optional|Thumbnail version|
|count|[int](/API_docs/types/int.html) | Yes|Number of stickers in pack|
|hash|[int](/API_docs/types/int.html) | Yes|



### Type: [StickerSet](/API_docs/types/StickerSet.html)


### Example:

```
$stickerSet = ['_' => 'stickerSet', 'archived' => Bool, 'official' => Bool, 'masks' => Bool, 'animated' => Bool, 'videos' => Bool, 'installed_date' => int, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'thumbs' => [PhotoSize, PhotoSize], 'thumb_dc_id' => int, 'thumb_version' => int, 'count' => int, 'hash' => int];
```  
