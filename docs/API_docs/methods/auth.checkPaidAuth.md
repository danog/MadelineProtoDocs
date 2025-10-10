---
title: "auth.checkPaidAuth"
description: "auth.checkPaidAuth parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_checkPaidAuth.html
---
# Method: auth.checkPaidAuth
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Optional|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Optional|
|form\_id|[long](/API_docs/types/long.html) | Yes|


### Return type: [auth.SentCode](/API_docs/types/auth.SentCode.html)

### Can users use this method: **YES**


### Can bots use this method: **YES**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->auth->checkPaidAuth(phone_number: 'string', phone_code_hash: 'string', form_id: $long, );
```

