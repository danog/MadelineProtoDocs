---
title: "inputStickerSetThumb"
description: "Location of stickerset thumbnail (see files)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetThumb  
[Back to constructors index](/API_docs/constructors/index.html)



Location of stickerset thumbnail (see [files](https://core.telegram.org/api/files))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|Sticker set|
|thumb\_version|[int](/API_docs/types/int.html) | Yes|Thumbnail version|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputStickerSetThumb = ['_' => 'inputStickerSetThumb', 'stickerset' => InputStickerSet, 'thumb_version' => int];
```  
