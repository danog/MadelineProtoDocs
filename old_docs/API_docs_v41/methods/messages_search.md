---
title: messages.search
description: Search peers or messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.search  
[Back to methods index](index.md)


Search peers or messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|important\_only|[Bool](../types/Bool.md) | Show only important messages | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to search | Optional|
|q|[string](../types/string.md) | What to search | Yes|
|filter|[MessagesFilter](../types/MessagesFilter.md) | Message filter | Optional|
|min\_date|[int](../types/int.md) | Minumum date of results to fetch | Yes|
|max\_date|[int](../types/int.md) | Maximum date of results to fetch | Yes|
|offset|[int](../types/int.md) | Offset  | Yes|
|max\_id|[int](../types/int.md) | Maximum message id to return | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [messages\_Messages](../types/messages_Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->search(['important_only' => Bool, 'peer' => InputPeer, 'q' => 'string', 'filter' => MessagesFilter, 'min_date' => int, 'max_date' => int, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.search({important_only=Bool, peer=InputPeer, q='string', filter=MessagesFilter, min_date=int, max_date=int, offset=int, max_id=int, limit=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|INPUT_CONSTRUCTOR_INVALID|The provided constructor is invalid|
|INPUT_USER_DEACTIVATED|The specified user was deleted|
|PEER_ID_INVALID|The provided peer id is invalid|
|PEER_ID_NOT_SUPPORTED|The provided peer ID is not supported|
|SEARCH_QUERY_EMPTY|The search query is empty|
|USER_ID_INVALID|The provided user ID is invalid|


