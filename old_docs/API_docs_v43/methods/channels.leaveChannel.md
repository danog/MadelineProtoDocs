---
title: channels.leaveChannel
description: Leave a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_leaveChannel.html
---
# Method: channels.leaveChannel
[Back to methods index](index.md)



Leave a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Channel/supergroup](https://core.telegram.org/api/channel) to leave | Optional|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->leaveChannel(['channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.leaveChannel({channel=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_CREATOR|You can't leave this channel, because you're its creator|
|400|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHANNEL_PUBLIC_GROUP_NA|channel/supergroup not available|


