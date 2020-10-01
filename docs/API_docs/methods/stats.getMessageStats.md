---
title: stats.getMessageStats
description: stats.getMessageStats parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMessageStats.html
---
# Method: stats.getMessageStats
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dark|[Bool](../types/Bool.md) | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Optional|
|msg\_id|[int](../types/int.md) | Yes|


### Return type: [stats.MessageStats](../types/stats.MessageStats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$stats.MessageStats = $MadelineProto->stats->getMessageStats(['dark' => Bool, 'channel' => InputChannel, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
stats.MessageStats = stats.getMessageStats({dark=Bool, channel=InputChannel, msg_id=int, })
```

