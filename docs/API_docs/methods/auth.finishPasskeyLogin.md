---
title: "auth.finishPasskeyLogin"
description: "auth.finishPasskeyLogin parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_finishPasskeyLogin.html
---
# Method: auth.finishPasskeyLogin
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|credential|[InputPasskeyCredential](/API_docs/types/InputPasskeyCredential.html) | Yes|
|from\_dc\_id|[int](/API_docs/types/int.html) | Optional|
|from\_auth\_key\_id|[long](/API_docs/types/long.html) | Optional|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

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

$auth_Authorization = $MadelineProto->auth->finishPasskeyLogin(credential: $InputPasskeyCredential, from_dc_id: $int, from_auth_key_id: $long, );
```

