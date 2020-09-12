---
title: inputStickerSetThumb
description: Location of stickerset thumbnail (see [files](https://core.telegram.org/api/files))
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetThumb  
[Back to constructors index](index.md)



Location of stickerset thumbnail (see [files](https://core.telegram.org/api/files))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Sticker set|
|volume\_id|[long](../types/long.md) | Yes|Volume ID|
|local\_id|[int](../types/int.md) | Yes|Local ID|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputStickerSetThumb = ['_' => 'inputStickerSetThumb', 'stickerset' => InputStickerSet, 'volume_id' => long, 'local_id' => int];
```  


Or, if you're into Lua:

```lua
inputStickerSetThumb={_='inputStickerSetThumb', stickerset=InputStickerSet, volume_id=long, local_id=int}

```


