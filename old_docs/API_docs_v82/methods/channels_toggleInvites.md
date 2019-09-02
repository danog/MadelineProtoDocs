---
title: channels.toggleInvites
description: Allow or disallow any user to invite users to this channel/supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.toggleInvites  
[Back to methods index](index.md)


Allow or disallow any user to invite users to this channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|enabled|[Bool](../types/Bool.md) | Allow or disallow | Yes|


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

$Updates = $MadelineProto->channels->toggleInvites(['channel' => InputChannel, 'enabled' => Bool, ]);
```

Or, if you're into Lua:

```lua
Updates = channels.toggleInvites({channel=InputChannel, enabled=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|


