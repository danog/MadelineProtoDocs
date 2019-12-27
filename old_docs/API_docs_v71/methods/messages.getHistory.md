---
title: messages.getHistory
description: Gets back the conversation history with one interlocutor / within a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getHistory  
[Back to methods index](index.md)


Gets back the conversation history with one interlocutor / within a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Target peer | Optional|
|offset\_id|[int](../types/int.md) | Only return messages starting from the specified message ID | Yes|
|offset\_date|[int](../types/int.md) | Only return messages sent after the specified date | Yes|
|add\_offset|[int](../types/int.md) | Number of list elements to be skipped, negative values are also accepted. | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|
|max\_id|[int](../types/int.md) | If a positive value was transferred, the method will return only messages with IDs less than **max\_id** | Yes|
|min\_id|[int](../types/int.md) | If a positive value was transferred, the method will return only messages with IDs more than **min\_id** | Yes|


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

$messages.Messages = $MadelineProto->messages->getHistory(['peer' => InputPeer, 'offset_id' => int, 'offset_date' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Messages = messages.getHistory({peer=InputPeer, offset_id=int, offset_date=int, add_offset=int, limit=int, max_id=int, min_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ID_INVALID|The provided chat id is invalid|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|AUTH_KEY_PERM_EMPTY|The temporary auth key must be binded to the permanent auth key to use these methods.|
|-503|Timeout|Timeout while fetching data|


