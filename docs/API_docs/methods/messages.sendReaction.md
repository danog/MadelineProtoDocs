---
title: "messages.sendReaction"
description: "React to message"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendReaction.html
---
# Method: messages.sendReaction
[Back to methods index](index.html)



React to message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|big|[Bool](/API_docs/types/Bool.html) | Whether a bigger and longer reaction should be shown | Optional|
|add\_to\_recent|[Bool](/API_docs/types/Bool.html) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID to react to | Optional|
|reaction|Array of [Reaction](/API_docs/types/Reaction.html) |  | Optional|


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

$Updates = $MadelineProto->messages->sendReaction(big: Bool, add_to_recent: Bool, peer: InputPeer, msg_id: int, reaction: [Reaction, Reaction], );
```

