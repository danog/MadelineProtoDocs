---
title: updateBotCallbackQuery
description: Update bot callback query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCallbackQuery  
[Back to constructors index](index.md)



Update bot callback query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|msg\_id|[int](../types/int.md) | Yes|Msg ID|
|chat\_instance|[long](../types/long.md) | Yes|Chat instance|
|data|[bytes](../types/bytes.md) | Optional|Data|
|game\_short\_name|[string](../types/string.md) | Optional|Game short name|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'peer' => Peer, 'msg_id' => int, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  


Or, if you're into Lua:

```lua
updateBotCallbackQuery={_='updateBotCallbackQuery', query_id=long, user_id=int, peer=Peer, msg_id=int, chat_instance=long, data='bytes', game_short_name='string'}

```


