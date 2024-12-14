---
title: "account.reorderUsernames"
description: "Reorder usernames associated with the currently logged-in user."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_reorderUsernames.html
---
# Method: account.reorderUsernames
[Back to methods index](index.html)



Reorder usernames associated with the currently logged-in user.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|order|Array of [string](/API_docs/types/string.html) | The new order for active usernames. All active usernames must be specified. | Yes|


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

$Bool = $MadelineProto->account->reorderUsernames(order: ['string', 'string'], );
```

