---
title: "channels.deleteChannel"
description: "Delete a [channel/supergroup](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteChannel.html
---
# Method: channels.deleteChannel
[Back to methods index](index.html)



Delete a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Channel/supergroup](https://core.telegram.org/api/channel) to delete | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->deleteChannel(['channel' => InputChannel, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHANNEL_TOO_LARGE|Channel is too large to be deleted; this error is issued when trying to delete channels with more than 1000 members (subject to change)|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|CHAT_NOT_MODIFIED|The pinned message wasn't modified|
|406|CHANNEL_TOO_LARGE|Channel is too large to be deleted; this error is issued when trying to delete channels with more than 1000 members (subject to change)|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


