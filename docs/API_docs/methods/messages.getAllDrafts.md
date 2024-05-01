---
title: "messages.getAllDrafts"
description: "Return all message [drafts](https://core.telegram.org/api/drafts).  "
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAllDrafts.html
---
# Method: messages.getAllDrafts
[Back to methods index](index.html)



Return all message [drafts](https://core.telegram.org/api/drafts).  
Returns all the latest [updateDraftMessage](../constructors/updateDraftMessage.html) updates related to all chats with drafts.



### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->getAllDrafts();
```

