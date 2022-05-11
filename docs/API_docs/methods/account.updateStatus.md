---
title: "account.updateStatus"
description: "Updates online user status."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateStatus.html
---
# Method: account.updateStatus
[Back to methods index](index.html)



Updates online user status.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offline|[Bool](/API_docs/types/Bool.html) | If [(boolTrue)](../constructors/boolTrue.html) is transmitted, user status will change to [(userStatusOffline)](../constructors/userStatusOffline.html). | Yes|


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
$Bool = $MadelineProto->account->updateStatus(offline: Bool, );
```

