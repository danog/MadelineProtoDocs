---
title: messages.getUnreadMentions
description: Get unread messages where we were mentioned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getUnreadMentions.html
---
# Method: messages.getUnreadMentions
[Back to methods index](index.md)



Get unread messages where we were mentioned

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Peer where to look for mentions | Optional|
|offset\_id|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|add\_offset|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|min\_id|[int](../types/int.md) | Minimum message ID to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


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

$messages_Messages = $MadelineProto->messages->getUnreadMentions(['peer' => InputPeer, 'offset_id' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.getUnreadMentions({peer=InputPeer, offset_id=int, add_offset=int, limit=int, max_id=int, min_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|-503|Timeout|Timeout while fetching data|


