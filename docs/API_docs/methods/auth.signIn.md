---
title: "auth.signIn"
description: "You cannot use this method directly, use the completePhoneLogin method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_signIn.html
---
# Method: auth.signIn
[Back to methods index](index.html)



You cannot use this method directly, use the completePhoneLogin method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number in the international format | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | SMS-message ID, obtained from [auth.sendCode](../methods/auth.sendCode.html) | Yes|
|phone\_code|[string](/API_docs/types/string.html) | Valid numerical code from the SMS-message | Yes|


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
$auth_Authorization = $MadelineProto->auth->signIn(phone_number: 'string', phone_code_hash: 'string', phone_code: 'string', );
```

