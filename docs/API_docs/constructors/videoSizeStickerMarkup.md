---
title: "videoSizeStickerMarkup"
description: "An animated profile picture based on a sticker."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSizeStickerMarkup  
[Back to constructors index](/API_docs/constructors/index.html)



An [animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) based on a [sticker](https://core.telegram.org/api/stickers).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|Stickerset|
|sticker\_id|[long](/API_docs/types/long.html) | Yes|Sticker ID|
|background\_colors|Array of [int](/API_docs/types/int.html) | Yes|1, 2, 3 or 4 RBG-24 colors used to generate a solid (1), gradient (2) or freeform gradient (3, 4) background, similar to how [fill wallpapers](https://core.telegram.org/api/wallpapers#fill-types) are generated. The rotation angle for gradient backgrounds is 0.|



### Type: [VideoSize](/API_docs/types/VideoSize.html)


### Example:

```
$videoSizeStickerMarkup = ['_' => 'videoSizeStickerMarkup', 'stickerset' => InputStickerSet, 'sticker_id' => long, 'background_colors' => [int, int]];
```  
