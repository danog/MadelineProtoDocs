---
title: "messages.sendQuickReplyMessages"
description: "Send a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendQuickReplyMessages.html
---
# Method: messages.sendQuickReplyMessages
[Back to methods index](index.html)



Send a [quick reply shortcut »](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where to send the shortcut (users only, for now). | Optional|
|shortcut\_id|[int](/API_docs/types/int.html) | The ID of the quick reply shortcut to send. | Optional|
|id|Array of [int](/API_docs/types/int.html) | Specify a subset of messages from the shortcut to send; if empty, defaults to all of them. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendQuickReplyMessages(peer: $InputPeer, shortcut_id: $int, id: [$int, $int], );
```

