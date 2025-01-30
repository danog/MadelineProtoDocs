---
title: "channelAdminLogEventActionChangeEmojiStickerSet"
description: "The supergroup's custom emoji stickerset was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeEmojiStickerSet  
[Back to constructors index](/API_docs/constructors/index.html)



The supergroup's [custom emoji stickerset](https://core.telegram.org/api/boost#setting-a-custom-emoji-stickerset-for-supergroups) was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|Old value|
|new\_stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|New value|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeEmojiStickerSet = ['_' => 'channelAdminLogEventActionChangeEmojiStickerSet', 'prev_stickerset' => InputStickerSet, 'new_stickerset' => InputStickerSet];
```  
