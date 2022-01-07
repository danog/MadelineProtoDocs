---
title: "messages.sendReaction"
description: "Send reaction to message"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendReaction.html
---
# Method: messages.sendReaction
[Back to methods index](index.html)



Send reaction to message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID to react to | Yes|
|reaction|[string](/API_docs/types/string.html) | Reaction (a UTF8 emoji) | Optional|


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

$Updates = $MadelineProto->messages->sendReaction(['peer' => InputPeer, 'msg_id' => int, 'reaction' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|MESSAGE_ID_INVALID|The provided message id is invalid|
|400|REACTION_EMPTY|Empty reaction provided|


