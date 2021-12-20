---
title: "inputStickerSetDice"
description: "Used for fetching animated dice stickers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetDice  
[Back to constructors index](index.md)



Used for fetching [animated dice stickers](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](../types/string.md) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [InputStickerSet](../types/InputStickerSet.md)


### Example:

```php
$inputStickerSetDice = ['_' => 'inputStickerSetDice', 'emoticon' => 'string'];
```  


Or, if you're into Lua:

```lua
inputStickerSetDice={_='inputStickerSetDice', emoticon='string'}

```


