---
title: messages.getStatsURL
description: Get stats URL
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getStatsURL  
[Back to methods index](index.md)


Get stats URL

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|


### Return type: [StatsURL](../types/StatsURL.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$StatsURL = $MadelineProto->messages->getStatsURL(['peer' => InputPeer, ]);
```

Or, if you're into Lua:

```lua
StatsURL = messages.getStatsURL({peer=InputPeer, })
```

