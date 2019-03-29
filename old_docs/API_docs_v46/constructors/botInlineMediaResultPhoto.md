---
title: botInlineMediaResultPhoto
description: Bot inline media result photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMediaResultPhoto  
[Back to constructors index](index.md)



Bot inline media result photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|photo|[Photo](../types/Photo.md) | Optional|Photo|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|Send message|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineMediaResultPhoto = ['_' => 'botInlineMediaResultPhoto', 'id' => 'string', 'type' => 'string', 'photo' => Photo, 'send_message' => BotInlineMessage];
```  


Or, if you're into Lua:

```lua
botInlineMediaResultPhoto={_='botInlineMediaResultPhoto', id='string', type='string', photo=Photo, send_message=BotInlineMessage}

```


