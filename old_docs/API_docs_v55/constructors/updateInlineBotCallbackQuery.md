---
title: updateInlineBotCallbackQuery
description: This notification is received by bots when a button is pressed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateInlineBotCallbackQuery  
[Back to constructors index](index.md)



This notification is received by bots when a button is pressed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|ID of the user that pressed the button|
|msg\_id|[InputBotInlineMessageID](../types/InputBotInlineMessageID.md) | Yes|ID of the inline message with the button|
|data|[bytes](../types/bytes.md) | Yes|Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateInlineBotCallbackQuery = ['_' => 'updateInlineBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'msg_id' => InputBotInlineMessageID, 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
updateInlineBotCallbackQuery={_='updateInlineBotCallbackQuery', query_id=long, user_id=int, msg_id=InputBotInlineMessageID, data='bytes'}

```


