---
title: "messages.toggleSavedDialogPin"
description: "messages.toggleSavedDialogPin parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_toggleSavedDialogPin.html
---
# Method: messages.toggleSavedDialogPin
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[InputDialogPeer](/API_docs/types/InputDialogPeer.html) | Yes|


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

$Bool = $MadelineProto->messages->toggleSavedDialogPin(pinned: $Bool, peer: $InputDialogPeer, );
```

