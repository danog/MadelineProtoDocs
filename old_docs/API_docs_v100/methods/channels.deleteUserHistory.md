---
title: channels.deleteUserHistory
description: Delete all messages sent by a certain user in a [supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteUserHistory.html
---
# Method: channels.deleteUserHistory  
[Back to methods index](index.md)


Delete all messages sent by a certain user in a [supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Supergroup](https://core.telegram.org/api/channel) | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | User whose messages should be deleted | Optional|


### Return type: [messages.AffectedHistory](../types/messages.AffectedHistory.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.AffectedHistory = $MadelineProto->channels->deleteUserHistory(['channel' => InputChannel, 'user_id' => InputUser, ]);
```

Or, if you're into Lua:

```lua
messages.AffectedHistory = channels.deleteUserHistory({channel=InputChannel, user_id=InputUser, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|USER_ID_INVALID|The provided user ID is invalid|


