---
title: "inputMediaDice"
description: "Send a dice-based animated sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDice  
[Back to constructors index](/API_docs/constructors/index.html)



Send a [dice-based animated sticker](https://core.telegram.org/api/dice)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.html) | Yes|The emoji, for now 🏀, 🎲 and 🎯 are supported|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaDice = ['_' => 'inputMediaDice', 'emoticon' => 'string'];
```  
