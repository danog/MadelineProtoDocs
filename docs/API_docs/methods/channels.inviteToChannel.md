---
title: "channels.inviteToChannel"
description: "Invite users to a channel/supergroup"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_inviteToChannel.html
---
# Method: channels.inviteToChannel
[Back to methods index](index.md)



Invite users to a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel/supergroup | Optional|
|users|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Users to invite | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->inviteToChannel(['channel' => InputChannel, 'users' => [InputUser, InputUser], ]);
```

Or, if you're into Lua:

```lua
Updates = channels.inviteToChannel({channel=InputChannel, users={InputUser}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BOT_GROUPS_BLOCKED|This bot can't be added to groups|
|400|BOTS_TOO_MUCH|There are too many bots in this chat/channel|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_INVALID|Invalid chat|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_BANNED_IN_CHANNEL|You're banned from sending messages in supergroups/channels|
|400|USER_BLOCKED|User blocked|
|400|USER_BOT|Bots can only be admins in channels.|
|400|USER_CHANNELS_TOO_MUCH|One of the users you tried to add is already in too many channels/supergroups|
|400|USER_ID_INVALID|The provided user ID is invalid|
|400|USER_KICKED|This user was kicked from this supergroup/channel|
|400|USER_NOT_MUTUAL_CONTACT|The provided user is not a mutual contact|
|400|USERS_TOO_MUCH|The maximum number of users has been exceeded (to create a chat, for example)|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|USER_CHANNELS_TOO_MUCH|One of the users you tried to add is already in too many channels/supergroups|
|403|USER_NOT_MUTUAL_CONTACT|The provided user is not a mutual contact|
|403|USER_PRIVACY_RESTRICTED|The user's privacy settings do not allow you to do this|
|-503|Timeout|Timeout while fetching data|


