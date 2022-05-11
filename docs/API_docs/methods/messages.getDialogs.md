---
title: "messages.getDialogs"
description: "Returns the current user dialog list."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getDialogs.html
---
# Method: messages.getDialogs
[Back to methods index](index.html)



Returns the current user dialog list.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_pinned|[Bool](/API_docs/types/Bool.html) | Exclude pinned dialogs | Optional|
|folder\_id|[int](/API_docs/types/int.html) | [Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders) | Optional|
|offset\_date|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | [Offset peer for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Number of list elements to be returned | Yes|
|hash|[long](/API_docs/types/long.html) | [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Yes|


### Return type: [messages.Dialogs](/API_docs/types/messages.Dialogs.html)

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
$messages_Dialogs = $MadelineProto->messages->getDialogs(exclude_pinned: Bool, folder_id: int, offset_date: int, offset_id: int, offset_peer: InputPeer, limit: int, hash: long, );
```

