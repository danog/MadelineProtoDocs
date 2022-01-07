---
title: "channels.deleteMessages"
description: "Delete messages in a [channel/supergroup](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_deleteMessages.html
---
# Method: channels.deleteMessages
[Back to methods index](index.html)



Delete messages in a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | [Channel/supergroup](https://core.telegram.org/api/channel) | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of messages to delete | Yes|


### Return type: [messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedMessages = $MadelineProto->channels->deleteMessages(['channel' => InputChannel, 'id' => [int, int], ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|MESSAGE_DELETE_FORBIDDEN|You can't delete one of the messages you tried to delete, most likely because it is a service message.|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


