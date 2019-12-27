---
title: messages.search
description: Gets back found messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.search  
[Back to methods index](index.md)


Gets back found messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | User or chat, histories with which are searched, or [(inputPeerEmpty)](../constructors/inputPeerEmpty.md) constructor for global search | Optional|
|q|[string](../types/string.md) | Text search request | Yes|
|from\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Only return messages sent by the specified user ID | Optional|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Filter to return only specified message types | Optional|
|min\_date|[int](../types/int.md) | If a positive value was transferred, only messages with a sending date bigger than the transferred one will be returned | Yes|
|max\_date|[int](../types/int.md) | If a positive value was transferred, only messages with a sending date smaller than the transferred one will be returned | Yes|
|offset\_id|[int](../types/int.md) | Only return messages starting from the specified message ID | Yes|
|add\_offset|[int](../types/int.md) | [Additional offset](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | [Number of results to return](https://core.telegram.org/api/offsets) | Yes|
|max\_id|[int](../types/int.md) | [Maximum message ID to return](https://core.telegram.org/api/offsets) | Yes|
|min\_id|[int](../types/int.md) | [Minimum message ID to return](https://core.telegram.org/api/offsets) | Yes|
|hash|Array of [int](../types/int.md) | The IDs of messages you already fetched | Optional|


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

$messages_Messages = $MadelineProto->messages->search(['peer' => InputPeer, 'q' => 'string', 'from_id' => InputUser, 'filter' => MessagesFilter, 'min_date' => int, 'max_date' => int, 'offset_id' => int, 'add_offset' => int, 'limit' => int, 'max_id' => int, 'min_id' => int, 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.search({peer=InputPeer, q='string', from_id=InputUser, filter=MessagesFilter, min_date=int, max_date=int, offset_id=int, add_offset=int, limit=int, max_id=int, min_id=int, hash={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|INPUT_CONSTRUCTOR_INVALID|The provided constructor is invalid|
|400|INPUT_USER_DEACTIVATED|The specified user was deleted|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|PEER_ID_NOT_SUPPORTED|The provided peer ID is not supported|
|400|SEARCH_QUERY_EMPTY|The search query is empty|
|400|USER_ID_INVALID|The provided user ID is invalid|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|


