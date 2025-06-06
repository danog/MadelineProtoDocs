---
title: "account.setAuthorizationTTL"
description: "Set time-to-live of current session"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_setAuthorizationTTL.html
---
# Method: account.setAuthorizationTTL
[Back to methods index](index.html)



Set time-to-live of current session

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|authorization\_ttl\_days|[int](/API_docs/types/int.html) | Time-to-live of current session in days | Optional|


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

$Bool = $MadelineProto->account->setAuthorizationTTL(authorization_ttl_days: $int, );
```

