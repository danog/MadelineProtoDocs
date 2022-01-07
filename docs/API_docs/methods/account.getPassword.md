---
title: "account.getPassword"
description: "Obtain configuration for two-factor authorization with password"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_getPassword.html
---
# Method: account.getPassword
[Back to methods index](index.md)



Obtain configuration for two-factor authorization with password



### Return type: [account.Password](../types/account.Password.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$account_Password = $MadelineProto->account->getPassword();
```

