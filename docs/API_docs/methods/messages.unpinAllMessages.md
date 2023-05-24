---
title: "messages.unpinAllMessages"
description: "[Unpin](https://core.telegram.org/api/pin) all pinned messages"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_unpinAllMessages.html
---
# Method: messages.unpinAllMessages
[Back to methods index](index.html)



[Unpin](https://core.telegram.org/api/pin) all pinned messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Chat where to unpin | Optional|
|top\_msg\_id|[int](/API_docs/types/int.html) | [Forum topic](https://core.telegram.org/api/forum#forum-topics) where to unpin | Optional|


### Return type: [messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_AffectedHistory = $MadelineProto->messages->unpinAllMessages(peer: InputPeer, top_msg_id: int, );
```

