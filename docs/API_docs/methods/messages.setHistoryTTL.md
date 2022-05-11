---
title: "messages.setHistoryTTL"
description: "Set maximum Time-To-Live of all messages in the specified chat"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_setHistoryTTL.html
---
# Method: messages.setHistoryTTL
[Back to methods index](index.html)



Set maximum Time-To-Live of all messages in the specified chat

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The dialog | Optional|
|period|[int](/API_docs/types/int.html) | Automatically delete all messages sent in the chat after this many seconds | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->setHistoryTTL(peer: InputPeer, period: int, );
```

