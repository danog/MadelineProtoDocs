---
title: "photo"
description: "Photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photo  
[Back to constructors index](/API_docs/constructors/index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_stickers|[Bool](/API_docs/types/Bool.md) | Optional|Whether the photo has mask stickers attached to it|
|id|[long](/API_docs/types/long.md) | Yes|ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[file reference](https://core.telegram.org/api/file_reference)|
|date|[int](/API_docs/types/int.md) | Yes|Date of upload|
|sizes|Array of [PhotoSize](/API_docs/types/PhotoSize.md) | Yes|Available sizes for download|
|video\_sizes|Array of [VideoSize](/API_docs/types/VideoSize.md) | Optional|[For animated profiles](https://core.telegram.org/api/files#animated-profile-pictures), the MPEG4 videos|
|dc\_id|[int](/API_docs/types/int.md) | Yes|DC ID to use for download|



### Type: [Photo](/API_docs/types/Photo.md)


### Example:

```php
$photo = ['_' => 'photo', 'has_stickers' => Bool, 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'sizes' => [PhotoSize, PhotoSize], 'video_sizes' => [VideoSize, VideoSize], 'dc_id' => int];
```  
