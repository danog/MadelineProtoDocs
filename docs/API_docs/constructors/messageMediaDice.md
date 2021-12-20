---
title: "messageMediaDice"
description: "Dice-based animated sticker"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDice  
[Back to constructors index](index.md)



[Dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|[int](../types/int.md) | Yes|[Dice value](https://core.telegram.org/api/dice)|
|emoticon|[string](../types/string.md) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaDice = ['_' => 'messageMediaDice', 'value' => int, 'emoticon' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaDice={_='messageMediaDice', value=int, emoticon='string'}

```


