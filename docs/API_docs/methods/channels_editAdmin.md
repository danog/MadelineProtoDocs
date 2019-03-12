---
title: channels.editAdmin
description: Edit admin permissions of a user in a channel/supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.editAdmin  
[Back to methods index](index.md)


Edit admin permissions of a user in a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user | Optional|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Admin rights | Yes|


### Return type: [Updates](../types/Updates.md)

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

$Updates = $MadelineProto->channels->editAdmin(['channel' => InputChannel, 'user_id' => InputUser, 'admin_rights' => ChatAdminRights, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - channels.editAdmin
* params - `{"channel": InputChannel, "user_id": InputUser, "admin_rights": ChatAdminRights, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.editAdmin`

Parameters:

channel - Json encoded InputChannel

user_id - Json encoded InputUser

admin_rights - Json encoded ChatAdminRights




Or, if you're into Lua:

```lua
Updates = channels.editAdmin({channel=InputChannel, user_id=InputUser, admin_rights=ChatAdminRights, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|ADMINS_TOO_MUCH|Too many admins|
|BOT_CHANNELS_NA|Bots can't edit admin privileges|
|CHANNEL_INVALID|The provided channel is invalid|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|USER_CREATOR|You can't leave this channel, because you're its creator|
|USER_ID_INVALID|The provided user ID is invalid|
|USER_NOT_MUTUAL_CONTACT|The provided user is not a mutual contact|
|CHAT_ADMIN_INVITE_REQUIRED|You do not have the rights to do this|
|RIGHT_FORBIDDEN|Your admin rights do not allow you to do this|
|USER_PRIVACY_RESTRICTED|The user's privacy settings do not allow you to do this|


