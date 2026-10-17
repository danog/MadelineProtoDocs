---
title: "wallet.getExistingWaltBalance"
description: "wallet.getExistingWaltBalance parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_getExistingWaltBalance.html
---
# Method: wallet.getExistingWaltBalance
[Back to methods index](index.html)





### Return type: [wallet.ExistingBalance](/API_docs/types/wallet.ExistingBalance.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$wallet_ExistingBalance = $MadelineProto->wallet->getExistingWaltBalance();
```

