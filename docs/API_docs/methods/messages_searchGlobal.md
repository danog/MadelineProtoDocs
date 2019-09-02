---
title: messages.searchGlobal
description: Global message search
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.searchGlobal  
[Back to methods index](index.md)


Global message search

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](../types/int.md) | Folder ID | Optional|
|q|[string](../types/string.md) | The query | Yes|
|offset\_rate|[int](../types/int.md) | Offset rate | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | 0 or the peer offset | Optional|
|offset\_id|[int](../types/int.md) | 0 or the message ID offset | Yes|
|limit|[int](../types/int.md) | The number of results to return | Yes|


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

$messages_Messages = $MadelineProto->messages->searchGlobal(['folder_id' => int, 'q' => 'string', 'offset_rate' => int, 'offset_peer' => InputPeer, 'offset_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Messages = messages.searchGlobal({folder_id=int, q='string', offset_rate=int, offset_peer=InputPeer, offset_id=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|SEARCH_QUERY_EMPTY|The search query is empty|


