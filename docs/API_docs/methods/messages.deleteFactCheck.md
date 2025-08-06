---
title: "messages.deleteFactCheck"
description: "Delete a [fact-check](https://core.telegram.org/api/factcheck) from a message."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteFactCheck.html
---
# Method: messages.deleteFactCheck
[Back to methods index](index.html)



Delete a [fact-check](https://core.telegram.org/api/factcheck) from a message.

Can only be used by independent fact-checkers as specified by the [appConfig.can\_edit\_factcheck](https://core.telegram.org/api/config#can-edit-factcheck) configuration flag.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the message was sent. | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID | Optional|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->deleteFactCheck(peer: $InputPeer, msg_id: $int, );
```

