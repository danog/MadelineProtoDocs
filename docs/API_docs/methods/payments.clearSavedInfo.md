---
title: "payments.clearSavedInfo"
description: "Clear saved payment information"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_clearSavedInfo.html
---
# Method: payments.clearSavedInfo
[Back to methods index](index.html)



Clear saved payment information

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|credentials|[Bool](/API_docs/types/Bool.html) | Remove saved payment credentials | Optional|
|info|[Bool](/API_docs/types/Bool.html) | Clear the last order settings saved by the user | Optional|


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
$Bool = $MadelineProto->payments->clearSavedInfo(credentials: Bool, info: Bool, );
```

