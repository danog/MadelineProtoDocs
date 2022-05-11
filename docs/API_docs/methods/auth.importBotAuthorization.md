---
title: "auth.importBotAuthorization"
description: "You cannot use this method directly, use the botLogin method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importBotAuthorization.html
---
# Method: auth.importBotAuthorization
[Back to methods index](index.html)



You cannot use this method directly, use the botLogin method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](/API_docs/types/int.html) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|api\_hash|[string](/API_docs/types/string.html) | Application identifier hash (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|bot\_auth\_token|[string](/API_docs/types/string.html) | Bot token (see [bots](https://core.telegram.org/bots)) | Yes|


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
$auth_Authorization = $MadelineProto->auth->importBotAuthorization(api_id: int, api_hash: 'string', bot_auth_token: 'string', );
```

