---
title: channels.getParticipant
description: Get info about a [channel/supergroup](https://core.telegram.org/api/channel) participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getParticipant.html
---
# Method: channels.getParticipant
[Back to methods index](index.md)



Get info about a [channel/supergroup](https://core.telegram.org/api/channel) participant

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel/supergroup | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | ID of participant to get info about | Optional|


### Return type: [channels.ChannelParticipant](../types/channels.ChannelParticipant.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$channels_ChannelParticipant = $MadelineProto->channels->getParticipant(['channel' => InputChannel, 'user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
channels_ChannelParticipant = channels.getParticipant({channel=InputChannel, user_id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PARTICIPANT_ID_INVALID|The specified participant ID is invalid|
|400|USER_ID_INVALID|The provided user ID is invalid|
|400|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


