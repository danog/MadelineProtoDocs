---
title: "messageMediaDice"
description: "Dice-based animated sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDice  
[Back to constructors index](/API_docs/constructors/index.md)



[Dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|value|[int](/API_docs/types/int.md) | Yes|[Dice value](https://core.telegram.org/api/dice)|
|emoticon|[string](/API_docs/types/string.md) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [MessageMedia](/API_docs/types/MessageMedia.md)


### Example:

```php
$messageMediaDice = ['_' => 'messageMediaDice', 'value' => int, 'emoticon' => 'string'];
```  
