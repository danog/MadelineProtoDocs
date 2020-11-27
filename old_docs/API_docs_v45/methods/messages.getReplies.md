---
title: messages.getReplies
description: messages.getReplies parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getReplies.html
---
# Method: messages.getReplies
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|
|msg\_id|[int](../types/int.md) | Yes|
|offset\_id|[int](../types/int.md) | Yes|
|offset\_date|[int](../types/int.md) | Yes|
|add\_offset|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|
|max\_id|[int](../types/int.md) | Yes|
|min\_id|[int](../types/int.md) | Yes|
|hash|Array of [int](../types/int.md) | Optional|


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

$messages_Messages = $MadelineProto->messages->getReplies(['peer' => InputPeer, 'msg_id' => int, 'offset_id' => int, 'offset_date' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getReplies({peer=InputPeer, msg_id=int, offset_id=int, offset_date=int, add_offset=int, limit=int, max_id=int, min_id=int, hash={int}, })
```

