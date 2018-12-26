---
title: inputBotInlineResult
description: Bot inline result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResult  
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
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResult = ['_' => 'inputBotInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'content_type' => 'string', 'w' => int, 'h' => int, 'duration' => int, 'send_message' => InputBotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineResult", "id": "string", "type": "string", "title": "string", "description": "string", "url": "string", "thumb_url": "string", "content_url": "string", "content_type": "string", "w": int, "h": int, "duration": int, "send_message": InputBotInlineMessage}
```


Or, if you're into Lua:

```lua
inputBotInlineResult={_='inputBotInlineResult', id='string', type='string', title='string', description='string', url='string', thumb_url='string', content_url='string', content_type='string', w=int, h=int, duration=int, send_message=InputBotInlineMessage}

```


