---
title: "messages.sendVote"
description: "Vote in a [poll](../constructors/poll.html)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendVote.html
---
# Method: messages.sendVote
[Back to methods index](index.html)



Vote in a [poll](../constructors/poll.html)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The chat where the poll was sent | Optional|
|msg\_id|[int](/API_docs/types/int.html) | The message ID of the poll | Yes|
|options|Array of [bytes](/API_docs/types/bytes.html) | The options that were chosen | Yes|


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
$Updates = $MadelineProto->messages->sendVote(peer: InputPeer, msg_id: int, options: ['bytes', 'bytes'], );
```

