---
title: "messages.togglePaidReactionPrivacy"
description: "Changes the privacy of already sent [paid reactions](https://core.telegram.org/api/reactions#paid-reactions) on a specific message."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_togglePaidReactionPrivacy.html
---
# Method: messages.togglePaidReactionPrivacy
[Back to methods index](index.html)



Changes the privacy of already sent [paid reactions](https://core.telegram.org/api/reactions#paid-reactions) on a specific message.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The channel | Optional|
|msg\_id|[int](/API_docs/types/int.html) | The ID of the message to which we sent the paid reactions | Optional|
|private|[PaidReactionPrivacy](/API_docs/types/PaidReactionPrivacy.html) |  | Yes|


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

$Bool = $MadelineProto->messages->togglePaidReactionPrivacy(peer: $InputPeer, msg_id: $int, private: $PaidReactionPrivacy, );
```

