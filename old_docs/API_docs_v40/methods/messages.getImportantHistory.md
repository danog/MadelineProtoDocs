---
title: messages.getImportantHistory
description: Get important message history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getImportantHistory  
[Back to methods index](index.md)


Get important message history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer | Optional|
|max\_id|[int](../types/int.md) | Maximum message ID to fetch | Yes|
|min\_id|[int](../types/int.md) | Minumum message ID to fetch | Yes|
|limit|[int](../types/int.md) | Number of results to fetch | Yes|


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

$messages.Messages = $MadelineProto->messages->getImportantHistory(['peer' => InputPeer, 'max_id' => int, 'min_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Messages = messages.getImportantHistory({peer=InputPeer, max_id=int, min_id=int, limit=int, })
```

