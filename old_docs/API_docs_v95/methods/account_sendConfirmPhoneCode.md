---
title: account.sendConfirmPhoneCode
description: Send confirmation phone code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendConfirmPhoneCode  
[Back to methods index](index.md)


Send confirmation phone code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[string](../types/string.md) | The hash | Yes|
|settings|[CodeSettings](../types/CodeSettings.md) | Code settings | Yes|


### Return type: [auth\_SentCode](../types/auth_SentCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendConfirmPhoneCode(['hash' => 'string', 'settings' => CodeSettings, ]);
```

Or, if you're into Lua:

```lua
auth_SentCode = account.sendConfirmPhoneCode({hash='string', settings=CodeSettings, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|HASH_INVALID|The provided hash is invalid|


