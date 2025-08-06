---
title: "messages.deleteQuickReplyShortcut"
description: "Completely delete a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts).  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_deleteQuickReplyShortcut.html
---
# Method: messages.deleteQuickReplyShortcut
[Back to methods index](index.html)



Completely delete a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts).  
This will also emit an [updateDeleteQuickReply](../constructors/updateDeleteQuickReply.html) update to other logged-in sessions (and *no* [updateDeleteQuickReplyMessages](../constructors/updateDeleteQuickReplyMessages.html) updates, even if all the messages in the shortcuts are also deleted by this method).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|shortcut\_id|[int](/API_docs/types/int.html) | [Shortcut ID](https://core.telegram.org/api/business#quick-reply-shortcuts) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->messages->deleteQuickReplyShortcut(shortcut_id: $int, );
```

