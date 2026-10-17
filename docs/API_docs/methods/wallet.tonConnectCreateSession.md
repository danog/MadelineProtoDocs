---
title: "wallet.tonConnectCreateSession"
description: "wallet.tonConnectCreateSession parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_tonConnectCreateSession.html
---
# Method: wallet.tonConnectCreateSession
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dapp\_client\_id|[string](/API_docs/types/string.html) | Optional|
|manifest\_url|[string](/API_docs/types/string.html) | Optional|


### Return type: [TonConnectSession](/API_docs/types/TonConnectSession.html)

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

$TonConnectSession = $MadelineProto->wallet->tonConnectCreateSession(dapp_client_id: 'string', manifest_url: 'string', );
```

