---
title: "messages.search"
description: "Returns found messages"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_search.html
---
# Method: messages.search
[Back to methods index](index.html)



Returns found messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | User or chat, histories with which are searched, or [(inputPeerEmpty)](../constructors/inputPeerEmpty.html) constructor for global search | Optional|
|q|[string](/API_docs/types/string.html) | Text search request | Yes|
|from\_id|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Only return messages sent by the specified user ID | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | [Thread ID](https://core.telegram.org/api/threads) | Optional|
|filter|[MessagesFilter](/API_docs/types/MessagesFilter.html) | Filter to return only specified message types | Optional|
|min\_date|[int](/API_docs/types/int.html) | If a positive value was transferred, only messages with a sending date bigger than the transferred one will be returned | Optional|
|max\_date|[int](/API_docs/types/int.html) | If a positive value was transferred, only messages with a sending date smaller than the transferred one will be returned | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Only return messages starting from the specified message ID | Optional|
|add\_offset|[int](/API_docs/types/int.html) | [Additional offset](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | [Number of results to return](https://core.telegram.org/api/offsets) | Optional|
|max\_id|[int](/API_docs/types/int.html) | [Maximum message ID to return](https://core.telegram.org/api/offsets) | Optional|
|min\_id|[int](/API_docs/types/int.html) | [Minimum message ID to return](https://core.telegram.org/api/offsets) | Optional|
|hash|Array of [long](/API_docs/types/long.html) | [Hash](https://core.telegram.org/api/offsets) | Optional|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Messages = $MadelineProto->messages->search(peer: InputPeer, q: 'string', from_id: InputPeer, top_msg_id: int, filter: MessagesFilter, min_date: int, max_date: int, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: [long, long], );
```

