---
title: "auth.importWebTokenAuthorization"
description: "Login by importing an authorization token"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importWebTokenAuthorization.html
---
# Method: auth.importWebTokenAuthorization
[Back to methods index](index.html)



Login by importing an authorization token

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](/API_docs/types/int.html) | [API ID](https://core.telegram.org/api/obtaining_api_id) | Optional|
|api\_hash|[string](/API_docs/types/string.html) | [API hash](https://core.telegram.org/api/obtaining_api_id) | Optional|
|web\_auth\_token|[string](/API_docs/types/string.html) | The authorization token | Optional|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.html)

### Can users use this method: **YES**


### Can bots use this method: **NO**


### Can bots use this method over a business connection with the `businessConnectionId` flag: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_Authorization = $MadelineProto->auth->importWebTokenAuthorization(api_id: $int, api_hash: 'string', web_auth_token: 'string', );
```

