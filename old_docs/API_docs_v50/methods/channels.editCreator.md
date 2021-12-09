---
title: channels.editCreator
description: Transfer channel ownership
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_editCreator.html
---
# Method: channels.editCreator
[Back to methods index](index.md)



Transfer channel ownership

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | New channel owner | Optional|
|password|[InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md) | [2FA password](https://core.telegram.org/api/srp) of account | Yes|


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

$Updates = $MadelineProto->channels->editCreator(['channel' => InputChannel, 'user_id' => InputUser, 'password' => InputCheckPasswordSRP, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.editCreator({channel=InputChannel, user_id=InputUser, password=InputCheckPasswordSRP, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|PASSWORD_HASH_INVALID|The provided password hash is invalid|
|400|PASSWORD_MISSING|You must enable 2FA in order to transfer ownership of a channel|
|400|PASSWORD_TOO_FRESH_X|The password was modified less than 24 hours ago, try again in X seconds|
|400|SESSION_TOO_FRESH_X|This session was created less than 24 hours ago, try again in X seconds|
|400|SRP_ID_INVALID|Invalid SRP ID provided|
|400|USER_ID_INVALID|The provided user ID is invalid|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


