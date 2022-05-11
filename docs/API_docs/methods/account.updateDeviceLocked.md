---
title: "account.updateDeviceLocked"
description: "When client-side passcode lock feature is enabled, will not show message texts in incoming [PUSH notifications](https://core.telegram.org/api/push-updates)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_updateDeviceLocked.html
---
# Method: account.updateDeviceLocked
[Back to methods index](index.html)



When client-side passcode lock feature is enabled, will not show message texts in incoming [PUSH notifications](https://core.telegram.org/api/push-updates).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|period|[int](/API_docs/types/int.html) | Inactivity period after which to start hiding message texts in [PUSH notifications](https://core.telegram.org/api/push-updates). | Yes|


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
$Bool = $MadelineProto->account->updateDeviceLocked(period: int, );
```

