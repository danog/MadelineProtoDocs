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


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendConfirmPhoneCode(['hash' => 'string', 'settings' => CodeSettings, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.sendConfirmPhoneCode`

Parameters:

hash - Json encoded string

settings - Json encoded CodeSettings




Or, if you're into Lua:

```lua
auth_SentCode = account.sendConfirmPhoneCode({hash='string', settings=CodeSettings, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|HASH_INVALID|The provided hash is invalid|


