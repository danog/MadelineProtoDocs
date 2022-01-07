---
title: "inputMediaDice"
description: "Send a dice-based animated sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDice  
[Back to constructors index](/API_docs/constructors/index.md)



Send a [dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.md) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaDice = ['_' => 'inputMediaDice', 'emoticon' => 'string'];
```  
