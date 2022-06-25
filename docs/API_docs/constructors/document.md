---
title: "document"
description: "Document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: document  
[Back to constructors index](/API_docs/constructors/index.html)



Document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Check sum, dependent on document ID|
|file\_reference|[bytes](/API_docs/types/bytes.html) | Yes|[File reference](https://core.telegram.org/api/file_reference)|
|date|[int](/API_docs/types/int.html) | Yes|Creation date|
|mime\_type|[string](/API_docs/types/string.html) | Yes|MIME type|
|size|[long](/API_docs/types/long.html) | Yes|
|thumbs|Array of [PhotoSize](/API_docs/types/PhotoSize.html) | Optional|Thumbnails|
|video\_thumbs|Array of [VideoSize](/API_docs/types/VideoSize.html) | Optional|Video thumbnails|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.html) | Yes|Attributes|



### Type: [Document](/API_docs/types/Document.html)


### Example:

```
$document = ['_' => 'document', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'mime_type' => 'string', 'size' => long, 'thumbs' => [PhotoSize, PhotoSize], 'video_thumbs' => [VideoSize, VideoSize], 'dc_id' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
