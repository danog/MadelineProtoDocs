---
title: "messages.getQuickReplies"
description: "Fetch basic info about all existing [quick reply shortcuts](https://core.telegram.org/api/business#quick-reply-shortcuts)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getQuickReplies.html
---
# Method: messages.getQuickReplies
[Back to methods index](index.html)



Fetch basic info about all existing [quick reply shortcuts](https://core.telegram.org/api/business#quick-reply-shortcuts).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | Hash for pagination, generated as specified [here »](https://core.telegram.org/api/business#quick-reply-shortcuts) (not the usual algorithm used for hash generation.) | Optional|


### Return type: [messages.QuickReplies](/API_docs/types/messages.QuickReplies.html)

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

$messages_QuickReplies = $MadelineProto->messages->getQuickReplies(hash: [$long\|string, $long\|string], );
```

