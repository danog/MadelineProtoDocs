---
title: "decryptedMessageMediaVideo"
description: "Video attached to an encrypted message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVideo\_8  
[Back to constructors index](/API_docs/constructors/index.html)



Video attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](/API_docs/types/bytes.html) | Yes|Content of thumbnail file (JPEG file, quality 55, set in a square 90x90)|
|thumb\_w|[int](/API_docs/types/int.html) | Yes|Thumbnail width|
|thumb\_h|[int](/API_docs/types/int.html) | Yes|Thumbnail height|
|duration|[int](/API_docs/types/int.html) | Yes|Duration of video in seconds|
|w|[int](/API_docs/types/int.html) | Yes|Image width|
|h|[int](/API_docs/types/int.html) | Yes|Image height|
|size|[int](/API_docs/types/int.html) | Yes|File size|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaVideo_8 = ['_' => 'decryptedMessageMediaVideo', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'duration' => int, 'w' => int, 'h' => int, 'size' => int];
```  
