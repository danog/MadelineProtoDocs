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
|thumb|[WebDocument](../types/WebDocument.md) | Optional|Thumbnailnail|
|content|[WebDocument](../types/WebDocument.md) | Optional|Content|
|send\_message|[BotInlineMessage](../types/BotInlineMessage.md) | Yes|Message to send|



### Type: [BotInlineResult](../types/BotInlineResult.md)


### Example:

```php
$botInlineResult = ['_' => 'botInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => WebDocument, 'content' => WebDocument, 'send_message' => BotInlineMessage];
```  


Or, if you're into Lua:

```lua
botInlineResult={_='botInlineResult', id='string', type='string', title='string', description='string', url='string', thumb=WebDocument, content=WebDocument, send_message=BotInlineMessage}

```


