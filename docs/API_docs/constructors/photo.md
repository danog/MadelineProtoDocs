---
title: "photo"
description: "Photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photo  
[Back to constructors index](/API_docs/constructors/index.html)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_stickers|[Bool](/API_docs/types/Bool.html) | Optional|Whether the photo has mask stickers attached to it|
|id|[long](/API_docs/types/long.html) | Yes|ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|[file reference](https://core.telegram.org/api/file_reference)|
|date|[int](/API_docs/types/int.html) | Yes|Date of upload|
|sizes|Array of [PhotoSize](/API_docs/types/PhotoSize.html) | Yes|Available sizes for download|
|video\_sizes|Array of [VideoSize](/API_docs/types/VideoSize.html) | Optional|[For animated profiles](https://core.telegram.org/api/files#animated-profile-pictures), the MPEG4 videos|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID to use for download|



### Type: [Photo](/API_docs/types/Photo.html)


### Example:

```
$photo = ['_' => 'photo', 'has_stickers' => Bool, 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'sizes' => [PhotoSize, PhotoSize], 'video_sizes' => [VideoSize, VideoSize], 'dc_id' => int];
```  
