---
title: "messages.getDialogs"
description: "Returns the current user dialog list."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDialogs.html
---
# Method: messages.getDialogs
[Back to methods index](index.md)



Returns the current user dialog list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_pinned|[Bool](/API_docs/types/Bool.md) | Exclude pinned dialogs | Optional|
|folder\_id|[int](/API_docs/types/int.md) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Optional|
|offset\_date|[int](/API_docs/types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_id|[int](/API_docs/types/int.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.md) | [Offset peer for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.md) | Number of list elements to be returned | Yes|
|hash|[long](/API_docs/types/long.md) |  | Yes|


### Return type: [messages.Dialogs](/API_docs/types/messages.Dialogs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Dialogs = $MadelineProto->messages->getDialogs(['exclude_pinned' => Bool, 'folder_id' => int, 'offset_date' => int, 'offset_id' => int, 'offset_peer' => InputPeer, 'limit' => int, 'hash' => long, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|FOLDER_ID_INVALID|Invalid folder ID|
|400|INPUT_FETCH_FAIL|Failed deserializing TL payload|
|400|OFFSET_PEER_ID_INVALID|The provided offset peer is invalid|
|-3002|All workers are busy. Active_queries = X|All workers are busy. Active_queries = X|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|401|SESSION_PASSWORD_NEEDED|2FA is enabled, use a password to login|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


