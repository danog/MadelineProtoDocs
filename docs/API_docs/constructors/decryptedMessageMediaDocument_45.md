---
title: "decryptedMessageMediaDocument"
description: "Document attached to a message in a secret chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_45  
[Back to constructors index](/API_docs/constructors/index.md)



Document attached to a message in a secret chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](/API_docs/types/bytes.md) | Yes|Thumbnail-file contents (JPEG-file, quality 55, set in a 90x90 square)|
|thumb\_w|[int](/API_docs/types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](/API_docs/types/int.md) | Yes|Thumbnail height|
|mime\_type|[string](/API_docs/types/string.md) | Yes|File MIME-type|
|size|[int](/API_docs/types/int.md) | Yes|Document size|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.md) | Yes|Document attributes for media types|
|caption|[string](/API_docs/types/string.md) | Yes|Caption|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaDocument_45 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'mime_type' => 'string', 'size' => int, 'attributes' => [DocumentAttribute, DocumentAttribute], 'caption' => 'string'];
```  
