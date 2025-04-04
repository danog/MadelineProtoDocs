---
title: "account.resetWebAuthorization"
description: "Log out an active web [telegram login](https://core.telegram.org/widgets/login) session"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resetWebAuthorization.html
---
# Method: account.resetWebAuthorization
[Back to methods index](index.html)



Log out an active web [telegram login](https://core.telegram.org/widgets/login) session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|Array of [long\|string](/API_docs/types/long\|string.html) | [Session](../constructors/webAuthorization.html) hash | Optional|


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

$Bool = $MadelineProto->account->resetWebAuthorization(hash: [$long\|string, $long\|string], );
```

