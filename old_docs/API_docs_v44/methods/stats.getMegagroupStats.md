---
title: stats.getMegagroupStats
description: stats.getMegagroupStats parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMegagroupStats.html
---
# Method: stats.getMegagroupStats
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dark|[Bool](../types/Bool.md) | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Optional|


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

$stats.MegagroupStats = $MadelineProto->stats->getMegagroupStats(['dark' => Bool, 'channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
stats.MegagroupStats = stats.getMegagroupStats({dark=Bool, channel=InputChannel, })
```

