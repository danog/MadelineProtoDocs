---
title: messages.deleteHistory
description: Deletes communication history.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.deleteHistory  
[Back to methods index](index.md)


Deletes communication history.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | User or chat, communication history of which will be deleted | Optional|
|offset|[int](../types/int.md) | Offset | Yes|


### Return type: [messages\_AffectedHistory](../types/messages_AffectedHistory.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->messages->deleteHistory(['peer' => InputPeer, 'offset' => int, ]);
```

Or, if you're into Lua:

```lua
messages_AffectedHistory = messages.deleteHistory({peer=InputPeer, offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|


