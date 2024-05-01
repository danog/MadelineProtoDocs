---
title: "decryptedMessageMediaDocument"
description: "Document attached to a message in a secret chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_143  
[Back to constructors index](/API_docs/constructors/index.html)



Document attached to a message in a secret chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](/API_docs/types/bytes.html) | Yes|Thumbnail-file contents (JPEG-file, quality 55, set in a 90x90 square)|
|thumb\_w|[int](/API_docs/types/int.html) | Yes|Thumbnail width|
|thumb\_h|[int](/API_docs/types/int.html) | Yes|Thumbnail height|
|mime\_type|[string](/API_docs/types/string.html) | Yes|File MIME-type|
|size|[long](/API_docs/types/long.html) | Yes|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.html) | Yes|Document attributes for media types|
|caption|[string](/API_docs/types/string.html) | Yes|Caption|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaDocument_143 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'mime_type' => 'string', 'size' => long, 'attributes' => [DocumentAttribute, DocumentAttribute], 'caption' => 'string'];
```  
