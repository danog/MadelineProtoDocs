---
title: "auth.signUp"
description: "You cannot use this method directly, use the completeSignup method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_signUp.html
---
# Method: auth.signUp
[Back to methods index](index.html)



You cannot use this method directly, use the completeSignup method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number in the international format | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | SMS-message ID | Yes|
|first\_name|[string](/API_docs/types/string.html) | New user first name | Yes|
|last\_name|[string](/API_docs/types/string.html) | New user last name | Yes|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

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
$auth_Authorization = $MadelineProto->auth->signUp(phone_number: 'string', phone_code_hash: 'string', first_name: 'string', last_name: 'string', );
```

