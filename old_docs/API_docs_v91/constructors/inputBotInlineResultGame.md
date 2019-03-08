---
title: inputBotInlineResultGame
description: Bot inline result game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultGame  
[Back to constructors index](index.md)



Bot inline result game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|short\_name|[string](../types/string.md) | Yes|Short name|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultGame = ['_' => 'inputBotInlineResultGame', 'id' => 'string', 'short_name' => 'string', 'send_message' => InputBotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineResultGame", "id": "string", "short_name": "string", "send_message": InputBotInlineMessage}
```


Or, if you're into Lua:

```lua
inputBotInlineResultGame={_='inputBotInlineResultGame', id='string', short_name='string', send_message=InputBotInlineMessage}

```


