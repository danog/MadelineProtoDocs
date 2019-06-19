---
title: channels.getImportantHistory
description: Get important channel/supergroup history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getImportantHistory  
[Back to methods index](index.md)


Get important channel/supergroup history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The supergroup/channel | Optional|
|offset\_id|[int](../types/int.md) | Message ID offset | Yes|
|add\_offset|[int](../types/int.md) | Additional offset | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID | Yes|
|min\_id|[int](../types/int.md) | Minumum message ID | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->channels->getImportantHistory(['channel' => InputChannel, 'offset_id' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = channels.getImportantHistory({channel=InputChannel, offset_id=int, add_offset=int, limit=int, max_id=int, min_id=int, })
```

