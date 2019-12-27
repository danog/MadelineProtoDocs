---
title: messages.searchGlobal
description: Search for messages and peers globally
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchGlobal.html
---
# Method: messages.searchGlobal  
[Back to methods index](index.md)


Search for messages and peers globally

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](../types/int.md) | Folder where to search | Optional|
|q|[string](../types/string.md) | Query | Yes|
|offset\_rate|[int](../types/int.md) | Initially 0, then set to the [`next_rate` parameter of messages.messagesSlice](../constructors/messages.messagesSlice.md) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|


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

$messages.Messages = $MadelineProto->messages->searchGlobal(['folder_id' => int, 'q' => 'string', 'offset_rate' => int, 'offset_peer' => InputPeer, 'offset_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Messages = messages.searchGlobal({folder_id=int, q='string', offset_rate=int, offset_peer=InputPeer, offset_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|SEARCH_QUERY_EMPTY|The search query is empty|


