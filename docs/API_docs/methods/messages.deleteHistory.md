---
title: "messages.deleteHistory"
description: "Deletes communication history."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteHistory.html
---
# Method: messages.deleteHistory
[Back to methods index](index.html)



Deletes communication history.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|just\_clear|[Bool](/API_docs/types/Bool.html) | Just clear history for the current user, without actually removing messages for every chat user | Optional|
|revoke|[Bool](/API_docs/types/Bool.html) | Whether to delete the message history for all chat participants | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | User or chat, communication history of which will be deleted | Optional|
|max\_id|[int](/API_docs/types/int.html) | Maximum ID of message to delete | Yes|
|min\_date|[int](/API_docs/types/int.html) | Delete all messages newer than this UNIX timestamp | Optional|
|max\_date|[int](/API_docs/types/int.html) | Delete all messages older than this UNIX timestamp | Optional|


### Return type: [messages.AffectedHistory](/API_docs/types/messages.AffectedHistory.html)

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
$messages_AffectedHistory = $MadelineProto->messages->deleteHistory(just_clear: Bool, revoke: Bool, peer: InputPeer, max_id: int, min_date: int, max_date: int, );
```

