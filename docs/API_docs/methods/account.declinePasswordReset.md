---
title: "account.declinePasswordReset"
description: "Abort a pending 2FA password reset, [see here for more info »](https://core.telegram.org/api/srp#password-reset)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_declinePasswordReset.html
---
# Method: account.declinePasswordReset
[Back to methods index](index.html)



Abort a pending 2FA password reset, [see here for more info »](https://core.telegram.org/api/srp#password-reset)



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
$Bool = $MadelineProto->account->declinePasswordReset();
```

