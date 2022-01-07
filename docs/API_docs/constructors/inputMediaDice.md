---
title: "inputMediaDice"
description: "Send a dice-based animated sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDice  
[Back to constructors index](index.md)



Send a [dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](../types/string.md) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDice = ['_' => 'inputMediaDice', 'emoticon' => 'string'];
```  
