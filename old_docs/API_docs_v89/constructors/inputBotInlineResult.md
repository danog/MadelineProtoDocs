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
|thumb|[InputWebDocument](../types/InputWebDocument.md) | Optional|Thumbnail|
|content|[InputWebDocument](../types/InputWebDocument.md) | Optional|Content|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResult = ['_' => 'inputBotInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => InputWebDocument, 'content' => InputWebDocument, 'send_message' => InputBotInlineMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineResult", "id": "string", "type": "string", "title": "string", "description": "string", "url": "string", "thumb": InputWebDocument, "content": InputWebDocument, "send_message": InputBotInlineMessage}
```


Or, if you're into Lua:

```lua
inputBotInlineResult={_='inputBotInlineResult', id='string', type='string', title='string', description='string', url='string', thumb=InputWebDocument, content=InputWebDocument, send_message=InputBotInlineMessage}

```


