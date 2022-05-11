---
title: "messages.getSuggestedDialogFilters"
description: "Get [suggested folders](https://core.telegram.org/api/folders)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getSuggestedDialogFilters.html
---
# Method: messages.getSuggestedDialogFilters
[Back to methods index](index.html)



Get [suggested folders](https://core.telegram.org/api/folders)



### Return type: [Vector\_of\_DialogFilterSuggested](/API_docs/types/DialogFilterSuggested.html)

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
$Vector_of_DialogFilterSuggested = $MadelineProto->messages->getSuggestedDialogFilters();
```

