---
title: "messages.getHistory"
description: "Gets back the conversation history with one interlocutor / within a chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getHistory.html
---
# Method: messages.getHistory
[Back to methods index](index.html)



Gets back the conversation history with one interlocutor / within a chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Target peer | Optional|
|offset\_id|[int](/API_docs/types/int.html) | Only return messages starting from the specified message ID | Yes|
|offset\_date|[int](/API_docs/types/int.html) | Only return messages sent before the specified date | Yes|
|add\_offset|[int](/API_docs/types/int.html) | Number of list elements to be skipped, negative values are also accepted. | Yes|
|limit|[int](/API_docs/types/int.html) | Number of results to return | Yes|
|max\_id|[int](/API_docs/types/int.html) | If a positive value was transferred, the method will return only messages with IDs less than **max\_id** | Yes|
|min\_id|[int](/API_docs/types/int.html) | If a positive value was transferred, the method will return only messages with IDs more than **min\_id** | Yes|
|hash|[long](/API_docs/types/long.html) | [Result hash](https://core.telegram.org/api/offsets) | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$messages_Messages = $MadelineProto->messages->getHistory(peer: InputPeer, offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: long, );
```

