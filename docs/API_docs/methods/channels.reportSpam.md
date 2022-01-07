---
title: "channels.reportSpam"
description: "Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_reportSpam.html
---
# Method: channels.reportSpam
[Back to methods index](index.md)



Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Supergroup | Optional|
|participant|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) |  | Optional|
|id|Array of [int](../types/int.md) | IDs of spam messages | Yes|


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

$Bool = $MadelineProto->channels->reportSpam(['channel' => InputChannel, 'participant' => InputPeer, 'id' => [int, int], ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|USER_ID_INVALID|The provided user ID is invalid|


