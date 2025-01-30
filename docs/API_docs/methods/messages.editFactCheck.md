---
title: "messages.editFactCheck"
description: "Edit/create a [fact-check](https://core.telegram.org/api/factcheck) on a message."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_editFactCheck.html
---
# Method: messages.editFactCheck
[Back to methods index](index.html)



Edit/create a [fact-check](https://core.telegram.org/api/factcheck) on a message.

Can only be used by independent fact-checkers as specified by the [appConfig.can\_edit\_factcheck](https://core.telegram.org/api/config#can-edit-factcheck) configuration flag.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer where the message was sent | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Message ID | Optional|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Fact-check (maximum UTF-8 length specified in [appConfig.factcheck\_length\_limit](https://core.telegram.org/api/config#factcheck-length-limit)). | Yes|


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

$Updates = $MadelineProto->messages->editFactCheck(peer: $InputPeer, msg_id: $int, text: $TextWithEntities, );
```

