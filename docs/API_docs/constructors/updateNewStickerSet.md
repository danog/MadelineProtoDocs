---
title: "updateNewStickerSet"
description: "A new stickerset was installed"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewStickerSet  
[Back to constructors index](index.md)



A new stickerset was installed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[messages.StickerSet](../constructors/messages.StickerSet.md) | Yes|The installed stickerset|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewStickerSet = ['_' => 'updateNewStickerSet', 'stickerset' => messages.StickerSet];
```  


Or, if you're into Lua:

```lua
updateNewStickerSet={_='updateNewStickerSet', stickerset=messages.StickerSet}

```


