---
title: "messages.searchGlobal"
description: "Search for messages and peers globally"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchGlobal.html
---
# Method: messages.searchGlobal
[Back to methods index](index.md)



Search for messages and peers globally

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](/API_docs/types/int.md) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Optional|
|q|[string](/API_docs/types/string.md) | Query | Yes|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.md) | Global search filter | Optional|
|min\_date|[int](/API_docs/types/int.md) | If a positive value was specified, the method will return only messages with date bigger than min\_date | Yes|
|max\_date|[int](/API_docs/types/int.md) | If a positive value was transferred, the method will return only messages with date smaller than max\_date | Yes|
|offset\_rate|[int](/API_docs/types/int.md) | Initially 0, then set to the [`next_rate` parameter of messages.messagesSlice](../constructors/messages.messagesSlice.md) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](/API_docs/types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](/API_docs/types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->searchGlobal(['folder_id' => int, 'q' => 'string', 'filter' => MessagesFilter, 'min_date' => int, 'max_date' => int, 'offset_rate' => int, 'offset_peer' => InputPeer, 'offset_id' => int, 'limit' => int, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_INVALID|Invalid folder ID|
|400|SEARCH_QUERY_EMPTY|The search query is empty|


