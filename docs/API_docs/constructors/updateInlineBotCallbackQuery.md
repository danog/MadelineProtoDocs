---
title: "updateInlineBotCallbackQuery"
description: "This notification is received by bots when a button is pressed"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateInlineBotCallbackQuery  
[Back to constructors index](index.md)



This notification is received by bots when a button is pressed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[long](../types/long.md) | Yes|
|msg\_id|[InputBotInlineMessageID](../types/InputBotInlineMessageID.md) | Yes|ID of the inline message with the button|
|chat\_instance|[long](../types/long.md) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](../types/bytes.md) | Optional|Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.|
|game\_short\_name|[string](../types/string.md) | Optional|Short name of a Game to be returned, serves as the unique identifier for the game|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateInlineBotCallbackQuery = ['_' => 'updateInlineBotCallbackQuery', 'query_id' => long, 'user_id' => long, 'msg_id' => InputBotInlineMessageID, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  


Or, if you're into Lua:

```lua
updateInlineBotCallbackQuery={_='updateInlineBotCallbackQuery', query_id=long, user_id=long, msg_id=InputBotInlineMessageID, chat_instance=long, data='bytes', game_short_name='string'}

```


