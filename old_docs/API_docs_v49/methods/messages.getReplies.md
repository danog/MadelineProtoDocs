---
title: messages.getReplies
description: Get messages in a reply thread
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getReplies.html
---
# Method: messages.getReplies
[Back to methods index](index.md)



Get messages in a reply thread

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|msg\_id|[int](../types/int.md) | Message ID | Yes|
|offset\_id|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_date|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|add\_offset|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|max\_id|[int](../types/int.md) | If a positive value was transferred, the method will return only messages with ID smaller than max\_id | Yes|
|min\_id|[int](../types/int.md) | If a positive value was transferred, the method will return only messages with ID bigger than min\_id | Yes|
|hash|Array of [int](../types/int.md) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


### Return type: [messages.Messages](../types/messages.Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getReplies(['peer' => InputPeer, 'msg_id' => int, 'offset_id' => int, 'offset_date' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getReplies({peer=InputPeer, msg_id=int, offset_id=int, offset_date=int, add_offset=int, limit=int, max_id=int, min_id=int, hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|


