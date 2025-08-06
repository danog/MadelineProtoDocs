---
title: "messages.getFactCheck"
description: "Fetch one or more [factchecks, see here »](https://core.telegram.org/api/factcheck) for the full flow."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getFactCheck.html
---
# Method: messages.getFactCheck
[Back to methods index](index.html)



Fetch one or more [factchecks, see here »](https://core.telegram.org/api/factcheck) for the full flow.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the messages were sent. | Optional|
|msg\_id|Array of [int](/API_docs/types/int.html) | Messages that have associated [factCheck](../constructors/factCheck.html) constructors with the `need_check` flag set. | Yes|


### Return type: [Vector\_of\_FactCheck](/API_docs/types/FactCheck.html)

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

$Vector_of_FactCheck = $MadelineProto->messages->getFactCheck(peer: $InputPeer, msg_id: [$int, $int], );
```

