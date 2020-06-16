---
title: channels.deleteMessages
description: Delete messages in a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteMessages.html
---
# Method: channels.deleteMessages
[Back to methods index](index.md)



Delete messages in a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Channel/supergroup](https://core.telegram.org/api/channel) | Optional|
|id|Array of [int](../types/int.md) | IDs of messages to delete | Yes|


### Return type: [messages.AffectedMessages](../types/messages.AffectedMessages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.AffectedMessages = $MadelineProto->channels->deleteMessages(['channel' => InputChannel, 'id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages.AffectedMessages = channels.deleteMessages({channel=InputChannel, id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|403|MESSAGE_DELETE_FORBIDDEN|You can't delete one of the messages you tried to delete, most likely because it is a service message.|


