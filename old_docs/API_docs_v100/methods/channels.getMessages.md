---
title: channels.getMessages
description: Get [channel/supergroup](https://core.telegram.org/api/channel) messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getMessages.html
---
# Method: channels.getMessages  
[Back to methods index](index.md)


Get [channel/supergroup](https://core.telegram.org/api/channel) messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel/supergroup | Optional|
|id|Array of [Message ID or InputMessage](../types/InputMessage.md) | The message IDs | Yes|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Messages = $MadelineProto->channels->getMessages(['channel' => InputChannel, 'id' => [InputMessage, InputMessage], ]);
```

Or, if you're into Lua:

```lua
messages.Messages = channels.getMessages({channel=InputChannel, id={InputMessage}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MESSAGE_IDS_EMPTY|No message ids were provided|
|-503|Timeout|Timeout while fetching data|


