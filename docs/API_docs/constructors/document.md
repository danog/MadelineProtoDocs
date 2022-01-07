---
title: "document"
description: "Document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: document  
[Back to constructors index](/API_docs/constructors/index.md)



Document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Check sum, dependant on document ID|
|file\_reference|[bytes](/API_docs/types/bytes.md) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|date|[int](/API_docs/types/int.md) | Yes|Creation date|
|mime\_type|[string](/API_docs/types/string.md) | Yes|MIME type|
|size|[int](/API_docs/types/int.md) | Yes|Size|
|thumbs|Array of [PhotoSize](/API_docs/types/PhotoSize.md) | Optional|Thumbnails|
|video\_thumbs|Array of [VideoSize](/API_docs/types/VideoSize.md) | Optional|Video thumbnails|
|dc\_id|[int](/API_docs/types/int.md) | Yes|DC ID|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.md) | Yes|Attributes|



### Type: [Document](/API_docs/types/Document.md)


### Example:

```php
$document = ['_' => 'document', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'mime_type' => 'string', 'size' => int, 'thumbs' => [PhotoSize, PhotoSize], 'video_thumbs' => [VideoSize, VideoSize], 'dc_id' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
