---
title: "account.registerPasskey"
description: "account.registerPasskey parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_registerPasskey.html
---
# Method: account.registerPasskey
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|credential|[InputPasskeyCredential](/API_docs/types/InputPasskeyCredential.html) | Yes|


### Return type: [Passkey](/API_docs/types/Passkey.html)

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

$Passkey = $MadelineProto->account->registerPasskey(credential: $InputPasskeyCredential, );
```

