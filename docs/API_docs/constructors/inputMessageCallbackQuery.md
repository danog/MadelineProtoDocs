---
title: "inputMessageCallbackQuery"
description: "Used by bots for fetching information about the message that originated a callback query"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMessageCallbackQuery  
[Back to constructors index](index.md)



Used by bots for fetching information about the message that originated a callback query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Message ID|
|query\_id|[long](../types/long.md) | Yes|Callback query ID|



### Type: [InputMessage](../types/InputMessage.md)


### Example:

```php
$inputMessageCallbackQuery = ['_' => 'inputMessageCallbackQuery', 'id' => int, 'query_id' => long];
```  


Or, if you're into Lua:

```lua
inputMessageCallbackQuery={_='inputMessageCallbackQuery', id=int, query_id=long}

```


