---
title: channelAdminLogEventActionChangeStickerSet
description: channelAdminLogEventActionChangeStickerSet attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeStickerSet  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|
|new\_stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangeStickerSet = ['_' => 'channelAdminLogEventActionChangeStickerSet', 'prev_stickerset' => InputStickerSet, 'new_stickerset' => InputStickerSet];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionChangeStickerSet", "prev_stickerset": InputStickerSet, "new_stickerset": InputStickerSet}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionChangeStickerSet={_='channelAdminLogEventActionChangeStickerSet', prev_stickerset=InputStickerSet, new_stickerset=InputStickerSet}

```


