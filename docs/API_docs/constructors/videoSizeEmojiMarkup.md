---
title: "videoSizeEmojiMarkup"
description: "An animated profile picture based on a custom emoji sticker."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSizeEmojiMarkup  
[Back to constructors index](/API_docs/constructors/index.html)



An [animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) based on a [custom emoji sticker](https://core.telegram.org/api/custom-emoji).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoji\_id|[long](/API_docs/types/long.html) | Yes|[Custom emoji ID](https://core.telegram.org/api/custom-emoji): the custom emoji sticker is shown at the center of the profile picture and occupies at most 67% of it.|
|background\_colors|Array of [int](/API_docs/types/int.html) | Yes|1, 2, 3 or 4 RBG-24 colors used to generate a solid (1), gradient (2) or freeform gradient (3, 4) background, similar to how [fill wallpapers](https://core.telegram.org/api/wallpapers#fill-types) are generated. The rotation angle for gradient backgrounds is 0.|



### Type: [VideoSize](/API_docs/types/VideoSize.html)


### Example:

```
$videoSizeEmojiMarkup = ['_' => 'videoSizeEmojiMarkup', 'emoji_id' => long, 'background_colors' => [int, int]];
```  
