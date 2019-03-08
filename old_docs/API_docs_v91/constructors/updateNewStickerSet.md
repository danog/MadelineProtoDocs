---
title: updateNewStickerSet
description: Update new sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewStickerSet  
[Back to constructors index](index.md)



Update new sticker set

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[messages\_StickerSet](../types/messages_StickerSet.md) | Yes|Stickerset|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewStickerSet = ['_' => 'updateNewStickerSet', 'stickerset' => messages_StickerSet];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateNewStickerSet", "stickerset": messages_StickerSet}
```


Or, if you're into Lua:

```lua
updateNewStickerSet={_='updateNewStickerSet', stickerset=messages_StickerSet}

```


