---
title: "messages.searchGlobal"
description: "Search for messages and peers globally"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchGlobal.html
---
# Method: messages.searchGlobal
[Back to methods index](index.html)



Search for messages and peers globally

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcasts\_only|[Bool](/API_docs/types/Bool.html) | If set, only returns results from channels (used in the [global channel search tab »](https://core.telegram.org/api/search#global-search)). | Optional|
|groups\_only|[Bool](/API_docs/types/Bool.html) | Whether to search only in groups | Optional|
|users\_only|[Bool](/API_docs/types/Bool.html) | Whether to search only in private chats | Optional|
|folder\_id|[int](/API_docs/types/int.html) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Optional|
|q|[string](/API_docs/types/string.html) | Query | Optional|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Global search filter | Optional|
|min\_date|[int](/API_docs/types/int.html) | If a positive value was specified, the method will return only messages with date bigger than min\_date | Optional|
|max\_date|[int](/API_docs/types/int.html) | If a positive value was transferred, the method will return only messages with date smaller than max\_date | Optional|
|offset\_rate|[int](/API_docs/types/int.html) | Initially 0, then set to the [`next_rate` parameter of messages.messagesSlice](../constructors/messages.messagesSlice.html) | Optional|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->searchGlobal(broadcasts_only: $Bool, groups_only: $Bool, users_only: $Bool, folder_id: $int, q: 'string', filter: $MessagesFilter, min_date: $int, max_date: $int, offset_rate: $int, offset_peer: $InputPeer, offset_id: $int, limit: $int, );
```

