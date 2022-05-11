---
title: "stats.getMegagroupStats"
description: "Get [supergroup statistics](https://core.telegram.org/api/stats)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/stats_getMegagroupStats.html
---
# Method: stats.getMegagroupStats
[Back to methods index](index.html)



Get [supergroup statistics](https://core.telegram.org/api/stats)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Whether to enable dark theme for graph colors | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Supergroup ID](https://core.telegram.org/api/channel) | Optional|


### Return type: [stats.MegagroupStats](/API_docs/types/stats.MegagroupStats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$stats_MegagroupStats = $MadelineProto->stats->getMegagroupStats(dark: Bool, channel: InputChannel, );
```

