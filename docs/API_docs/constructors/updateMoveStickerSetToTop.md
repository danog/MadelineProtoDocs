---
title: "updateMoveStickerSetToTop"
description: "A stickerset was just moved to top, see here for more info »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMoveStickerSetToTop  
[Back to constructors index](/API_docs/constructors/index.html)



A stickerset was just moved to top, [see here for more info »](https://core.telegram.org/api/stickers#recent-stickersets)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](/API_docs/types/Bool.html) | Optional|This update is referring to a [mask stickerset](https://core.telegram.org/api/stickers#mask-stickers)|
|emojis|[Bool](/API_docs/types/Bool.html) | Optional|This update is referring to a [custom emoji stickerset](https://core.telegram.org/api/custom-emoji)|
|stickerset|[long](/API_docs/types/long.html) | Yes|[Stickerset](https://core.telegram.org/api/stickers) ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMoveStickerSetToTop = ['_' => 'updateMoveStickerSetToTop', 'masks' => Bool, 'emojis' => Bool, 'stickerset' => long];
```  
