---
title: channels.editTitle
description: Edit the title of a supergroup/channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.editTitle  
[Back to methods index](index.md)


Edit the title of a supergroup/channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|title|[string](../types/string.md) | The new channel/supergroup title | Yes|


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

$Updates = $MadelineProto->channels->editTitle(['channel' => InputChannel, 'title' => 'string', ]);
```

Or, if you're into Lua:

```lua
Updates = channels.editTitle({channel=InputChannel, title='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|


