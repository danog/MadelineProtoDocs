---
title: updateBotCallbackQuery
description: A callback button was pressed, and the button data was sent to the bot that created the button
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCallbackQuery  
[Back to constructors index](index.md)



A callback button was pressed, and the button data was sent to the bot that created the button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|ID of the user that pressed the button|
|peer|[Peer](../types/Peer.md) | Yes|Chat where the inline keyboard was sent|
|msg\_id|[int](../types/int.md) | Yes|Message ID|
|chat\_instance|[long](../types/long.md) | Yes|Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.|
|data|[bytes](../types/bytes.md) | Optional|Callback data|
|game\_short\_name|[string](../types/string.md) | Optional|Short name of a Game to be returned, serves as the unique identifier for the game|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'peer' => Peer, 'msg_id' => int, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  


Or, if you're into Lua:

```lua
updateBotCallbackQuery={_='updateBotCallbackQuery', query_id=long, user_id=int, peer=Peer, msg_id=int, chat_instance=long, data='bytes', game_short_name='string'}

```


