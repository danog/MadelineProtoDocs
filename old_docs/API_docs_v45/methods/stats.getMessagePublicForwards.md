---
title: stats.getMessagePublicForwards
description: stats.getMessagePublicForwards parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessagePublicForwards.html
---
# Method: stats.getMessagePublicForwards
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Optional|
|msg\_id|[int](../types/int.md) | Yes|
|offset\_rate|[int](../types/int.md) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|offset\_id|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Messages = $MadelineProto->stats->getMessagePublicForwards(['channel' => InputChannel, 'msg_id' => int, 'offset_rate' => int, 'offset_peer' => InputPeer, 'offset_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Messages = stats.getMessagePublicForwards({channel=InputChannel, msg_id=int, offset_rate=int, offset_peer=InputPeer, offset_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


