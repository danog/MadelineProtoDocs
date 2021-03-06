---
title: messages.sendScheduledMessages
description: Send scheduled messages right away
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendScheduledMessages.html
---
# Method: messages.sendScheduledMessages  
[Back to methods index](index.md)


Send scheduled messages right away

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|id|Array of [int](../types/int.md) | ID | Yes|


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

$Updates = $MadelineProto->messages->sendScheduledMessages(['peer' => InputPeer, 'id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendScheduledMessages({peer=InputPeer, id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


