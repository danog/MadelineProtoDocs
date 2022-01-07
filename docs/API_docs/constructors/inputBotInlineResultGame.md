---
title: "inputBotInlineResultGame"
description: "Game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultGame  
[Back to constructors index](index.md)



Game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|Result ID|
|short\_name|[string](../types/string.md) | Yes|Game short name|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultGame = ['_' => 'inputBotInlineResultGame', 'id' => 'string', 'short_name' => 'string', 'send_message' => InputBotInlineMessage];
```  
