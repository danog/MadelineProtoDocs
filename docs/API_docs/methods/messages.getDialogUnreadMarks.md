---
title: "messages.getDialogUnreadMarks"
description: "Get dialogs manually marked as unread"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDialogUnreadMarks.html
---
# Method: messages.getDialogUnreadMarks
[Back to methods index](index.html)



Get dialogs manually marked as unread

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Can be equal to the ID of a monoforum, to fetch monoforum topics manually marked as unread. | Optional|


### Return type: [Vector\_of\_DialogPeer](/API_docs/types/DialogPeer.html)

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

$Vector_of_DialogPeer = $MadelineProto->messages->getDialogUnreadMarks(parent_peer: $InputPeer, );
```

