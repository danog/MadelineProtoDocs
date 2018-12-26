---
title: messages.botCallbackAnswer
description: Bot callback answer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.botCallbackAnswer  
[Back to constructors index](index.md)



Bot callback answer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|alert|[Bool](../types/Bool.md) | Optional|Alert?|
|has\_url|[Bool](../types/Bool.md) | Optional|Has URL?|
|message|[string](../types/string.md) | Optional|Message|
|url|[string](../types/string.md) | Optional|URL|
|cache\_time|[int](../types/int.md) | Yes|Cache time|



### Type: [messages\_BotCallbackAnswer](../types/messages_BotCallbackAnswer.md)


### Example:

```php
$messages_botCallbackAnswer = ['_' => 'messages.botCallbackAnswer', 'alert' => Bool, 'has_url' => Bool, 'message' => 'string', 'url' => 'string', 'cache_time' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.botCallbackAnswer", "alert": Bool, "has_url": Bool, "message": "string", "url": "string", "cache_time": int}
```


Or, if you're into Lua:

```lua
messages_botCallbackAnswer={_='messages.botCallbackAnswer', alert=Bool, has_url=Bool, message='string', url='string', cache_time=int}

```


