---
title: "messages.getSavedDialogs"
description: "Returns the current [saved dialog list »](https://core.telegram.org/api/saved-messages) or [monoforum topic list »](https://core.telegram.org/api/monoforum)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSavedDialogs.html
---
# Method: messages.getSavedDialogs
[Back to methods index](index.html)



Returns the current [saved dialog list »](https://core.telegram.org/api/saved-messages) or [monoforum topic list »](https://core.telegram.org/api/monoforum).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_pinned|[Bool](/API_docs/types/Bool.html) | Exclude pinned dialogs | Optional|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | If set, fetches the topic list of the passed monoforum, otherwise fetches the saved dialog list. | Optional|
|offset\_date|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Optional|
|offset\_id|[int](/API_docs/types/int.html) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) (`top_message` ID used for pagination) | Optional|
|offset\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | [Offset peer for pagination](https://core.telegram.org/api/offsets) | Optional|
|limit|[int](/API_docs/types/int.html) | Number of list elements to be returned | Optional|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation) | Optional|


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

$messages_SavedDialogs = $MadelineProto->messages->getSavedDialogs(exclude_pinned: $Bool, parent_peer: $InputPeer, offset_date: $int, offset_id: $int, offset_peer: $InputPeer, limit: $int, hash: [$long\|string, $long\|string], );
```

