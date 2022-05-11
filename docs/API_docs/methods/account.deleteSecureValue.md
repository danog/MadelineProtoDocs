---
title: "account.deleteSecureValue"
description: "Delete stored [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_deleteSecureValue.html
---
# Method: account.deleteSecureValue
[Back to methods index](index.html)



Delete stored [Telegram Passport](https://core.telegram.org/passport) documents, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|types|Array of [SecureValueType](/API_docs/types/SecureValueType.html) | Document types to delete | Yes|


### Return type: [Bool](/API_docs/types/Bool.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$Bool = $MadelineProto->account->deleteSecureValue(types: [SecureValueType, SecureValueType], );
```

