---
title: "account.verifyEmail"
description: "Verify an email address for telegram [passport](https://core.telegram.org/passport)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_verifyEmail.html
---
# Method: account.verifyEmail
[Back to methods index](index.html)



Verify an email address for telegram [passport](https://core.telegram.org/passport).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|email|[string](/API_docs/types/string.html) | The email to verify | Yes|
|code|[string](/API_docs/types/string.html) | The verification code that was received | Yes|


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
$Bool = $MadelineProto->account->verifyEmail(email: 'string', code: 'string', );
```

