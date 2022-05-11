---
title: "messages.getUnreadReactions"
description: "Get unread reactions to messages you sent"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getUnreadReactions.html
---
# Method: messages.getUnreadReactions
[Back to methods index](index.html)



Get unread reactions to messages you sent

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|add\_offset|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|
|max\_id|[int](/API_docs/types/int.html) | Only return reactions for messages up until this message ID | Yes|
|min\_id|[int](/API_docs/types/int.html) | Only return reactions for messages starting from this message ID | Yes|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_Messages = $MadelineProto->messages->getUnreadReactions(peer: InputPeer, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, );
```

