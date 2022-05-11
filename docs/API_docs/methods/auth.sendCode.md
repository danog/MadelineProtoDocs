---
title: "auth.sendCode"
description: "You cannot use this method directly, use the phoneLogin method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_sendCode.html
---
# Method: auth.sendCode
[Back to methods index](index.html)



You cannot use this method directly, use the phoneLogin method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number in international format | Yes|
|api\_id|[int](/API_docs/types/int.html) | Application identifier (see [App configuration](https://core.telegram.org/myapp)) | Yes|
|api\_hash|[string](/API_docs/types/string.html) | Application secret hash (see [App configuration](https://core.telegram.org/myapp)) | Yes|
|settings|[CodeSettings](/API_docs/types/CodeSettings.html) | Settings for the code type to send | Yes|


### Return type: [auth.SentCode](/API_docs/types/auth.SentCode.html)

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
$auth_SentCode = $MadelineProto->auth->sendCode(phone_number: 'string', api_id: int, api_hash: 'string', settings: CodeSettings, );
```

