---
title: messages.getStatsURL
description: Returns URL with the chat statistics. Currently this method can be used only for channels
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getStatsURL.html
---
# Method: messages.getStatsURL
[Back to methods index](index.md)



Returns URL with the chat statistics. Currently this method can be used only for channels

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|dark|[Bool](../types/Bool.md) | Pass true if a URL with the dark theme must be returned | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Chat identifier | Optional|
|params|[string](../types/string.md) | Parameters from `tg://statsrefresh?params=******` link | Yes|


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

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|UNKNOWN_ERROR|Internal error|


