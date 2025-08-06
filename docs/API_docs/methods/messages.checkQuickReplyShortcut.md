---
title: "messages.checkQuickReplyShortcut"
description: "Before offering the user the choice to add a message to a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts), to make sure that none of the limits specified [here »](https://core.telegram.org/api/business#quick-reply-shortcuts) were reached."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_checkQuickReplyShortcut.html
---
# Method: messages.checkQuickReplyShortcut
[Back to methods index](index.html)



Before offering the user the choice to add a message to a [quick reply shortcut](https://core.telegram.org/api/business#quick-reply-shortcuts), to make sure that none of the limits specified [here »](https://core.telegram.org/api/business#quick-reply-shortcuts) were reached.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|shortcut|[string](/API_docs/types/string.html) | Shorcut name (not ID!). | Optional|


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

$Bool = $MadelineProto->messages->checkQuickReplyShortcut(shortcut: 'string', );
```

