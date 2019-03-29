---
title: channelAdminLogEventActionChangeStickerSet
description: Change stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeStickerSet  
[Back to constructors index](index.md)



Change stickerset

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


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeStickerSet={_='channelAdminLogEventActionChangeStickerSet', prev_stickerset=InputStickerSet, new_stickerset=InputStickerSet}

```


