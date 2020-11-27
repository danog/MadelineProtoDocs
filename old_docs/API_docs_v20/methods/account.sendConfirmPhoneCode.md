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
|allow\_flashcall|[Bool](../types/Bool.md) |  | Optional|
|hash|[string](../types/string.md) | The hash from the service notification, for more info [click here »](https://core.telegram.org/api/account-deletion) | Yes|
|current\_number|[Bool](../types/Bool.md) |  | Optional|


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

$auth_SentCode = $MadelineProto->account->sendConfirmPhoneCode(['allow_flashcall' => Bool, 'hash' => 'string', 'current_number' => Bool, ]);
```

Or, if you're into Lua:

```lua
auth_SentCode = account.sendConfirmPhoneCode({allow_flashcall=Bool, hash='string', current_number=Bool, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|HASH_INVALID|The provided hash is invalid|


