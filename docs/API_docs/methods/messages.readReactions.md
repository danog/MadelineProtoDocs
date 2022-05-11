---
title: "messages.readReactions"
description: "Mark [message reactions »](https://core.telegram.org/api/reactions) as read"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readReactions.html
---
# Method: messages.readReactions
[Back to methods index](index.html)



Mark [message reactions »](https://core.telegram.org/api/reactions) as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|


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

// PHP 8+ syntax, use an array on PHP 7.
$messages_AffectedHistory = $MadelineProto->messages->readReactions(peer: InputPeer, );
```

