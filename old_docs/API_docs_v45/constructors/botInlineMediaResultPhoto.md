---
title: botInlineMediaResultPhoto
description: botInlineMediaResultPhoto attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMediaResultPhoto  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[string](../types/string.md) | Yes|
|type|[string](../types/string.md) | Yes|
|photo|[Photo](../types/Photo.md) | Optional|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineMediaResultPhoto = ['_' => 'botInlineMediaResultPhoto', 'id' => 'string', 'type' => 'string', 'photo' => Photo, 'send_message' => BotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botInlineMediaResultPhoto", "id": "string", "type": "string", "photo": Photo, "send_message": BotInlineMessage}
```


Or, if you're into Lua:

```lua
botInlineMediaResultPhoto={_='botInlineMediaResultPhoto', id='string', type='string', photo=Photo, send_message=BotInlineMessage}

```


