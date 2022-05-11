---
title: "account.resendPasswordEmail"
description: "Resend the code to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_resendPasswordEmail.html
---
# Method: account.resendPasswordEmail
[Back to methods index](index.html)



Resend the code to verify an email to use as [2FA recovery method](https://core.telegram.org/api/srp).



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
$Bool = $MadelineProto->account->resendPasswordEmail();
```

