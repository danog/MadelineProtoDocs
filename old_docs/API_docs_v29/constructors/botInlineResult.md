---
title: botInlineResult
description: Generic result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineResult  
[Back to constructors index](index.md)



Generic result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|Result ID|
|type|[string](../types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](../types/string.md) | Optional|Result title|
|description|[string](../types/string.md) | Optional|Result description|
|url|[string](../types/string.md) | Optional|URL of article or webpage|
|thumb|[WebDocument](../types/WebDocument.md) | Optional|Thumbnail for the result|
|content|[WebDocument](../types/WebDocument.md) | Optional|Content of the result|
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


