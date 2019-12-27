---
title: messages.getPollResults
description: Get poll results
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getPollResults  
[Back to methods index](index.md)


Get poll results

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer where the poll was found | Optional|
|msg\_id|[int](../types/int.md) | Message ID of poll message | Yes|


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

$Updates = $MadelineProto->messages->getPollResults(['peer' => InputPeer, 'msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.getPollResults({peer=InputPeer, msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|


