---
title: "stats.getMessagePublicForwards"
description: "Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessagePublicForwards.html
---
# Method: stats.getMessagePublicForwards
[Back to methods index](index.md)



Obtains a list of messages, indicating to which other public channels was a channel message forwarded.  
Will return a list of [messages](../constructors/message.md) with `peer_id` equal to the public channel to which this message was forwarded.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Source channel | Optional|
|msg\_id|[int](../types/int.md) | Source message ID | Yes|
|offset\_rate|[int](../types/int.md) | Initially 0, then set to the `next_rate` parameter of [messages.messagesSlice](../constructors/messages.messagesSlice.md) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->stats->getMessagePublicForwards(['channel' => InputChannel, 'msg_id' => int, 'offset_rate' => int, 'offset_peer' => InputPeer, 'offset_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = stats.getMessagePublicForwards({channel=InputChannel, msg_id=int, offset_rate=int, offset_peer=InputPeer, offset_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


