---
title: "account.saveSecureValue"
description: "Securely save [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_saveSecureValue.html
---
# Method: account.saveSecureValue
[Back to methods index](index.html)



Securely save [Telegram Passport](https://core.telegram.org/passport) document, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|value|[InputSecureValue](/API_docs/types/InputSecureValue.html) | Secure value, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption) | Yes|
|secure\_secret\_id|[long](/API_docs/types/long.html) | Passport secret hash, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption) | Yes|


### Return type: [SecureValue](/API_docs/types/SecureValue.html)

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
$SecureValue = $MadelineProto->account->saveSecureValue(value: InputSecureValue, secure_secret_id: long, );
```

