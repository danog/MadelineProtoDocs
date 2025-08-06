---
title: "messages.deleteSavedHistory"
description: "Deletes messages forwarded from a specific peer to [saved messages »](https://core.telegram.org/api/saved-messages)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteSavedHistory.html
---
# Method: messages.deleteSavedHistory
[Back to methods index](index.html)



Deletes messages forwarded from a specific peer to [saved messages »](https://core.telegram.org/api/saved-messages).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|parent\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) |  | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Peer, whose messages will be deleted from [saved messages »](https://core.telegram.org/api/saved-messages) | Optional|
|max\_id|[int](/API_docs/types/int.html) | Maximum ID of message to delete | Optional|
|min\_date|[int](/API_docs/types/int.html) | Delete all messages newer than this UNIX timestamp | Optional|
|max\_date|[int](/API_docs/types/int.html) | Delete all messages older than this UNIX timestamp | Optional|


### Return type: [messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)

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

$messages_AffectedHistory = $MadelineProto->messages->deleteSavedHistory(parent_peer: $InputPeer, peer: $InputPeer, max_id: $int, min_date: $int, max_date: $int, );
```

