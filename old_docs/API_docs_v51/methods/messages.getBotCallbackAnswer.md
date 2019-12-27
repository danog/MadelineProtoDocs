---
title: messages.getBotCallbackAnswer
description: Press an inline callback button and get a callback answer from the bot
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getBotCallbackAnswer.html
---
# Method: messages.getBotCallbackAnswer  
[Back to methods index](index.md)


Press an inline callback button and get a callback answer from the bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where was the inline keyboard sent | Optional|
|msg\_id|[int](../types/int.md) | ID of the Message with the inline keyboard | Yes|
|data|[bytes](../types/bytes.md) | Callback data | Yes|


### Return type: [messages.BotCallbackAnswer](../types/messages.BotCallbackAnswer.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.BotCallbackAnswer = $MadelineProto->messages->getBotCallbackAnswer(['peer' => InputPeer, 'msg_id' => int, 'data' => 'bytes', ]);
```

Or, if you're into Lua:

```lua
messages.BotCallbackAnswer = messages.getBotCallbackAnswer({peer=InputPeer, msg_id=int, data='bytes', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|DATA_INVALID|Encrypted data invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


