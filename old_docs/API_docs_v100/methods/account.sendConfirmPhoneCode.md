---
title: account.sendConfirmPhoneCode
description: Send confirmation code to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/account_sendConfirmPhoneCode.html
---
# Method: account.sendConfirmPhoneCode  
[Back to methods index](index.md)


Send confirmation code to cancel account deletion, for more info [click here »](https://core.telegram.org/api/account-deletion)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|hash|[string](../types/string.md) | The hash from the service notification, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|
|settings|[CodeSettings](../types/CodeSettings.md) | Phone code settings | Yes|


### Return type: [auth.SentCode](../types/auth.SentCode.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth.SentCode = $MadelineProto->account->sendConfirmPhoneCode(['hash' => 'string', 'settings' => CodeSettings, ]);
```

Or, if you're into Lua:

```lua
auth.SentCode = account.sendConfirmPhoneCode({hash='string', settings=CodeSettings, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|HASH_INVALID|The provided hash is invalid|


