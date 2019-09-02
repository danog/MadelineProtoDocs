---
title: auth.importBotAuthorization
description: You cannot use this method directly, use the bot_login method instead (see https://docs.madelineproto.xyz for more info)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: auth.importBotAuthorization  
[Back to methods index](index.md)


You cannot use this method directly, use the bot_login method instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|api\_id|[int](../types/int.md) | You cannot use this method directly, use the bot_login method instead (see https://docs.madelineproto.xyz for more info) | Yes|
|api\_hash|[string](../types/string.md) | You cannot use this method directly, use the bot_login method instead (see https://docs.madelineproto.xyz for more info) | Yes|
|bot\_auth\_token|[string](../types/string.md) | You cannot use this method directly, use the bot_login method instead (see https://docs.madelineproto.xyz for more info) | Yes|


### Return type: [auth\_Authorization](../types/auth_Authorization.md)

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


