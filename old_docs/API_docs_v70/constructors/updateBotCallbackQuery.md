---
title: updateBotCallbackQuery
description: updateBotCallbackQuery attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotCallbackQuery  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](../types/long.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|peer|[Peer](../types/Peer.md) | Yes|
|msg\_id|[int](../types/int.md) | Yes|
|chat\_instance|[long](../types/long.md) | Yes|
|data|[bytes](../types/bytes.md) | Optional|
|game\_short\_name|[string](../types/string.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'peer' => Peer, 'msg_id' => int, 'chat_instance' => long, 'data' => 'bytes', 'game_short_name' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateBotCallbackQuery", "query_id": long, "user_id": int, "peer": Peer, "msg_id": int, "chat_instance": long, "data": {"_": "bytes", "bytes":"base64 encoded bytes"}, "game_short_name": "string"}
```


Or, if you're into Lua:

```lua
updateBotCallbackQuery={_='updateBotCallbackQuery', query_id=long, user_id=int, peer=Peer, msg_id=int, chat_instance=long, data='bytes', game_short_name='string'}

```


