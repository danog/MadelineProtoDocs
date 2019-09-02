---
title: messages.getHistory
description: Get previous messages of a group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getHistory  
[Back to methods index](index.md)


Get previous messages of a group

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | The chat | Optional|
|offset\_id|[int](../types/int.md) | The last fetched message ID, initially 0 | Yes|
|offset\_date|[int](../types/int.md) | The date of the last previously fetched message, initially 0 | Yes|
|add\_offset|[int](../types/int.md) | Additional offset, can be 0 | Yes|
|limit|[int](../types/int.md) | Number of messages to fetch | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID to fetch | Yes|
|min\_id|[int](../types/int.md) | Minumum message ID to fetch | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->getHistory(['peer' => InputPeer, 'offset_id' => int, 'offset_date' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getHistory({peer=InputPeer, offset_id=int, offset_date=int, add_offset=int, limit=int, max_id=int, min_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|-503|Timeout|Timeout while fetching data|


