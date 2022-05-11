---
title: "messages.updateDialogFiltersOrder"
description: "Reorder [folders](https://core.telegram.org/api/folders)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_updateDialogFiltersOrder.html
---
# Method: messages.updateDialogFiltersOrder
[Back to methods index](index.html)



Reorder [folders](https://core.telegram.org/api/folders)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|order|Array of [int](/API_docs/types/int.html) | New [folder](https://core.telegram.org/api/folders) order | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

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
$Bool = $MadelineProto->messages->updateDialogFiltersOrder(order: [int, int], );
```

