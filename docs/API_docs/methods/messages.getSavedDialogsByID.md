---
title: "messages.getSavedDialogsByID"
description: "Obtain information about specific [saved message dialogs »](https://core.telegram.org/api/saved-messages#saved-message-dialogs) or [monoforum topics »](https://core.telegram.org/api/monoforum)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedDialogsByID.html
---
# Method: messages.getSavedDialogsByID
[Back to methods index](index.html)



Obtain information about specific [saved message dialogs »](https://core.telegram.org/api/saved-messages#saved-message-dialogs) or [monoforum topics »](https://core.telegram.org/api/monoforum).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, fetches [monoforum topics »](https://core.telegram.org/api/monoforum), otherwise fetches [saved message dialogs »](https://core.telegram.org/api/saved-messages#saved-message-dialogs). | Optional|
|ids|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | IDs of dialogs (topics) to fetch. | Yes|


### Return type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)

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

$messages_SavedDialogs = $MadelineProto->messages->getSavedDialogsByID(parent_peer: $InputPeer, ids: [$InputPeer, $InputPeer], );
```

