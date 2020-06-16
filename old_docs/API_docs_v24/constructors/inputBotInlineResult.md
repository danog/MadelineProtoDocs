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
|thumb\_url|[string](../types/string.md) | Optional|
|content\_url|[string](../types/string.md) | Optional|
|content\_type|[string](../types/string.md) | Optional|
|w|[int](../types/int.md) | Optional|
|h|[int](../types/int.md) | Optional|
|duration|[int](../types/int.md) | Optional|
|send\_message|[InputBotInlineMessage](../types/InputBotInlineMessage.md) | Yes|Message to send when the result is selected|



### Type: [InputBotInlineResult](../types/InputBotInlineResult.md)


### Example:

```php
$inputBotInlineResult = ['_' => 'inputBotInlineResult', 'id' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'url' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'content_type' => 'string', 'w' => int, 'h' => int, 'duration' => int, 'send_message' => InputBotInlineMessage];
```  


Or, if you're into Lua:

```lua
inputBotInlineResult={_='inputBotInlineResult', id='string', type='string', title='string', description='string', url='string', thumb_url='string', content_url='string', content_type='string', w=int, h=int, duration=int, send_message=InputBotInlineMessage}

```


