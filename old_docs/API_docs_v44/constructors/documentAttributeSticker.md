---
title: documentAttributeSticker
description: Document attribute sticker
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
[Back to constructors index](index.md)



Document attribute sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|alt|[string](../types/string.md) | Yes|Alt|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Stickerset|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'alt' => 'string', 'stickerset' => InputStickerSet];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "documentAttributeSticker", "alt": "string", "stickerset": InputStickerSet}
```


Or, if you're into Lua:

```lua
documentAttributeSticker={_='documentAttributeSticker', alt='string', stickerset=InputStickerSet}

```


