---
title: "documentAttributeSticker"
description: "Defines a sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker\_55  
[Back to constructors index](index.md)



Defines a sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|alt|[string](../types/string.md) | Yes|Alternative emoji representation of sticker|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Associated stickerset|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeSticker_55 = ['_' => 'documentAttributeSticker', 'alt' => 'string', 'stickerset' => InputStickerSet];
```  


Or, if you're into Lua:

```lua
documentAttributeSticker_55={_='documentAttributeSticker', alt='string', stickerset=InputStickerSet}

```


