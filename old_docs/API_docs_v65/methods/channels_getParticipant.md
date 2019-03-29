---
title: channels.getParticipant
description: Get info about a certain channel/supergroup participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getParticipant  
[Back to methods index](index.md)


Get info about a certain channel/supergroup participant

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user to fetch info about | Optional|


### Return type: [channels\_ChannelParticipant](../types/channels_ChannelParticipant.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$channels_ChannelParticipant = $MadelineProto->channels->getParticipant(['channel' => InputChannel, 'user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
channels_ChannelParticipant = channels.getParticipant({channel=InputChannel, user_id=InputUser, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|USER_ID_INVALID|The provided user ID is invalid|
|USER_NOT_PARTICIPANT|You're not a member of this supergroup/channel|


