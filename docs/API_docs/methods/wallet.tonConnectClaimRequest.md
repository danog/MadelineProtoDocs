---
title: "wallet.tonConnectClaimRequest"
description: "wallet.tonConnectClaimRequest parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/wallet_tonConnectClaimRequest.html
---
# Method: wallet.tonConnectClaimRequest
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|declined|[Bool](/API_docs/types/Bool.html) | Optional|
|session\_id|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Optional|
|app\_request\_id|[string](/API_docs/types/string.html) | Optional|
|challenge\_answer|[bytes](/API_docs/types/bytes.html) | Optional|


### Return type: [Bool](/API_docs/types/Bool.html)

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

$Bool = $MadelineProto->wallet->tonConnectClaimRequest(declined: $Bool, session_id: $long, msg_id: $int, app_request_id: 'string', challenge_answer: 'bytes', );
```

