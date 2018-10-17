---
title: messages.botResults
description: messages_botResults attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.botResults  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gallery|[Bool](../types/Bool.md) | Optional|
|query\_id|[long](../types/long.md) | Yes|
|next\_offset|[string](../types/string.md) | Optional|
|switch\_pm|[InlineBotSwitchPM](../types/InlineBotSwitchPM.md) | Optional|
|results|Array of [BotInlineResult](../types/BotInlineResult.md) | Yes|



### Type: [messages\_BotResults](../types/messages_BotResults.md)


### Example:

```php
$messages_botResults = ['_' => 'messages.botResults', 'gallery' => Bool, 'query_id' => long, 'next_offset' => 'string', 'switch_pm' => InlineBotSwitchPM, 'results' => [BotInlineResult, BotInlineResult]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.botResults", "gallery": Bool, "query_id": long, "next_offset": "string", "switch_pm": InlineBotSwitchPM, "results": [BotInlineResult]}
```


Or, if you're into Lua:

```lua
messages_botResults={_='messages.botResults', gallery=Bool, query_id=long, next_offset='string', switch_pm=InlineBotSwitchPM, results={BotInlineResult}}

```


