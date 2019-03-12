---
title: account.sendVerifyPhoneCode
description: Send phone verification code
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: account.sendVerifyPhoneCode  
[Back to methods index](index.md)


Send phone verification code

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|phone\_number|[string](../types/string.md) | The phone number | Yes|
|settings|[CodeSettings](../types/CodeSettings.md) | Code settings | Yes|


### Return type: [auth\_SentCode](../types/auth_SentCode.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$auth_SentCode = $MadelineProto->account->sendVerifyPhoneCode(['phone_number' => 'string', 'settings' => CodeSettings, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - account.sendVerifyPhoneCode
* params - `{"phone_number": "string", "settings": CodeSettings, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/account.sendVerifyPhoneCode`

Parameters:

phone_number - Json encoded string

settings - Json encoded CodeSettings




Or, if you're into Lua:

```lua
auth_SentCode = account.sendVerifyPhoneCode({phone_number='string', settings=CodeSettings, })
```

