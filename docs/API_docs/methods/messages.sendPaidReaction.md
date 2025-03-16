---
title: "messages.sendPaidReaction"
description: "Sends one or more [paid Telegram Star reactions »](https://core.telegram.org/api/reactions#paid-reactions), transferring [Telegram Stars »](https://core.telegram.org/api/stars) to a channel's balance."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendPaidReaction.html
---
# Method: messages.sendPaidReaction
[Back to methods index](index.html)



Sends one or more [paid Telegram Star reactions »](https://core.telegram.org/api/reactions#paid-reactions), transferring [Telegram Stars »](https://core.telegram.org/api/stars) to a channel's balance.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel | Optional|
|msg\_id|[int](/API_docs/types/int.html) | The message to react to | Optional|
|count|[int](/API_docs/types/int.html) | The number of [stars](https://core.telegram.org/api/stars) to send (each will increment the reaction counter by one). | Optional|
|private|[PaidReactionPrivacy](/API_docs/types/PaidReactionPrivacy.html) |  | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->messages->sendPaidReaction(peer: $InputPeer, msg_id: $int, count: $int, private: $PaidReactionPrivacy, );
```

