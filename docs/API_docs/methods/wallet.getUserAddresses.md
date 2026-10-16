---
title: "wallet.getUserAddresses"
description: "wallet.getUserAddresses parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_getUserAddresses.html
---
# Method: wallet.getUserAddresses
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|force|[Bool](/API_docs/types/Bool.html) | Optional|
|id|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Yes|


### Return type: [Vector\_of\_WalletUserAddress](/API_docs/types/WalletUserAddress.html)

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

$Vector_of_WalletUserAddress = $MadelineProto->wallet->getUserAddresses(force: $Bool, id: [$InputUser, $InputUser], );
```

