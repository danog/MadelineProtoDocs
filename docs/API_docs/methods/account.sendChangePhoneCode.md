---
title: "account.sendChangePhoneCode"
description: "Verify a new phone number to associate to the current account"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendChangePhoneCode.html
---
# Method: account.sendChangePhoneCode
[Back to methods index](index.html)



Verify a new phone number to associate to the current account

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | New phone number | Yes|
|settings|[CodeSettings](/API_docs/types/CodeSettings.html) | Phone code settings | Yes|


### Return type: [auth.SentCode](/API_docs/types/auth.SentCode.html)

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
$auth_SentCode = $MadelineProto->account->sendChangePhoneCode(phone_number: 'string', settings: CodeSettings, );
```

