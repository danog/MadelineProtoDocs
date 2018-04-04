---
title: inputStickerSetID
description: inputStickerSetID attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: inputStickerSetID  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputStickerSet](../types/InputStickerSet.md)


### Example:

```
$inputStickerSetID = ['_' => 'inputStickerSetID', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputStickerSetID", "id": long, "access_hash": long}
```


Or, if you're into Lua:  


```
inputStickerSetID={_='inputStickerSetID', id=long, access_hash=long}

```


