---
title: "messages.deleteMessages"
description: "Deletes messages by their identifiers."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteMessages.html
---
# Method: messages.deleteMessages
[Back to methods index](index.html)



Deletes messages by their identifiers.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|revoke|[Bool](/API_docs/types/Bool.html) | Whether to delete messages for all participants of the chat | Optional|
|id|Array of [int](/API_docs/types/int.html) | Message ID list | Yes|


### Return type: [messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_AffectedMessages = $MadelineProto->messages->deleteMessages(revoke: Bool, id: [int, int], );
```

