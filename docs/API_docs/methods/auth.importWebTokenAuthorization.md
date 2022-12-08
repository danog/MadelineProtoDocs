---
title: "auth.importWebTokenAuthorization"
description: "auth.importWebTokenAuthorization parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importWebTokenAuthorization.html
---
# Method: auth.importWebTokenAuthorization
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|api\_id|[int](/API_docs/types/int.html) | Yes|
|api\_hash|[string](/API_docs/types/string.html) | Yes|
|web\_auth\_token|[string](/API_docs/types/string.html) | Yes|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$auth_Authorization = $MadelineProto->auth->importWebTokenAuthorization(api_id: int, api_hash: 'string', web_auth_token: 'string', );
```

