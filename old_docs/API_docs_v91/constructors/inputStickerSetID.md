---
title: inputStickerSetID
description: Sticker set ID
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetID  
[Back to constructors index](index.md)



Sticker set ID

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputStickerSet](../types/InputStickerSet.md)


### Example:

```php
$inputStickerSetID = ['_' => 'inputStickerSetID', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputStickerSetID", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputStickerSetID={_='inputStickerSetID', id=long, access_hash=long}

```


