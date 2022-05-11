---
title: "messages.getMessagesViews"
description: "Get and increase the view counter of a message sent or forwarded from a [channel](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessagesViews.html
---
# Method: messages.getMessagesViews
[Back to methods index](index.html)



Get and increase the view counter of a message sent or forwarded from a [channel](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the message was found | Optional|
|id|Array of [int](/API_docs/types/int.html) | ID of message | Yes|
|increment|[Bool](/API_docs/types/Bool.html) | Whether to mark the message as viewed and increment the view counter | Yes|


### Return type: [messages.MessageViews](/API_docs/types/messages.MessageViews.html)

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
$messages_MessageViews = $MadelineProto->messages->getMessagesViews(peer: InputPeer, id: [int, int], increment: Bool, );
```

