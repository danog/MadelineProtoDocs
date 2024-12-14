---
title: "messages.reportReaction"
description: "Report a [message reaction](https://core.telegram.org/api/reactions)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reportReaction.html
---
# Method: messages.reportReaction
[Back to methods index](index.html)



Report a [message reaction](https://core.telegram.org/api/reactions)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the message was sent | Optional|
|id|[int](/API_docs/types/int.html) | Message ID | Optional|
|reaction\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer that sent the reaction | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->messages->reportReaction(peer: $InputPeer, id: $int, reaction_peer: $InputPeer, );
```

