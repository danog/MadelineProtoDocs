---
title: "account.confirmPasswordEmail"
description: "Verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_confirmPasswordEmail.html
---
# Method: account.confirmPasswordEmail
[Back to methods index](index.html)



Verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|code|[string](/API_docs/types/string.html) | The phone code that was received after [setting a recovery email](https://core.telegram.org/api/srp#email-verification) | Yes|


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
$Bool = $MadelineProto->account->confirmPasswordEmail(code: 'string', );
```

