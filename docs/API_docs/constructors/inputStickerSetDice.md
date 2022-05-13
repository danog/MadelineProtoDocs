---
title: "inputStickerSetDice"
description: "Used for fetching animated dice stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetDice  
[Back to constructors index](/API_docs/constructors/index.html)



Used for fetching [animated dice stickers](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.html) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [InputStickerSet](/API_docs/types/InputStickerSet.html)


### Example:

```
$inputStickerSetDice = ['_' => 'inputStickerSetDice', 'emoticon' => 'string'];
```  
