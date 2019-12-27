---
title: messages.sendVote
description: Vote in a [poll](../constructors/poll.md)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendVote  
[Back to methods index](index.md)


Vote in a [poll](../constructors/poll.md)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat where the poll was sent | Optional|
|msg\_id|[int](../types/int.md) | The message ID of the poll | Yes|
|options|Array of [bytes](../types/bytes.md) | Options | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendVote(['peer' => InputPeer, 'msg_id' => int, 'options' => ['bytes', 'bytes'], ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendVote({peer=InputPeer, msg_id=int, options={'bytes'}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|MESSAGE_POLL_CLOSED|Poll closed|
|400|OPTION_INVALID|Invalid option selected|


