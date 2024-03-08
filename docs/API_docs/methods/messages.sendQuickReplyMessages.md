---
title: "messages.sendQuickReplyMessages"
description: "messages.sendQuickReplyMessages parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendQuickReplyMessages.html
---
# Method: messages.sendQuickReplyMessages
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|shortcut\_id|[int](/API_docs/types/int.html) | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendQuickReplyMessages(peer: $InputPeer, shortcut_id: $int, );
```

