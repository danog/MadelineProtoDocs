---
title: inputStickerSetThumb
description: Stickerset thumbnail
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetThumb  
[Back to constructors index](index.md)



Stickerset thumbnail

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Stickerset|
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


