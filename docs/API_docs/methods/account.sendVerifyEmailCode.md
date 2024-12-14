---
title: "account.sendVerifyEmailCode"
description: "Send an email verification code."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendVerifyEmailCode.html
---
# Method: account.sendVerifyEmailCode
[Back to methods index](index.html)



Send an email verification code.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|purpose|[EmailVerifyPurpose](/API_docs/types/EmailVerifyPurpose.html) | Verification purpose. | Yes|
|email|[string](/API_docs/types/string.html) | The email where to send the code. | Optional|


### Return type: [account.SentEmailCode](/API_docs/types/account.SentEmailCode.html)

### Can userbots use this method: **YES**

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_SentEmailCode = $MadelineProto->account->sendVerifyEmailCode(purpose: $EmailVerifyPurpose, email: 'string', );
```

