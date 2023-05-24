---
title: "auth.resetLoginEmail"
description: "Reset the [login email »](https://core.telegram.org/api/auth#email-verification)."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_resetLoginEmail.html
---
# Method: auth.resetLoginEmail
[Back to methods index](index.html)



Reset the [login email »](https://core.telegram.org/api/auth#email-verification).

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number of the account | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Phone code hash, obtained as described in the [documentation »](https://core.telegram.org/api/auth) | Yes|


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

$auth_SentCode = $MadelineProto->auth->resetLoginEmail(phone_number: 'string', phone_code_hash: 'string', );
```

