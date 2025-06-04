---
title: "messages.getSavedDialogsByID"
description: "messages.getSavedDialogsByID parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedDialogsByID.html
---
# Method: messages.getSavedDialogsByID
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|ids|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Yes|


### Return type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)

### Can userbots use this method: **YES**

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_SavedDialogs = $MadelineProto->messages->getSavedDialogsByID(parent_peer: $InputPeer, ids: [$InputPeer, $InputPeer], );
```

