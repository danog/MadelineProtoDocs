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
|chat\_instance|[long](../types/long.md) | Yes|Chat instance|
|data|[bytes](../types/bytes.md) | Optional|Data|
|game\_short\_name|[string](../types/string.md) | Optional|Game short name|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateInlineBotCallbackQuery = ['_' => 'updateInlineBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'msg_id' => InputBotInlineMessageID, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateInlineBotCallbackQuery", "query_id": long, "user_id": int, "msg_id": InputBotInlineMessageID, "chat_instance": long, "data": {"_": "bytes", "bytes":"base64 encoded bytes"}, "game_short_name": "string"}
```


Or, if you're into Lua:

```lua
updateInlineBotCallbackQuery={_='updateInlineBotCallbackQuery', query_id=long, user_id=int, msg_id=InputBotInlineMessageID, chat_instance=long, data='bytes', game_short_name='string'}

```


