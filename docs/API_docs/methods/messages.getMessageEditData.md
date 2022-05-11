---
title: "messages.getMessageEditData"
description: "Find out if a media message's caption can be edited"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessageEditData.html
---
# Method: messages.getMessageEditData
[Back to methods index](index.html)



Find out if a media message's caption can be edited

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the media was sent | Optional|
|id|[int](/API_docs/types/int.html) | ID of message | Yes|


### Return type: [messages.MessageEditData](/API_docs/types/messages.MessageEditData.html)

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
$messages_MessageEditData = $MadelineProto->messages->getMessageEditData(peer: InputPeer, id: int, );
```

