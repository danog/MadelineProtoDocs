---
title: stats.getMegagroupStats
description: Get [supergroup statistics](https://core.telegram.org/api/stats)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMegagroupStats.html
---
# Method: stats.getMegagroupStats
[Back to methods index](index.md)



Get [supergroup statistics](https://core.telegram.org/api/stats)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](../types/Bool.md) | Whether to enable dark theme for graph colors | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Supergroup ID](https://core.telegram.org/api/channel) | Optional|


### Return type: [stats.MegagroupStats](../types/stats.MegagroupStats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats_MegagroupStats = $MadelineProto->stats->getMegagroupStats(['dark' => Bool, 'channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
stats_MegagroupStats = stats.getMegagroupStats({dark=Bool, channel=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|


