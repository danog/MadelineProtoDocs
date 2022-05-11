---
title: "messages.toggleDialogPin"
description: "Pin/unpin a dialog"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleDialogPin.html
---
# Method: messages.toggleDialogPin
[Back to methods index](index.html)



Pin/unpin a dialog

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Whether to pin or unpin the dialog | Optional|
|peer|[Username, chat ID, Update, Message or InputDialogPeer](/API_docs/types/InputDialogPeer.html) | The dialog to pin | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->toggleDialogPin(pinned: Bool, peer: InputDialogPeer, );
```

