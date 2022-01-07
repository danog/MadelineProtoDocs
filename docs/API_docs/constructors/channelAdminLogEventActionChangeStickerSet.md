---
title: "channelAdminLogEventActionChangeStickerSet"
description: "The supergroup's stickerset was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeStickerSet  
[Back to constructors index](index.md)



The supergroup's stickerset was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Previous stickerset|
|new\_stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|New stickerset|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeStickerSet = ['_' => 'channelAdminLogEventActionChangeStickerSet', 'prev_stickerset' => InputStickerSet, 'new_stickerset' => InputStickerSet];
```  
