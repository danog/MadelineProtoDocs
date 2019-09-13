---
title: channels.updateUsername
description: Update the username of a supergroup/channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.updateUsername  
[Back to methods index](index.md)


Update the username of a supergroup/channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|username|[string](../types/string.md) | The new username | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->updateUsername(['channel' => InputChannel, 'username' => 'string', ]);
```

Or, if you're into Lua:

```lua
Bool = channels.updateUsername({channel=InputChannel, username='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHANNELS_ADMIN_PUBLIC_TOO_MUCH|You're admin of too many public channels, make some channels private to change the username of this channel|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|USERNAME_INVALID|The provided username is not valid|
|400|USERNAME_NOT_MODIFIED|The username was not modified|
|400|USERNAME_OCCUPIED|The provided username is already occupied|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


