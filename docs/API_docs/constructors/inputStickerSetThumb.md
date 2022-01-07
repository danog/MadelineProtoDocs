---
title: "inputStickerSetThumb"
description: "Location of stickerset thumbnail (see files)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetThumb  
[Back to constructors index](index.md)



Location of stickerset thumbnail (see [files](https://core.telegram.org/api/files))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Sticker set|
|thumb\_version|[int](../types/int.md) | Yes|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputStickerSetThumb = ['_' => 'inputStickerSetThumb', 'stickerset' => InputStickerSet, 'thumb_version' => int];
```  
