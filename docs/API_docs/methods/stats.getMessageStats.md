---
title: "stats.getMessageStats"
description: "Get [message statistics](https://core.telegram.org/api/stats)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessageStats.html
---
# Method: stats.getMessageStats
[Back to methods index](index.md)



Get [message statistics](https://core.telegram.org/api/stats)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](../types/Bool.md) | Whether to enable dark theme for graph colors | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel ID | Optional|
|msg\_id|[int](../types/int.md) | Message ID | Yes|


### Return type: [stats.MessageStats](../types/stats.MessageStats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_MessageStats = $MadelineProto->stats->getMessageStats(['dark' => Bool, 'channel' => InputChannel, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
stats_MessageStats = stats.getMessageStats({dark=Bool, channel=InputChannel, msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|


