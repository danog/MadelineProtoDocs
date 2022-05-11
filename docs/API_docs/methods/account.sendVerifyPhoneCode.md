---
title: "account.sendVerifyPhoneCode"
description: "Send the verification phone code for telegram [passport](https://core.telegram.org/passport)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendVerifyPhoneCode.html
---
# Method: account.sendVerifyPhoneCode
[Back to methods index](index.html)



Send the verification phone code for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | The phone number to verify | Yes|
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
$auth_SentCode = $MadelineProto->account->sendVerifyPhoneCode(phone_number: 'string', settings: CodeSettings, );
```

