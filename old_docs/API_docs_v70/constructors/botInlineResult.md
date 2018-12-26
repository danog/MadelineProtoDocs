---
title: botInlineResult
description: Bot inline result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineResult  
[Back to constructors index](index.md)



Bot inline result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|type|[string](../types/string.md) | Yes|Type|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|url|[string](../types/string.md) | Optional|URL|
|thumb\_url|[string](../types/string.md) | Optional|Thumbnail URL|
|content\_url|[string](../types/string.md) | Optional|Content URL|
|content\_type|[string](../types/string.md) | Optional|Content type|
|w|[int](../types/int.md) | Optional|Width|
|h|[int](../types/int.md) | Optional|Height|
|duration|[int](../types/int.md) | Optional|Duration|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|Message to send|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineResult = ['_' => 'botInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'content_type' => 'string', 'w' => int, 'h' => int, 'duration' => int, 'send_message' => BotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botInlineResult", "id": "string", "type": "string", "title": "string", "description": "string", "url": "string", "thumb_url": "string", "content_url": "string", "content_type": "string", "w": int, "h": int, "duration": int, "send_message": BotInlineMessage}
```


Or, if you're into Lua:

```lua
botInlineResult={_='botInlineResult', id='string', type='string', title='string', description='string', url='string', thumb_url='string', content_url='string', content_type='string', w=int, h=int, duration=int, send_message=BotInlineMessage}

```


