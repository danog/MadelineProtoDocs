---
title: "channels.deleteHistory"
description: "Delete the history of a [supergroup](https://core.telegram.org/api/channel)"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteHistory.html
---
# Method: channels.deleteHistory
[Back to methods index](index.md)



Delete the history of a [supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Supergroup](https://core.telegram.org/api/channel) whose history must be deleted | Optional|
|max\_id|[int](../types/int.md) | ID of message **up to which** the history must be deleted | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->deleteHistory(['channel' => InputChannel, 'max_id' => int, ]);
```

Or, if you're into Lua:

```lua
Bool = channels.deleteHistory({channel=InputChannel, max_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|


