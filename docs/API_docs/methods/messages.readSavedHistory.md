---
title: "messages.readSavedHistory"
description: "Mark messages as read in a [monoforum topic »](https://core.telegram.org/api/monoforum)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_readSavedHistory.html
---
# Method: messages.readSavedHistory
[Back to methods index](index.html)



Mark messages as read in a [monoforum topic »](https://core.telegram.org/api/monoforum).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | ID of the monoforum group. | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | ID of the topic. | Optional|
|max\_id|[int](/API_docs/types/int.html) | If a positive value is passed, only messages with identifiers less or equal than the given one will be read. | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->messages->readSavedHistory(parent_peer: $InputPeer, peer: $InputPeer, max_id: $int, );
```

