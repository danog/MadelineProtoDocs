---
title: "updateNewStickerSet"
description: "A new stickerset was installed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewStickerSet  
[Back to constructors index](/API_docs/constructors/index.html)



A new stickerset was installed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[messages.StickerSet](/API_docs/constructors/messages.StickerSet.html) | Yes|The installed stickerset|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewStickerSet = ['_' => 'updateNewStickerSet', 'stickerset' => messages.StickerSet];
```  
