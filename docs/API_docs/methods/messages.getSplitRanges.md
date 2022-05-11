---
title: "messages.getSplitRanges"
description: "Get message ranges for saving the user's chat history"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSplitRanges.html
---
# Method: messages.getSplitRanges
[Back to methods index](index.html)



Get message ranges for saving the user's chat history



### Return type: [Vector\_of\_MessageRange](/API_docs/types/MessageRange.html)

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
$Vector_of_MessageRange = $MadelineProto->messages->getSplitRanges();
```

