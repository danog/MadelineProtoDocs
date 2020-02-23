---
title: channels.editAdmin
description: Modify the admin rights of a user in a [supergroup/channel](https://core.telegram.org/api/channel).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editAdmin.html
---
# Method: channels.editAdmin  
[Back to methods index](index.md)


Modify the admin rights of a user in a [supergroup/channel](https://core.telegram.org/api/channel).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The [supergroup/channel](https://core.telegram.org/api/channel). | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The ID of the user whose admin rights should be modified | Optional|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | The admin rights | Yes|
|rank|[string](../types/string.md) | Indicates the role (rank) of the admin in the group: just an arbitrary string | Yes|


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

$Updates = $MadelineProto->channels->editAdmin(['channel' => InputChannel, 'user_id' => InputUser, 'admin_rights' => ChatAdminRights, 'rank' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = channels.editAdmin({channel=InputChannel, user_id=InputUser, admin_rights=ChatAdminRights, rank='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ADMINS_TOO_MUCH|There are too many admins|
|400|BOT_CHANNELS_NA|Bots can't edit admin privileges|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|USER_CREATOR|You can't leave this channel, because you're its creator|
|400|USER_ID_INVALID|The provided user ID is invalid|
|400|USER_NOT_MUTUAL_CONTACT|The provided user is not a mutual contact|
|403|CHAT_ADMIN_INVITE_REQUIRED|You do not have the rights to do this|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|
|403|RIGHT_FORBIDDEN|Your admin rights do not allow you to do this|
|403|USER_PRIVACY_RESTRICTED|The user's privacy settings do not allow you to do this|
|403|USER_RESTRICTED|You're spamreported, you can't create channels or chats.|


