---
title: "account.verifyEmail"
description: "Verify an email address."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_verifyEmail.html
---
# Method: account.verifyEmail
[Back to methods index](index.html)



Verify an email address.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|purpose|[EmailVerifyPurpose](/API_docs/types/EmailVerifyPurpose.html) | Verification purpose | Yes|
|verification|[EmailVerification](/API_docs/types/EmailVerification.html) | Email verification code or token | Yes|


### Return type: [account.EmailVerified](/API_docs/types/account.EmailVerified.html)

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

$account_EmailVerified = $MadelineProto->account->verifyEmail(purpose: $EmailVerifyPurpose, verification: $EmailVerification, );
```

