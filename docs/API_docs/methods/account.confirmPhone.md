---
title: "account.confirmPhone"
description: "Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_confirmPhone.html
---
# Method: account.confirmPhone
[Back to methods index](index.html)



Confirm a phone number to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Phone code hash, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|
|phone\_code|[string](/API_docs/types/string.html) | SMS code, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|


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
$Bool = $MadelineProto->account->confirmPhone(phone_code_hash: 'string', phone_code: 'string', );
```

