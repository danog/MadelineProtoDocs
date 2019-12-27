---
title: documentAttributeSticker
description: Defines a sticker
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
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
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'alt' => 'string', 'stickerset' => InputStickerSet];
```  


Or, if you're into Lua:

```lua
documentAttributeSticker={_='documentAttributeSticker', alt='string', stickerset=InputStickerSet}

```


