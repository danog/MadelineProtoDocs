---
title: messages.search
description: Gets back found messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_search.html
---
# Method: messages.search  
[Back to methods index](index.md)


Gets back found messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|important\_only|[Bool](../types/Bool.md) | Show only important messages | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | User or chat, histories with which are searched, or [(inputPeerEmpty)](../constructors/inputPeerEmpty.md) constructor for global search | Optional|
|q|[string](../types/string.md) | Text search request | Yes|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Filter to return only specified message types | Optional|
|min\_date|[int](../types/int.md) | If a positive value was transferred, only messages with a sending date bigger than the transferred one will be returned | Yes|
|max\_date|[int](../types/int.md) | If a positive value was transferred, only messages with a sending date smaller than the transferred one will be returned | Yes|
|offset|[int](../types/int.md) | Offset  | Yes|
|max\_id|[int](../types/int.md) | [Maximum message ID to return](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | [Number of results to return](https://core.telegram.org/api/offsets) | Yes|


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

$messages.Messages = $MadelineProto->messages->search(['important_only' => Bool, 'peer' => InputPeer, 'q' => 'string', 'filter' => MessagesFilter, 'min_date' => int, 'max_date' => int, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Messages = messages.search({important_only=Bool, peer=InputPeer, q='string', filter=MessagesFilter, min_date=int, max_date=int, offset=int, max_id=int, limit=int, })
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


