---
title: channels.exportInvite
description: Export the invite link of a channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.exportInvite  
[Back to methods index](index.md)


Export the invite link of a channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|


### Return type: [ExportedChatInvite](../types/ExportedChatInvite.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedChatInvite = $MadelineProto->channels->exportInvite(['channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
ExportedChatInvite = channels.exportInvite({channel=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INVITE_HASH_EXPIRED|The invite link has expired|


