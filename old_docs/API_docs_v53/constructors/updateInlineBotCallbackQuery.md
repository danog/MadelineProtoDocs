---
title: updateInlineBotCallbackQuery
description: Update inline bot callback query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateInlineBotCallbackQuery  
[Back to constructors index](index.md)



Update inline bot callback query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|msg\_id|[InputBotInlineMessageID](../types/InputBotInlineMessageID.md) | Yes|Msg ID|
|data|[bytes](../types/bytes.md) | Yes|Data|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateInlineBotCallbackQuery = ['_' => 'updateInlineBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'msg_id' => InputBotInlineMessageID, 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
updateInlineBotCallbackQuery={_='updateInlineBotCallbackQuery', query_id=long, user_id=int, msg_id=InputBotInlineMessageID, data='bytes'}

```


