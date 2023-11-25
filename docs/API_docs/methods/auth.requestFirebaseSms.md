---
title: "auth.requestFirebaseSms"
description: "Request an SMS code via Firebase."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_requestFirebaseSms.html
---
# Method: auth.requestFirebaseSms
[Back to methods index](index.html)



Request an SMS code via Firebase.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](/API_docs/types/string.html) | Phone number | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Phone code hash returned by [auth.sendCode](../methods/auth.sendCode.html) | Yes|
|safety\_net\_token|[string](/API_docs/types/string.html) | On Android, a JWS object obtained as described in the [auth documentation »](https://core.telegram.org/api/auth) | Optional|
|ios\_push\_secret|[string](/API_docs/types/string.html) | Secret token received via an apple push notification | Optional|


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

$Bool = $MadelineProto->auth->requestFirebaseSms(phone_number: 'string', phone_code_hash: 'string', safety_net_token: 'string', ios_push_secret: 'string', );
```

