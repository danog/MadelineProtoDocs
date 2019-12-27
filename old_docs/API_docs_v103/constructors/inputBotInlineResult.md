---
title: inputBotInlineResult
description: An inline bot result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineResult  
[Back to constructors index](index.md)



An inline bot result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID of result|
|type|[string](../types/string.md) | Yes|Result type (see [bot API docs](https://core.telegram.org/bots/api#inlinequeryresult))|
|title|[string](../types/string.md) | Optional|Result title|
|description|[string](../types/string.md) | Optional|Result description|
|url|[string](../types/string.md) | Optional|URL of result|
|thumb|[InputWebDocument](../types/InputWebDocument.md) | Optional|Thumbnail for result|
|content|[InputWebDocument](../types/InputWebDocument.md) | Optional|Result contents|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResult = ['_' => 'inputBotInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb' => InputWebDocument, 'content' => InputWebDocument, 'send_message' => InputBotInlineMessage];
```  


Or, if you're into Lua:

```lua
inputBotInlineResult={_='inputBotInlineResult', id='string', type='string', title='string', description='string', url='string', thumb=InputWebDocument, content=InputWebDocument, send_message=InputBotInlineMessage}

```


