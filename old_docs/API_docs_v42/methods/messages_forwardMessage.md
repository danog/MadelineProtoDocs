---
title: messages.forwardMessage
description: Forward message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.forwardMessage  
[Back to methods index](index.md)


Forward message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | From where to forward the message | Optional|
|id|[int](../types/int.md) | The message ID | Yes|


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

$Updates = $MadelineProto->messages->forwardMessage(['peer' => InputPeer, 'id' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.forwardMessage({peer=InputPeer, id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|YOU_BLOCKED_USER|You blocked this user|


