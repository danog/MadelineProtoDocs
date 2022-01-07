---
title: "messages.getPinnedDialogs"
description: "Get pinned dialogs"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getPinnedDialogs.html
---
# Method: messages.getPinnedDialogs
[Back to methods index](index.html)



Get pinned dialogs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](/API_docs/types/int.html) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Yes|


### Return type: [messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_PeerDialogs = $MadelineProto->messages->getPinnedDialogs(['folder_id' => int, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_INVALID|Invalid folder ID|


