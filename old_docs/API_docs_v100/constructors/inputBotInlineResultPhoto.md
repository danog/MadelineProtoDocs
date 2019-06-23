---
title: inputBotInlineResultPhoto
description: Bot inline result photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResultPhoto  
[Back to constructors index](index.md)



Bot inline result photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|photo|[MessageMedia, Message, Update or InputPhoto](../types/InputPhoto.md) | Optional|Photo|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResultPhoto = ['_' => 'inputBotInlineResultPhoto', 'id' => 'string', 'type' => 'string', 'photo' => InputPhoto, 'send_message' => InputBotInlineMessage];
```  


Or, if you're into Lua:

```lua
inputBotInlineResultPhoto={_='inputBotInlineResultPhoto', id='string', type='string', photo=InputPhoto, send_message=InputBotInlineMessage}

```


