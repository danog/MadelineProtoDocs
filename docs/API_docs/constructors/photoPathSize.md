---
title: "photoPathSize"
description: "Messages with animated stickers can have a compressed svg (< 300 bytes) to show the outline of the sticker before fetching the actual lottie animation."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoPathSize  
[Back to constructors index](/API_docs/constructors/index.html)



Messages with animated stickers can have a compressed svg (&lt; 300 bytes) to show the outline of the sticker before fetching the actual lottie animation.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.html) | Yes|Always `j`|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|Compressed SVG path payload, [see here for decompression instructions](https://core.telegram.org/api/files#vector-thumbnails)|



### Type: [PhotoSize](/API_docs/types/PhotoSize.html)


### Example:

```
$photoPathSize = ['_' => 'photoPathSize', 'type' => 'string', 'bytes' => 'bytes'];
```  
