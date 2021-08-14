---
title: auth.importBotAuthorization
description: Login as a bot
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/auth_importBotAuthorization.html
---
# Method: auth.importBotAuthorization
[Back to methods index](index.md)



Login as a bot

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](../types/int.md) | Application identifier (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|api\_hash|[string](../types/string.md) | Application identifier hash (see. [App configuration](https://core.telegram.org/myapp)) | Yes|
|bot\_auth\_token|[string](../types/string.md) | Bot token (see [bots](https://core.telegram.org/bots)) | Yes|


### Return type: [auth.Authorization](../types/auth.Authorization.md)

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

Or, if you're into Lua:

```lua
auth_Authorization = auth.importBotAuthorization({api_id=int, api_hash='string', bot_auth_token='string', })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|ACCESS_TOKEN_EXPIRED|Access token expired|
|400|ACCESS_TOKEN_INVALID|Access token invalid|
|400|API_ID_INVALID|API ID invalid|
|401|AUTH_KEY_INVALID|Auth key invalid|


