---
title: "decryptedMessageMediaPhoto"
description: "Photo attached to an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaPhoto\_45  
[Back to constructors index](/API_docs/constructors/index.html)



Photo attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](/API_docs/types/bytes.html) | Yes|Content of thumbnail file (JPEGfile, quality 55, set in a square 90x90)|
|thumb\_w|[int](/API_docs/types/int.html) | Yes|Thumbnail width|
|thumb\_h|[int](/API_docs/types/int.html) | Yes|Thumbnail height|
|w|[int](/API_docs/types/int.html) | Yes|Photo width|
|h|[int](/API_docs/types/int.html) | Yes|Photo height|
|size|[int](/API_docs/types/int.html) | Yes|Size of the photo in bytes|
|caption|[string](/API_docs/types/string.html) | Yes|Caption|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaPhoto_45 = ['_' => 'decryptedMessageMediaPhoto', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'w' => int, 'h' => int, 'size' => int, 'caption' => 'string'];
```  
