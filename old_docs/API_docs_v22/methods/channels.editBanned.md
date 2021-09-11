---
title: channels.editBanned
description: Ban/unban/kick a user in a [supergroup/channel](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editBanned.html
---
# Method: channels.editBanned
[Back to methods index](index.md)



Ban/unban/kick a user in a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The [supergroup/channel](https://core.telegram.org/api/channel). | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The ID of the user whose banned rights should be modified | Optional|
|banned\_rights|[ChannelBannedRights](../types/ChannelBannedRights.md) |  | Yes|


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

$Updates = $MadelineProto->channels->editBanned(['channel' => InputChannel, 'user_id' => InputUser, 'banned_rights' => ChannelBannedRights, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.editBanned({channel=InputChannel, user_id=InputUser, banned_rights=ChannelBannedRights, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_ADD_INVALID|Internal error|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PARTICIPANT_ID_INVALID|The specified participant ID is invalid|
|400|PINNED_DIALOGS_TOO_MUCH|Too many pinned dialogs|
|400|USER_ADMIN_INVALID|You're not an admin|
|400|USER_ID_INVALID|The provided user ID is invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


