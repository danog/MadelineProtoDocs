---
title: "account.changeAuthorizationSettings"
description: "account.changeAuthorizationSettings parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_changeAuthorizationSettings.html
---
# Method: account.changeAuthorizationSettings
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](../types/long.md) | Yes|
|encrypted\_requests\_disabled|[Bool](../types/Bool.md) | Optional|
|call\_requests\_disabled|[Bool](../types/Bool.md) | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->changeAuthorizationSettings(['hash' => long, 'encrypted_requests_disabled' => Bool, 'call_requests_disabled' => Bool, ]);
```

