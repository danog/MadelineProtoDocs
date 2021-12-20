---
title: "photo"
description: "Photo"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photo  
[Back to constructors index](index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_stickers|[Bool](../types/Bool.md) | Optional|Whether the photo has mask stickers attached to it|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|[file reference](https://core.telegram.org/api/file_reference)|
|date|[int](../types/int.md) | Yes|Date of upload|
|sizes|Array of [PhotoSize](../types/PhotoSize.md) | Yes|Available sizes for download|
|video\_sizes|Array of [VideoSize](../types/VideoSize.md) | Optional|[For animated profiles](https://core.telegram.org/api/files#animated-profile-pictures), the MPEG4 videos|
|dc\_id|[int](../types/int.md) | Yes|DC ID to use for download|



### Type: [Photo](../types/Photo.md)


### Example:

```php
$photo = ['_' => 'photo', 'has_stickers' => Bool, 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'sizes' => [PhotoSize, PhotoSize], 'video_sizes' => [VideoSize, VideoSize], 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
photo={_='photo', has_stickers=Bool, id=long, access_hash=long, file_reference='bytes', date=int, sizes={PhotoSize}, video_sizes={VideoSize}, dc_id=int}

```


