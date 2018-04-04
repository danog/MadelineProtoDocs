---
title: updateStickerSetsOrder
description: updateStickerSetsOrder attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStickerSetsOrder  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|order|Array of [long](../types/long.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'order' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateStickerSetsOrder", "order": [long]}
```


Or, if you're into Lua:  


```
updateStickerSetsOrder={_='updateStickerSetsOrder', order={long}}

```


