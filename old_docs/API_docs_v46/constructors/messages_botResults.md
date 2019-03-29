---
title: messages.botResults
description: Bot results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.botResults  
[Back to constructors index](index.md)



Bot results

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gallery|[Bool](../types/Bool.md) | Optional|Gallery?|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|next\_offset|[string](../types/string.md) | Optional|Next offset|
|results|Array of [BotInlineResult](../types/BotInlineResult.md) | Yes|Results|



### Type: [messages\_BotResults](../types/messages_BotResults.md)


### Example:

```php
$messages_botResults = ['_' => 'messages.botResults', 'gallery' => Bool, 'query_id' => long, 'next_offset' => 'string', 'results' => [BotInlineResult, BotInlineResult]];
```  


Or, if you're into Lua:

```lua
messages_botResults={_='messages.botResults', gallery=Bool, query_id=long, next_offset='string', results={BotInlineResult}}

```


