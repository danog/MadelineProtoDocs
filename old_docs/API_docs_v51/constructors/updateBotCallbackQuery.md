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
|data|[bytes](../types/bytes.md) | Yes|Data|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotCallbackQuery = ['_' => 'updateBotCallbackQuery', 'query_id' => long, 'user_id' => int, 'peer' => Peer, 'msg_id' => int, 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
updateBotCallbackQuery={_='updateBotCallbackQuery', query_id=long, user_id=int, peer=Peer, msg_id=int, data='bytes'}

```


