---
title: "account.sendVerifyEmailCode"
description: "Send the verification email code for telegram [passport](https://core.telegram.org/passport)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendVerifyEmailCode.html
---
# Method: account.sendVerifyEmailCode
[Back to methods index](index.html)



Send the verification email code for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](/API_docs/types/string.html) | The email where to send the code | Yes|


### Return type: [account.SentEmailCode](/API_docs/types/account.SentEmailCode.html)

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
$account_SentEmailCode = $MadelineProto->account->sendVerifyEmailCode(email: 'string', );
```

