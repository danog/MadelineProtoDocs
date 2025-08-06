---
title: "account.invalidateSignInCodes"
description: "Invalidate the specified login codes, see [here »](https://core.telegram.org/api/auth#invalidating-login-codes) for more info."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_invalidateSignInCodes.html
---
# Method: account.invalidateSignInCodes
[Back to methods index](index.html)



Invalidate the specified login codes, see [here »](https://core.telegram.org/api/auth#invalidating-login-codes) for more info.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|codes|Array of [string](/API_docs/types/string.html) | The login codes to invalidate. | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->account->invalidateSignInCodes(codes: ['string', 'string'], );
```

