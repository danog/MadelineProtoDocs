---
title: channels.exportMessageLink
description: Get link and embed info of a message in a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.exportMessageLink  
[Back to methods index](index.md)


Get link and embed info of a message in a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|id|[int](../types/int.md) | Message ID | Yes|
|grouped|[Bool](../types/Bool.md) | Whether to include other grouped media (for albums) | Yes|


### Return type: [ExportedMessageLink](../types/ExportedMessageLink.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedMessageLink = $MadelineProto->channels->exportMessageLink(['channel' => InputChannel, 'id' => int, 'grouped' => Bool, ]);
```

Or, if you're into Lua:

```lua
ExportedMessageLink = channels.exportMessageLink({channel=InputChannel, id=int, grouped=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


