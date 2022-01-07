---
title: "auth.importBotAuthorization"
description: "You cannot use this method directly, use the botLogin method instead (see https://docs.madelineproto.xyz for more info)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importBotAuthorization.html
---
# Method: auth.importBotAuthorization
[Back to methods index](index.md)



You cannot use this method directly, use the botLogin method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](/API_docs/types/int.md) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|api\_hash|[string](/API_docs/types/string.md) | Application identifier hash (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|bot\_auth\_token|[string](/API_docs/types/string.md) | Bot token (see [bots](https://core.telegram.org/bots)) | Yes|


### Return type: [auth.Authorization](/API_docs/types/auth.Authorization.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_Authorization = $MadelineProto->auth->importBotAuthorization(['api_id' => int, 'api_hash' => 'string', 'bot_auth_token' => 'string', ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ACCESS_TOKEN_EXPIRED|Access token expired|
|400|ACCESS_TOKEN_INVALID|Access token invalid|
|400|API_ID_INVALID|API ID invalid|
|400|API_ID_PUBLISHED_FLOOD|This API id was published somewhere, you can't use it now|
|401|AUTH_KEY_INVALID|Auth key invalid|


