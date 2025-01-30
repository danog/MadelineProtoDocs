---
title: "messages.reorderQuickReplies"
description: "Reorder [quick reply shortcuts](https://core.telegram.org/api/business#quick-reply-shortcuts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_reorderQuickReplies.html
---
# Method: messages.reorderQuickReplies
[Back to methods index](index.html)



Reorder [quick reply shortcuts](https://core.telegram.org/api/business#quick-reply-shortcuts).

This will emit an [updateQuickReplies](../constructors/updateQuickReplies.html) update to other logged-in sessions.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|order|Array of [int](/API_docs/types/int.html) | IDs of all created [quick reply shortcuts](https://core.telegram.org/api/business#quick-reply-shortcuts), in the desired order. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->messages->reorderQuickReplies(order: [$int, $int], );
```

