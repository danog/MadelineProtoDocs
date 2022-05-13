---
title: "decryptedMessageMediaDocument"
description: "Document attached to a message in a secret chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_8  
[Back to constructors index](/API_docs/constructors/index.html)



Document attached to a message in a secret chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](/API_docs/types/bytes.html) | Yes|Thumbnail-file contents (JPEG-file, quality 55, set in a 90x90 square)|
|thumb\_w|[int](/API_docs/types/int.html) | Yes|Thumbnail width|
|thumb\_h|[int](/API_docs/types/int.html) | Yes|Thumbnail height|
|file\_name|[string](/API_docs/types/string.html) | Yes|
|mime\_type|[string](/API_docs/types/string.html) | Yes|File MIME-type|
|size|[int](/API_docs/types/int.html) | Yes|Document size|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaDocument_8 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'file_name' => 'string', 'mime_type' => 'string', 'size' => int];
```  
