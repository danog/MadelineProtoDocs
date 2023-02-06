---
title: "videoSizeStickerMarkup"
description: "videoSizeStickerMarkup attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSizeStickerMarkup  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|
|sticker\_id|[long](/API_docs/types/long.html) | Yes|
|background\_colors|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [VideoSize](/API_docs/types/VideoSize.html)


### Example:

```
$videoSizeStickerMarkup = ['_' => 'videoSizeStickerMarkup', 'stickerset' => InputStickerSet, 'sticker_id' => long, 'background_colors' => [int, int]];
```  
