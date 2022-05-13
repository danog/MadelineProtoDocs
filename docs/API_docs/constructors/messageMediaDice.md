---
title: "messageMediaDice"
description: "Dice-based animated sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDice  
[Back to constructors index](/API_docs/constructors/index.html)



[Dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|[int](/API_docs/types/int.html) | Yes|[Dice value](https://core.telegram.org/api/dice)|
|emoticon|[string](/API_docs/types/string.html) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaDice = ['_' => 'messageMediaDice', 'value' => int, 'emoticon' => 'string'];
```  
