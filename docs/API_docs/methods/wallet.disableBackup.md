---
title: "wallet.disableBackup"
description: "wallet.disableBackup parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_disableBackup.html
---
# Method: wallet.disableBackup
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|password|[InputCheckPasswordSRP](/API_docs/types/InputCheckPasswordSRP.html) | Optional|
|new\_public\_key|[bytes](/API_docs/types/bytes.html) | Optional|
|proof|[WalletOwnershipProof](/API_docs/types/WalletOwnershipProof.html) | Optional|


### Return type: [WalletState](/API_docs/types/WalletState.html)

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

$WalletState = $MadelineProto->wallet->disableBackup(password: $InputCheckPasswordSRP, new_public_key: 'bytes', proof: $WalletOwnershipProof, );
```

