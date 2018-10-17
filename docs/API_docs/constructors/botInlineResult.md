---
title: botInlineResult
description: botInlineResult attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineResult  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[string](../types/string.md) | Yes|
|type|[string](../types/string.md) | Yes|
|title|[string](../types/string.md) | Optional|
|description|[string](../types/string.md) | Optional|
|url|[string](../types/string.md) | Optional|
|thumb|[WebDocument](../types/WebDocument.md) | Optional|
|content|[WebDocument](../types/WebDocument.md) | Optional|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineResult = ['_' => 'botInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => WebDocument, 'content' => WebDocument, 'send_message' => BotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botInlineResult", "id": "string", "type": "string", "title": "string", "description": "string", "url": "string", "thumb": WebDocument, "content": WebDocument, "send_message": BotInlineMessage}
```


Or, if you're into Lua:

```lua
botInlineResult={_='botInlineResult', id='string', type='string', title='string', description='string', url='string', thumb=WebDocument, content=WebDocument, send_message=BotInlineMessage}

```


