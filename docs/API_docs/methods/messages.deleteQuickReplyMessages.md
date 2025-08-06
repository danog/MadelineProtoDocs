---
title: "messages.deleteQuickReplyMessages"
description: "Delete one or more messages from a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts). This will also emit an [updateDeleteQuickReplyMessages](../constructors/updateDeleteQuickReplyMessages.html) update."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteQuickReplyMessages.html
---
# Method: messages.deleteQuickReplyMessages
[Back to methods index](index.html)



Delete one or more messages from a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts). This will also emit an [updateDeleteQuickReplyMessages](../constructors/updateDeleteQuickReplyMessages.html) update.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | [Shortcut ID](https://core.telegram.org/api/business#quick-reply-shortcuts). | Optional|
|id|Array of [int](/API_docs/types/int.html) | IDs of shortcut messages to delete. | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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

$Updates = $MadelineProto->messages->deleteQuickReplyMessages(shortcut_id: $int, id: [$int, $int], );
```

