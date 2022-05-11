---
title: "auth.cancelCode"
description: "Cancel the login verification code"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_cancelCode.html
---
# Method: auth.cancelCode
[Back to methods index](index.html)



Cancel the login verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Phone code hash from [auth.sendCode](../methods/auth.sendCode.html) | Yes|


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
$Bool = $MadelineProto->auth->cancelCode(phone_number: 'string', phone_code_hash: 'string', );
```

