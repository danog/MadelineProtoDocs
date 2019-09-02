---
title: messages.getBotCallbackAnswer
description: Get the callback answer of a bot (after clicking a button)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getBotCallbackAnswer  
[Back to methods index](index.md)


Get the callback answer of a bot (after clicking a button)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat | Optional|
|msg\_id|[int](../types/int.md) | The message ID | Yes|
|data|[bytes](../types/bytes.md) | The data to send to the bot | Yes|


### Return type: [messages\_BotCallbackAnswer](../types/messages_BotCallbackAnswer.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_BotCallbackAnswer = $MadelineProto->messages->getBotCallbackAnswer(['peer' => InputPeer, 'msg_id' => int, 'data' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
messages_BotCallbackAnswer = messages.getBotCallbackAnswer({peer=InputPeer, msg_id=int, data='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|DATA_INVALID|Encrypted data invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|-503|Timeout|Timeout while fetching data|


