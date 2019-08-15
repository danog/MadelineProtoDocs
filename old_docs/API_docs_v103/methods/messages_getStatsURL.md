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
|dark|[Bool](../types/Bool.md) | Dark? | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|params|[string](../types/string.md) | Params | Yes|


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

$StatsURL = $MadelineProto->messages->getStatsURL(['dark' => Bool, 'peer' => InputPeer, 'params' => 'string', ]);
```

Or, if you're into Lua:

```lua
StatsURL = messages.getStatsURL({dark=Bool, peer=InputPeer, params='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


