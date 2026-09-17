---
title: "auth.firebasePnvSignUp"
description: "auth.firebasePnvSignUp parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_firebasePnvSignUp.html
---
# Method: auth.firebasePnvSignUp
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|no\_joined\_notifications|[Bool](/API_docs/types/Bool.html) | Optional|
|first\_name|[string](/API_docs/types/string.html) | Optional|
|last\_name|[string](/API_docs/types/string.html) | Optional|


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

$auth_Authorization = $MadelineProto->auth->firebasePnvSignUp(no_joined_notifications: $Bool, first_name: 'string', last_name: 'string', );
```

